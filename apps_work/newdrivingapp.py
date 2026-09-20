import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# 1. Official WA DOL Rubric Configuration Map
RUBRIC = {
    "Backing": {"minor": 2, "major": 4, "cap": 4},
    "Parallel Parking": {"minor": 2, "major": 4, "cap": 4},
    "Park and Start on Hill": {"minor": 2, "major": 4, "cap": 4},
    "Starting": {"minor": 2, "major": 4, "cap": 4},
    "Lane Travel": {"minor": 2, "major": 4, "cap": 4},
    "Traffic Control Devices": {"minor": 2, "major": 4, "cap": 4},
    "Stop Signs / Flashing Lights": {"minor": 2, "major": 4, "cap": 4},
    "Traffic Signal Lights": {"minor": 2, "major": 4, "cap": 4},
    "Mechanical Operation": {"minor": 1, "major": 2, "cap": 2},
    "Left Turns": {"minor": 3, "major": 6, "cap": 6},
    "Right Turns": {"minor": 3, "major": 6, "cap": 6},
    "Uncontrolled Intersections": {"minor": 2, "major": 4, "cap": 4},
    "Following": {"minor": 2, "major": 4, "cap": 4},
    "Passing": {"minor": 2, "major": 4, "cap": 4},
    "Right-of-Way": {"minor": 2, "major": 4, "cap": 4},
    "General Driving Performance": {"minor": 2, "major": 4, "cap": 4}
}

class DOLTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WA DOL Driving Test Evaluator v1.2")
        self.root.geometry("550x840")  
        self.root.configure(bg="#f5f5f5")
        
        # State Tracking Engines
        self.score = 100
        self.category_losses = {name: 0 for name in RUBRIC}
        self.severity_history = {name: {"minor": False, "major": False} for name in RUBRIC}
        self.infraction_history = []
        self.dangerous_action = False
        self.da_reason = ""
        self.verified_age = None
        self.verified_permit_expiry = ""
        
        # Automatically grab the current test start parameters
        current_moment = datetime.now()
        self.test_date = current_moment.strftime("%m/%d/%Y")
        self.start_time = current_moment.strftime("%I:%M %p")
        
        self.build_ui()

    def build_ui(self):
        # Header Canvas Label
        header_frame = tk.Frame(self.root, bg="#006644", height=60)
        header_frame.pack(fill="x", side="top")
        tk.Label(header_frame, text="WASHINGTON STATE DOL DRIVE TEST", font=("Arial", 14, "bold"), fg="white", bg="#006644").pack(pady=15)
        
        # Admin Metadata Context Frame
        admin_frame = tk.LabelFrame(self.root, text=" Applicant & Compliance Verification ", font=("Arial", 10, "bold"), bg="#f5f5f5", padx=10, pady=10)
        admin_frame.pack(fill="x", padx=15, pady=10)
        
        # Row 0: Full Name
        tk.Label(admin_frame, text="Full Name:", bg="#f5f5f5", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=4)
        self.name_entry = tk.Entry(admin_frame, font=("Arial", 10), width=25)
        self.name_entry.grid(row=0, column=1, columnspan=2, sticky="w", pady=4, padx=5)
        
        # Row 1: Date of Birth
        tk.Label(admin_frame, text="DOB (MM/DD/YYYY):", bg="#f5f5f5", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=4)
        self.dob_entry = tk.Entry(admin_frame, font=("Arial", 10), width=15)
        self.dob_entry.grid(row=1, column=1, sticky="w", pady=4, padx=5)
        
        # Row 2: Permit Expiration Field
        tk.Label(admin_frame, text="Permit Expiry (MM/DD/YYYY):", bg="#f5f5f5", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=4)
        self.permit_expiry_entry = tk.Entry(admin_frame, font=("Arial", 10), width=15)
        self.permit_expiry_entry.grid(row=2, column=1, sticky="w", pady=4, padx=5)
        
        # Row 1 & 2 Anchor Button: Unified Verification Gatekeeper 
        self.verify_btn = tk.Button(admin_frame, text="Run Credentials Check", bg="#006644", fg="white", font=("Arial", 9, "bold"), width=20, command=self.run_credentials_verification)
        self.verify_btn.grid(row=1, column=2, rowspan=2, padx=10, pady=4, sticky="ns")
        
        self.meta_label = tk.Label(admin_frame, text=f"Date: {self.test_date}  |  Started: {self.start_time}", font=("Arial", 9, "italic"), bg="#f5f5f5")
        self.meta_label.grid(row=3, column=0, columnspan=3, sticky="w", pady=5)
        
        # Main Visual Scoring Dashboard Component
        score_frame = tk.Frame(self.root, bg="#f5f5f5")
        score_frame.pack(fill="x", padx=15, pady=5)
        
        self.score_label = tk.Label(score_frame, text="SCORE: 100", font=("Arial", 24, "bold"), fg="#006644", bg="#f5f5f5")
        self.score_label.pack(side="left", padx=10)
        
        # Test Evaluation Workspace Input Controls
        self.eval_frame = tk.LabelFrame(self.root, text=" Scoring Controls ", font=("Arial", 10, "bold"), bg="#f5f5f5", padx=10, pady=10)
        self.eval_frame.pack(fill="x", padx=15, pady=10)
        
        tk.Label(self.eval_frame, text="Select Driving Criteria Category:", bg="#f5f5f5").pack(anchor="w")
        self.category_select = ttk.Combobox(self.eval_frame, values=list(RUBRIC.keys()), state="readonly", font=("Arial", 10), width=40)
        self.category_select.pack(pady=5, fill="x")
        self.category_select.current(0)
        
        # Button Panel Configurations
        btn_frame = tk.Frame(self.eval_frame, bg="#f5f5f5")
        btn_frame.pack(fill="x", pady=5)
        
        self.minor_btn = tk.Button(btn_frame, text="Log Minor Error", bg="#ffe699", font=("Arial", 10, "bold"), width=15, command=lambda: self.apply_error("minor"))
        self.minor_btn.pack(side="left", padx=5, expand=True)
        
        self.major_btn = tk.Button(btn_frame, text="Log Major Error", bg="#f4b084", font=("Arial", 10, "bold"), width=15, command=lambda: self.apply_error("major"))
        self.major_btn.pack(side="left", padx=5, expand=True)
        
        self.da_btn = tk.Button(btn_frame, text="Dangerous Action", bg="#f8cecc", font=("Arial", 10, "bold"), fg="red", width=15, command=self.apply_dangerous_action)
        self.da_btn.pack(side="left", padx=5, expand=True)
        
        # History Feed Logs Box Widget (Fixed font size to integer 9)
        tk.Label(self.root, text="Live Exam History Log Feedback:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(anchor="w", padx=15)
        self.history_box = tk.Text(self.root, height=10, width=60, font=("Courier", 9), state="disabled", bg="white", relief="sunken")
        self.history_box.pack(padx=15, pady=5, fill="both", expand=True)
        
        # Finalization Trigger Anchor Button
        self.finalize_btn = tk.Button(self.root, text="FINALIZE ROAD EXAM & RECORD", bg="#006644", fg="white", font=("Arial", 12, "bold"), pady=8, command=self.finalize_exam)
        self.finalize_btn.pack(fill="x", padx=15, pady=15)
        
        self.lock_scoring_controls(True)

    def lock_scoring_controls(self, should_lock):
        state = "disabled" if should_lock else "normal"
        combo_state = "disabled" if should_lock else "readonly"
        
        self.category_select.config(state=combo_state)
        self.minor_btn.config(state=state)
        self.major_btn.config(state=state)
        self.da_btn.config(state=state)
        self.finalize_btn.config(state=state)

    def run_credentials_verification(self):
        dob_text = self.dob_entry.get().strip()
        expiry_text = self.permit_expiry_entry.get().strip()
        
        if not dob_text or not expiry_text:
            messagebox.showerror("Input Error", "Please fill out both the Date of Birth and the Permit Expiration Date fields.")
            return
            
        try:
            current_moment = datetime.now()
            dob_date = datetime.strptime(dob_text, "%m/%d/%Y")
            expiry_date = datetime.strptime(expiry_text, "%m/%d/%Y")
            
            # Age Engine
            age = current_moment.year - dob_date.year - ((current_moment.month, current_moment.day) < (dob_date.month, dob_date.day))
            is_expired = expiry_date.date() < current_moment.date()
            
            if age < 15:
                messagebox.showerror("REGULATORY FAILURE", f"Applicant age verification failed: {age} years old.\n\nUnder Washington State rules, an individual must be at least 15 years old to attempt a skills exam. System locked.")
                self.verified_age = None
                self.lock_scoring_controls(True)
                
            elif is_expired:
                days_expired = (current_moment.date() - expiry_date.date()).days
                messagebox.showerror("COMPLIANCE FAILURE", f"Instructional Permit validation failed.\n\nThe provided permit expired on {expiry_text} ({days_expired} days ago).\nTesting cannot legally proceed with an invalid or expired credential. System locked.")
                self.verified_age = None
                self.lock_scoring_controls(True)
                
            else:
                messagebox.showinfo("Credentials Validated", f"✓ Applicant Age: {age} years old\n✓ Permit Status: VALID (Active through {expiry_text})\n\nScoring control console has been securely unlocked.")
                self.verified_age = age
                self.verified_permit_expiry = expiry_text
                self.lock_scoring_controls(False)
                self.meta_label.config(text=f"Date: {self.test_date}  |  Started: {self.start_time}  |  Age: {age}  |  Permit Exp: {expiry_text}")
                
        except ValueError:
            messagebox.showerror("Format Error", "Invalid date entry structure. Please make sure to follow the explicit pattern MM/DD/YYYY exactly.")

    def apply_error(self, severity_key):
        if self.dangerous_action:
            messagebox.showwarning("Terminated", "Test already terminated due to a Dangerous Action.")
            return
        cat = self.category_select.get()
        rules = RUBRIC[cat]
        current_loss = self.category_losses[cat]
        max_cap = rules["cap"]
        
        if current_loss >= max_cap:
            messagebox.showinfo("Capped", f"'{cat}' has already reached its processing penalty cap (-{max_cap} pts).")
            return
            
        if self.severity_history[cat][severity_key]:
            messagebox.showinfo("Duplicate", f"A {severity_key} error was already recorded for '{cat}'. Deducting 0 points.")
            raw_penalty = 0
            dup_note = " [DUPLICATE]"
        else:
            raw_penalty = rules[severity_key]
            dup_note = ""
            
        if current_loss + raw_penalty > max_cap:
            actual_deduction = max_cap - current_loss
            cap_note = " [CAPPED]"
        else:
            actual_deduction = raw_penalty
            cap_note = ""
            
        self.severity_history[cat][severity_key] = True
        self.category_losses[cat] += actual_deduction
        self.score -= actual_deduction
        if self.score < 0: self.score = 0
        
        self.update_score_display()
        
        log_txt = f"• {cat} ({severity_key.upper()}): -{actual_deduction} pts{dup_note}{cap_note}\n"
        self.infraction_history.append(log_txt.strip())
        self.post_to_log(log_txt)

    def apply_dangerous_action(self):
        self.dangerous_action = True
        self.score = 0
        self.update_score_display()
        self.post_to_log("!! CRITICAL EXAM SAFETY TRIGGER: Dangerous Action Recorded (SCORE WIPED TO 0) !!\n")
        messagebox.showerror("Test Terminated", "Dangerous Action logged. Test has automatically failed.")

    def update_score_display(self):
        self.score_label.config(text=f"SCORE: {self.score}")
        if self.score >= 80:
            self.score_label.config(fg="#006644")
        else:
            self.score_label.config(fg="red")

    def post_to_log(self, text):
        self.history_box.config(state="normal")
        self.history_box.insert(tk.END, text)
        self.history_box.see(tk.END)
        self.history_box.config(state="disabled")

    def finalize_exam(self):
        student_name = self.name_entry.get().strip() or "Anonymous Applicant"
        age = self.verified_age if self.verified_age is not None else "Unknown"
        end_time = datetime.now().strftime("%I:%M %p")
            
        # Outcomes Logic
        if self.dangerous_action:
            status = "FAILED"
            outcome_text = "FAILED due to an automatic Dangerous Action violation."
        else:
            status = "PASSED" if self.score >= 80 else "FAILED"
            outcome_text = f"PASSED OFFICIAL SKILLS TEST" if status == "PASSED" else f"FAILED due to insufficient score (Minimum required is 80)"
            
        # Build Advisory Packet Next Steps Text Block
        advisory_msg = ""
        if status == "PASSED":
            if isinstance(age, int) and age < 18:
                advisory_msg = (
                    "\n\nNEXT STEPS FOR MINOR APPLICANT:\n"
                    "1. Must hold WA Instructional Permit for at least 6 consecutive months.\n"
                    "2. Confirm completion of 50 total practice hours (with 10 at night).\n"
                    "3. Head online to your License eXpress account to secure your IDL.\n"
                    "4. Restrictions: No passengers under 20 (except family) for 6 months."
                )
            else:
                advisory_msg = (
                    "\n\nNEXT STEPS FOR ADULT APPLICANT:\n"
                    "1. Score has been securely routed electronically to the WA DOL database.\n"
                    "2. Log into your License eXpress account online to process fees and print a temporary license.\n"
                    "3. Plastic identity card will arrive by post within 7-10 business days."
                )
        else:
            advisory_msg = "\n\nRETEST PROTOCOLS:\n• Schedule a remedial training drive block with an instructor before re-booking."

        summary_report = (
            f"Official Result Sheet for: {student_name}\n"
            f"Final Tabulated Score: {self.score} / 100\n"
            f"Status Outcome: {status}\n\n"
            f"Details: {outcome_text}"
            f"{advisory_msg}"
        )
        
        messagebox.showinfo("Official Exam Sheet Generated", summary_report)
        
        # Append data ledger to permanent CSV File database storage archive line
        csv_file = "driving_school_records.csv"
        file_exists = os.path.isfile(csv_file)
        flat_history_summary = " | ".join(self.infraction_history) if self.infraction_history else "Clean Driving Sheet Logged"
        
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "Student Name", "Age/DOB", "Permit Expiry", "Score", "Status", "Detailed Outcome Summary", "Raw Infractions Tracking Data Log"])
            writer.writerow([f"{self.test_date} {self.start_time}", student_name, f"Age: {age}", self.verified_permit_expiry, self.score, status, outcome_text, flat_history_summary])
            
        self.root.quit()

if __name__ == "__main__":
    window = tk.Tk()
    app = DOLTestApp(window)
    window.mainloop()