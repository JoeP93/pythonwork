import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# Official Washington State DLE-520-001A Rubric Point Values Mapping
RUBRIC = {
    "Backing": {"DP": 4, "LS": 2, "CP": 0, "cap": 4},
    "Parallel Parking": {"DP": 4, "LS": 2, "CP": 2, "cap": 4},
    "Park and Start on Hill": {"DP": 4, "LS": 2, "CP": 2, "cap": 4},
    "Starting": {"DP": 4, "LS": 0, "CP": 0, "cap": 4},
    "Lane Travel": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Traffic Control Devices": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Stop Signs/ Flashing Lights": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Traffic Signal Lights": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Mechanical Operation": {"DP": 2, "LS": 1, "CP": 0, "cap": 2},
    "Left Turns": {"DP": 6, "LS": 3, "CP": 3, "cap": 6},
    "Right Turns": {"DP": 6, "LS": 3, "CP": 3, "cap": 6},
    "Uncontrolled Intersections": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Following": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Passing": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "Right-of-Way": {"DP": 4, "LS": 0, "CP": 2, "cap": 4},
    "General Driving Performance": {"DP": 4, "LS": 0, "CP": 2, "cap": 4}
}

# Granular Form Markings Sub-Category Mapping Matrix (Exhaustive Form Replication)
SUB_INFRACTIONS = {
    "Backing": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Sw (Steering)", "Stp (Stop)", "Spd (Speed)", "Wide", "Curb", "2Stp (2-Step)", "Unable Road"],
        "LS": ["Wide", "Dis (Distance)", "Cut", "Curb", "Weave"], "CP": []
    },
    "Parallel Parking": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Cont (Control)", "Thru", "Curb", "Unable Road"],
        "LS": ["Curb", "1 1/2", "Joc (Jockeying)"], "CP": ["Try", "Dis (Distance)", "Cent (Centering)"]
    },
    "Park and Start on Hill": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Pb (Parking Brake)", "Gear", "Wh (Wheels)", "Dis (Distance)", "Ctl (Control)", "Curb"],
        "LS": ["Joc (Jockeying)", "Curb", "Ctl (Control)"], "CP": ["Dis (Distance)"]
    },
    "Starting": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Curb"], "LS": [], "CP": []
    },
    "Lane Travel": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Rt Lanes (Right Lanes)", "Curb"], "LS": [], "CP": ["Lanes", "Weave"]
    },
    "Traffic Control Devices": {
        "DP": ["Ftc (Failure to Comply)"], "LS": [], "CP": ["Stp (Stop)", "Hes (Hesitation)"]
    },
    "Stop Signs/ Flashing Lights": {
        "DP": ["Vis (Vision)", "2Stp (2-Step)"], "LS": [], "CP": ["Sl (Stop Line)", "Cw (Crosswalk)", "Int (Intersection)"]
    },
    "Traffic Signal Lights": {
        "DP": ["Vis (Vision)", "Yel (Yellow Light Violation)"], "LS": [], "CP": ["Sl (Slow)", "Cw (Crosswalk)", "Ror (Right on Red)", "Hes (Hesitation)"]
    },
    "Mechanical Operation": {
        "DP": ["Sig (Signal)", "Hands", "Arm Pos", "1Hand", "Clutch", "Gear", "Brk (Brake)"],
        "LS": ["Clutch", "Stall", "Start", "Races", "Gear", "PB (Parking Brake)", "Ctl (Control)", "Spins"], "CP": []
    },
    "Left Turns": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Spd (Speed)", "Cut", "Pos (Position)", "Wide"],
        "LS": ["Wide"], "CP": ["Late", "Stp (Stop)", "Lanes"]
    },
    "Right Turns": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Spd (Speed)", "Cut", "Pos (Position)", "Wide"],
        "LS": ["Wide"], "CP": ["Late", "Stp (Stop)", "Lanes"]
    },
    "Uncontrolled Intersections": {
        "DP": ["Vis (Vision)", "Spd (Speed)"], "LS": [], "CP": ["Stp (Stop)", "Hes (Hesitation)"]
    },
    "Following": {
        "DP": ["Close"], "LS": [], "CP": ["Dis (Distance)"]
    },
    "Passing": {
        "DP": ["Vis (Vision)", "Sig (Signal)", "Wide", "Close", "Left", "Right"], "LS": [], "CP": ["Pass"]
    },
    "Right-of-Way": {
        "DP": ["Row (Right of Way)"], "LS": [], "CP": ["Row (Right of Way)"]
    },
    "General Driving Performance": {
        "DP": ["Attn (Attention)", "Slow", "Stp (Stop)"], "LS": [], "CP": ["Slow", "Hes (Hesitation)"]
    }
}

class DOLTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WA DOL Driving Test Evaluator - DLE-520 Pro Engine")
        self.root.geometry("560x900")  
        
        self.bg_dark = "#1e222b"       
        self.bg_panel = "#282c34"      
        self.fg_white = "#abb2bf"      
        self.fg_bright = "#ffffff"     
        self.accent_green = "#4caf50"  
        self.accent_amber = "#ffb74d"  
        
        self.root.configure(bg=self.bg_dark)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=self.bg_panel, background=self.bg_dark, foreground=self.fg_bright, arrowcolor=self.accent_green)
        
        self.score = 100
        self.category_losses = {name: 0 for name in RUBRIC}
        self.severity_history = {name: [] for name in RUBRIC} # Dynamic tracking to allow multiple errors
        self.infraction_history = []
        self.dangerous_action_count = 0 # Counter allows tracking multiple critical errors
        
        self.verified_age = None
        self.verified_permit_expiry = ""
        self.verified_examiner = ""  
        
        current_moment = datetime.now()
        self.test_date = current_moment.strftime("%m/%d/%Y")
        self.start_time = current_moment.strftime("%I:%M %p")
        
        self.build_ui()

    def build_ui(self):
        header_frame = tk.Frame(self.root, bg=self.accent_green, height=65)
        header_frame.pack(fill="x", side="top")
        tk.Label(header_frame, text="WASHINGTON STATE DOL DRIVE TEST", font=("Segoe UI", 14, "bold"), fg=self.fg_bright, bg=self.accent_green).pack(pady=18)
        
        admin_frame = tk.LabelFrame(self.root, text=" Applicant & Compliance Verification ", font=("Segoe UI", 10, "bold"), bg=self.bg_panel, fg=self.accent_green, padx=12, pady=12, bd=1, relief="solid")
        admin_frame.pack(fill="x", padx=15, pady=12)
        
        tk.Label(admin_frame, text="Examiner Name:", bg=self.bg_panel, fg=self.fg_white, font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.examiner_entry = tk.Entry(admin_frame, font=("Segoe UI", 10), bg=self.bg_dark, fg=self.fg_bright, insertbackground="white", bd=1, relief="solid", width=22)
        self.examiner_entry.grid(row=0, column=1, columnspan=2, sticky="w", pady=5, padx=8)
        
        tk.Label(admin_frame, text="Student Name:", bg=self.bg_panel, fg=self.fg_white, font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(admin_frame, font=("Segoe UI", 10), bg=self.bg_dark, fg=self.fg_bright, insertbackground="white", bd=1, relief="solid", width=22)
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky="w", pady=5, padx=8)
        
        tk.Label(admin_frame, text="DOB (MM/DD/YYYY):", bg=self.bg_panel, fg=self.fg_white, font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.dob_entry = tk.Entry(admin_frame, font=("Segoe UI", 10), bg=self.bg_dark, fg=self.fg_bright, insertbackground="white", bd=1, relief="solid", width=12)
        self.dob_entry.grid(row=2, column=1, sticky="w", pady=5, padx=8)
        
        tk.Label(admin_frame, text="Permit Expiry (MM/DD/YYYY):", bg=self.bg_panel, fg=self.fg_white, font=("Segoe UI", 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.permit_expiry_entry = tk.Entry(admin_frame, font=("Segoe UI", 10), bg=self.bg_dark, fg=self.fg_bright, insertbackground="white", bd=1, relief="solid", width=12)
        self.permit_expiry_entry.grid(row=3, column=1, sticky="w", pady=5, padx=8)
        
        self.verify_btn = tk.Button(admin_frame, text="Run Credentials Check", bg=self.accent_green, fg=self.fg_bright, activebackground="#388e3c", activeforeground="white", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", width=18, command=self.run_credentials_verification)
        self.verify_btn.grid(row=2, column=2, rowspan=2, padx=10, pady=5, sticky="ns")
        
        self.meta_label = tk.Label(admin_frame, text=f"Date: {self.test_date}  |  Started: {self.start_time}", font=("Segoe UI", 9, "italic"), bg=self.bg_panel, fg=self.fg_white)
        self.meta_label.grid(row=4, column=0, columnspan=3, sticky="w", pady=6)
        
        score_frame = tk.Frame(self.root, bg=self.bg_dark)
        score_frame.pack(fill="x", padx=15, pady=5)
        
        self.score_label = tk.Label(score_frame, text="SCORE: 100", font=("Segoe UI", 26, "bold"), fg=self.accent_green, bg=self.bg_dark)
        self.score_label.pack(side="left", padx=10)
        
        self.eval_frame = tk.LabelFrame(self.root, text=" DLE-520 Automated Evaluation Dashboard ", font=("Segoe UI", 10, "bold"), bg=self.bg_panel, fg=self.accent_green, padx=12, pady=12, bd=1, relief="solid")
        self.eval_frame.pack(fill="x", padx=15, pady=10)
        
        tk.Label(self.eval_frame, text="Select Driving Criteria Category:", bg=self.bg_panel, fg=self.fg_white, font=("Segoe UI", 10)).pack(anchor="w")
        self.category_select = ttk.Combobox(self.eval_frame, values=list(RUBRIC.keys()), state="readonly", font=("Segoe UI", 10), width=42)
        self.category_select.pack(pady=8, fill="x")
        self.category_select.current(0)
        
        btn_frame = tk.Frame(self.eval_frame, bg=self.bg_panel)
        btn_frame.pack(fill="x", pady=6)
        
        self.dp_btn = tk.Button(btn_frame, text="Log DP Error", bg="#ef596f", fg=self.fg_bright, font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", width=11, command=lambda: self.launch_sub_infraction_window("DP"))
        self.dp_btn.pack(side="left", padx=3, expand=True, fill="x")
        
        self.ls_btn = tk.Button(btn_frame, text="Log LS Error", bg="#e5c07b", fg=self.bg_dark, font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", width=11, command=lambda: self.launch_sub_infraction_window("LS"))
        self.ls_btn.pack(side="left", padx=3, expand=True, fill="x")
        
        self.cp_btn = tk.Button(btn_frame, text="Log CP Error", bg="#61afef", fg=self.fg_bright, font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", width=11, command=lambda: self.launch_sub_infraction_window("CP"))
        self.cp_btn.pack(side="left", padx=3, expand=True, fill="x")
        
        self.da_btn = tk.Button(btn_frame, text="Dangerous Action", bg="#f44336", font=("Segoe UI", 10, "bold"), fg=self.fg_bright, bd=0, cursor="hand2", width=12, command=self.apply_dangerous_action)
        self.da_btn.pack(side="left", padx=3, expand=True, fill="x")
        
        tk.Label(self.root, text="Live Exam History Log Feedback:", font=("Segoe UI", 10, "bold"), bg=self.bg_dark, fg=self.fg_white).pack(anchor="w", padx=15, pady=4)
        self.history_box = tk.Text(self.root, height=10, width=60, font=("Consolas", 10), state="disabled", bg=self.bg_panel, fg="#98c379", insertbackground="white", bd=1, relief="solid")
        self.history_box.pack(padx=15, pady=5, fill="both", expand=True)
        
        self.finalize_btn = tk.Button(self.root, text="FINALIZE ROAD EXAM & RECORD", bg=self.accent_green, fg=self.fg_bright, activebackground="#388e3c", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", pady=10, command=self.finalize_exam)
        self.finalize_btn.pack(fill="x", padx=15, pady=18)
        
        self.lock_scoring_controls(True)

    def lock_scoring_controls(self, should_lock):
        state = "disabled" if should_lock else "normal"
        combo_state = "disabled" if should_lock else "readonly"
        self.category_select.config(state=combo_state)
        self.dp_btn.config(state=state)
        self.ls_btn.config(state=state)
        self.cp_btn.config(state=state)
        self.da_btn.config(state=state)
        self.finalize_btn.config(state=state)

    def run_credentials_verification(self):
        examiner_text = self.examiner_entry.get().strip()
        dob_text = self.dob_entry.get().strip()
        expiry_text = self.permit_expiry_entry.get().strip()
        
        if not examiner_text:
            messagebox.showerror("Input Error", "Please provide the Examiner Name to log this session.")
            return
        if not dob_text or not expiry_text:
            messagebox.showerror("Input Error", "Please fill out both DOB and Permit fields.")
            return
            
        try:
            current_moment = datetime.now()
            dob_date = datetime.strptime(dob_text, "%m/%d/%Y")
            expiry_date = datetime.strptime(expiry_text, "%m/%d/%Y")
            
            age = current_moment.year - dob_date.year - ((current_moment.month, current_moment.day) < (dob_date.month, dob_date.day))
            is_expired = expiry_date.date() < current_moment.date()
            
            if age < 15:
                messagebox.showerror("REGULATORY FAILURE", f"Applicant age verification failed: {age} years old.")
                self.lock_scoring_controls(True)
            elif is_expired:
                messagebox.showerror("COMPLIANCE FAILURE", f"Permit expired on {expiry_text}. Testing blocked.")
                self.lock_scoring_controls(True)
            else:
                messagebox.showinfo("Credentials Validated", f"✓ Examiner: {examiner_text}\n✓ Age: {age}\n✓ Permit: VALID")
                self.verified_age = age
                self.verified_permit_expiry = expiry_text
                self.verified_examiner = examiner_text
                self.lock_scoring_controls(False)
                self.meta_label.config(text=f"Examiner: {examiner_text}  |  Age: {age}  |  Permit Exp: {expiry_text}")
        except ValueError:
            messagebox.showerror("Format Error", "Use MM/DD/YYYY exactly.")

    def launch_sub_infraction_window(self, component_key):
        cat = self.category_select.get()
        options = SUB_INFRACTIONS[cat][component_key]
        
        if not options:
            messagebox.showinfo("Not Applicable", f"The DLE-520 form has no '{component_key}' checkmarks designated under '{cat}'.")
            return

        # Continuous Logging Engine: Let popup open even if already capped or failed
        pop = tk.Toplevel(self.root)
        pop.title(f"Select {component_key} Violation Reason")
        pop.geometry("340x380")
        pop.configure(bg=self.bg_dark)
        pop.grab_set()  
        
        tk.Label(pop, text=f"{cat.upper()} - Select {component_key} Item:", font=("Segoe UI", 10, "bold"), bg=self.bg_dark, fg=self.accent_green, wraplength=300).pack(pady=10)
        
        for item in options:
            btn = tk.Button(pop, text=item, font=("Segoe UI", 9, "bold"), bg=self.bg_panel, fg=self.fg_bright, bd=1, relief="solid", activebackground=self.accent_green, cursor="hand2", pady=4)
            btn.config(command=lambda choice=item: self.commit_granular_error(cat, component_key, choice, pop))
            btn.pack(fill="x", padx=20, pady=3)

    def commit_granular_error(self, cat, component_key, reason, window_handle):
        rules = RUBRIC[cat]
        current_loss = self.category_losses[cat]
        max_cap = rules["cap"]
        raw_penalty = rules[component_key]
        
        # Check if this exact sub-item combo was checked off already to block duplicate point spikes
        infraction_id = f"{component_key}-{reason}"
        if infraction_id in self.severity_history[cat]:
            messagebox.showinfo("Duplicate Mark", f"'{reason}' is already checked off under '{cat}' on the form.")
            window_handle.destroy()
            return
            
        # Determine actual deduction based on current category penalty processing caps
        if current_loss >= max_cap:
            actual_deduction = 0
            note = " [CAPPED]"
        elif current_loss + raw_penalty > max_cap:
            actual_deduction = max_cap - current_loss
            note = " [CAPPED]"
        else:
            actual_deduction = raw_penalty
            note = ""
            
        self.severity_history[cat].append(infraction_id)
        self.category_losses[cat] += actual_deduction
        self.score -= actual_deduction
        if self.score < 0: self.score = 0
        
        self.update_score_display()
        window_handle.destroy() 
        
        log_txt = f"• {cat} ({component_key} - {reason}): -{actual_deduction} pts{note}\n"
        self.infraction_history.append(log_txt.strip())
        self.post_to_log(log_txt)

    def apply_dangerous_action(self):
        self.dangerous_action_count += 1
        self.score = 0 # Score remains zero for administrative automatic failure tracking
        self.update_score_display()
        
        log_txt = f"!! CRITICAL EXAM SAFETY TRIGGER: Dangerous Action #{self.dangerous_action_count} Recorded !!\n"
        self.infraction_history.append(log_txt.strip())
        self.post_to_log(log_txt)
        messagebox.showerror("Dangerous Action Logged", f"Dangerous Action #{self.dangerous_action_count} recorded successfully.")

    def update_score_display(self):
        self.score_label.config(text=f"SCORE: {self.score}")
        if self.score >= 80 and self.dangerous_action_count == 0:
            self.score_label.config(fg=self.accent_green)
        else:
            self.score_label.config(fg=self.accent_amber)

    def post_to_log(self, text):
        self.history_box.config(state="normal")
        self.history_box.insert(tk.END, text)
        self.history_box.see(tk.END)
        self.history_box.config(state="disabled")

    def finalize_exam(self):
        student_name = self.name_entry.get().strip() or "Anonymous Applicant"
        age = self.verified_age if self.verified_age is not None else "Unknown"
        
        status = "PASSED" if (self.score >= 80 and self.dangerous_action_count == 0) else "FAILED"
        
        if self.dangerous_action_count > 0:
            outcome_text = f"FAILED due to {self.dangerous_action_count} Automatic Disqualifying Dangerous Actions."
        else:
            outcome_text = "PASSED OFFICIAL SKILLS TEST" if status == "PASSED" else "FAILED due to insufficient point score."
        
        summary_report = f"Official Result Sheet for: {student_name}\nFinal Score: {self.score} / 100\nOutcome: {status}\n\n{outcome_text}"
        messagebox.showinfo("Official Exam Sheet Generated", summary_report)
        
        csv_file = "driving_school_records.csv"
        file_exists = os.path.isfile(csv_file)
        flat_history_summary = " | ".join(self.infraction_history) if self.infraction_history else "Clean Sheet"
        
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "Examiner", "Student", "Age", "Permit Expiry", "Score", "Status", "Raw Infractions Tracking Log"])
            writer.writerow([f"{self.test_date} {self.start_time}", self.verified_examiner, student_name, age, self.verified_permit_expiry, self.score, status, flat_history_summary])
            
        self.root.quit()

if __name__ == "__main__":
    window = tk.Tk()
    app = DOLTestApp(window)
    window.mainloop()