import tkinter as tk
from tkinter import messagebox, ttk
import random
import os
from datetime import datetime

# 1. Official Academy DLE-520 IPDE Commentary Driving Database (27 Terms)
COMMENTARY_DATA = [
    # --- IDENTIFY CATEGORY ---
    {
        "category": "Identify", "term": "Trap/Closed Zone",
        "definition": "Slow movers, brake lights, red lights, stop signs, construction, etc.",
        "scenario": "Up ahead you see brake lights lighting up in a line, or a construction orange sign. What are you calling out?"
    },
    {
        "category": "Identify", "term": "Intersections",
        "definition": "Identify type (2-way, 4-way) and right of way rule (who stops/goes first).",
        "scenario": "You are approaching cross-traffic. You must call out if it is a 2-way or 4-way control and who goes first. This is identifying..."
    },
    {
        "category": "Identify", "term": "Intruder/Thief",
        "definition": "Any vehicle or person who is an immediate threat or steals space (within 3 car lengths).",
        "scenario": "A car suddenly cuts directly in front of you into your lane, less than two car lengths away. They are an..."
    },
    {
        "category": "Identify", "term": "Safety Stop",
        "definition": "After a complete stop, when vision is limited, slowly move forward to make sure it's clear.",
        "scenario": "You stopped completely at a stop sign, but a massive bush blocks your view of cross-traffic. You edge forward slowly. This is a..."
    },
    {
        "category": "Identify", "term": "Limited Sight",
        "definition": "An obstruction in your line of sight (15 seconds ahead).",
        "scenario": "A massive delivery truck blocks your ability to view the road geometry 15 seconds ahead. You call out..."
    },
    {
        "category": "Identify", "term": "Slug",
        "definition": "Drivers who are generally in no hurry (buses, commercial trucks, oversized loads).",
        "scenario": "You are sitting behind a slow-moving transit bus or a massive wide-load commercial semi-truck. This vehicle is a..."
    },
    {
        "category": "Identify", "term": "Distracted",
        "definition": "Semi-aware of surroundings, on cell phone, texting, eating, radio tuning, etc.",
        "scenario": "You glance at the driver next to you and see them looking down typing a text message on their phone. They are..."
    },
    {
        "category": "Identify", "term": "Speed Check",
        "definition": "Every time you see a speed sign, call out the number followed by how fast you are going.",
        "scenario": "You pass a white sign that says 'Speed Limit 35'. You look at your speedometer and say '35/32'. You just performed a..."
    },
    {
        "category": "Identify", "term": "Tag",
        "definition": "Potential hazard; any roadway user capable of causing a threat to you or others.",
        "scenario": "A jogger running along the shoulder or a skateboarder approaching a curb is identified as a..."
    },
    # --- PREDICT CATEGORY ---
    {
        "category": "Predict", "term": "Check One",
        "definition": "Check the rearview mirror every 5-8 seconds, before braking, after turning.",
        "scenario": "You completed a left turn and instantly glance up at your rearview mirror to track traffic behind you. What term is this?"
    },
    {
        "category": "Predict", "term": "Sneaky Right",
        "definition": "A vehicle that makes or intends to make a right turn into your path of travel.",
        "scenario": "An oncoming vehicle is slowing down to quickly turn right across your intended path. You predict a..."
    },
    {
        "category": "Predict", "term": "On-coming Left (BLT)",
        "definition": "A vehicle that makes or intends to make a left turn in front of you.",
        "scenario": "A car waiting in the oncoming turn lane turns directly across your grill. You just encountered a..."
    },
    {
        "category": "Predict", "term": "Fresh/Stale Green Light",
        "definition": "A light that just turned green or one that may change soon.",
        "scenario": "You approach an intersection and realize the traffic signal has been green for a long block. You predict a..."
    },
    {
        "category": "Predict", "term": "Tailgater/Charger",
        "definition": "A driver who follows another vehicle too closely.",
        "scenario": "You look in your mirror and see a sports car practically glued to your rear bumper. You are tracking a..."
    },
    {
        "category": "Predict", "term": "Pedestrian/Foot/Toddler/Dog/Bike",
        "definition": "Anyone unpredictable crossing your path.",
        "scenario": "A little kid playing with a basketball near the edge of a driveway represents what group of commentary hazards?"
    },
    {
        "category": "Predict", "term": "Pacer",
        "definition": "Semi-aware driver in a pack of cars, vulnerable to the actions of others.",
        "scenario": "A vehicle traveling at the exact same speed inside a tight cluster of gridlocked highway cars is called a..."
    },
    # --- DECIDE CATEGORY ---
    {
        "category": "Decide", "term": "Safe To Go",
        "definition": "Before entering an intersection, SCAN to the left, center, and right.",
        "scenario": "Your light snaps green. Before your foot touches the accelerator, you check Left, Center, Right to make sure it is..."
    },
    {
        "category": "Decide", "term": "Go Point/Point of No Return",
        "definition": "Point beyond which you can no longer stop safely without entering the intersection.",
        "scenario": "You are 15 feet from the intersection line going 35 MPH when the light turns yellow. You must decide to clear it via your..."
    },
    {
        "category": "Decide", "term": "Back Pressure",
        "definition": "Vehicles to the rear increasing intensity and decreasing space cushion.",
        "scenario": "An aggressive group of commuters rushes up fast from behind you, shrinking your rear safety buffer. This is..."
    },
    {
        "category": "Decide", "term": "Best Path",
        "definition": "The lane with the best visibility and traffic flow and most escape options.",
        "scenario": "You choose the middle lane on a 3-lane roadway because it avoids parallel parkers and turning traffic. You chose the..."
    },
    # --- EXECUTE CATEGORY ---
    {
        "category": "Execute", "term": "Signal 1-2-3",
        "definition": "Signal, check rear-view, side-view mirrors, and blind spot for lane change.",
        "scenario": "Before shifting left, you blinker, check your rear mirror, side mirror, and glance over your left shoulder. You ran a..."
    },
    {
        "category": "Execute", "term": "Cover Brake",
        "definition": "As potential hazards appear, take your foot off the accelerator and hover your foot over the brake to reduce reaction time.",
        "scenario": "You notice brake lights up ahead, so you lift off the gas and float your right foot straight over the pedal. You..."
    },
    {
        "category": "Execute", "term": "Closest Lane",
        "definition": "When turning onto a roadway with multiple lanes, take the closest lane. (Assume a car turning in front of you may cross over).",
        "scenario": "You execute a sharp right turn at a junction directly into lane 1, rather than swinging wide into lane 2. You used..."
    },
    {
        "category": "Execute", "term": "Body Shift",
        "definition": "Turn your body 180 degrees to the rear while backing. Don't rely on mirrors!",
        "scenario": "You shift into Reverse, physically twist your torso around to look straight out the back window. You executed a..."
    },
    {
        "category": "Execute", "term": "Up 2 Down 2",
        "definition": "Technique to increase space and break rapport with others. Increase speed by 2 MPH, remain briefly, then decrease by 2 MPH to clear the zone.",
        "scenario": "You are stuck riding right in another vehicle's blind spot. You click your speed up slightly, then settle back to clear out. This is..."
    },
    {
        "category": "Execute", "term": "Space Cushion",
        "definition": "Maintaining a pocket of space around one's vehicle.",
        "scenario": "You ease off the gas to create a 4-second safety buffer of open air in front of your bumper. You are establishing a..."
    },
    {
        "category": "Execute", "term": "Pocket Surfing",
        "definition": "Driving in between packs of cars, maintains healthy space cushion.",
        "scenario": "You cruise calmly in the large, open gap of empty asphalt positioned safely between two massive groups of highway traffic. This is..."
    }
]
class CommentaryGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Defensive Driving Academy - Commentary Mastery v1.0")
        self.root.geometry("550x700")
        
        # Sleek Premium Dark Slate & Royal Blue Theme Palette
        self.bg_dark = "#1a1e24"
        self.bg_panel = "#242932"
        self.fg_white = "#abb2bf"
        self.fg_bright = "#ffffff"
        self.accent_blue = "#3b82f6"
        self.accent_green = "#10b981"
        
        self.root.configure(bg=self.bg_dark)
        
        # Student State Tracking Variables
        self.student_name = ""
        self.current_flashcard_idx = 0
        self.quiz_questions = []
        self.current_quiz_idx = 0
        self.score = 0
        self.timer_seconds = 15
        self.timer_job = None
        
        self.build_login_screen()

    def build_login_screen(self):
        self.clear_window()
        
        # Header Banner
        header = tk.Frame(self.root, bg=self.accent_blue, height=70)
        header.pack(fill="x", side="top")
        tk.Label(header, text="COMMENTARY DRIVING HOMEWORK PORTAL", font=("Segoe UI", 12, "bold"), fg=self.fg_bright, bg=self.accent_blue).pack(pady=22)
        
        # Card Body Panel
        login_frame = tk.LabelFrame(self.root, text=" Student Homework Sign-In ", font=("Segoe UI", 10, "bold"), bg=self.bg_panel, fg=self.accent_blue, padx=20, pady=20, bd=1, relief="solid")
        login_frame.pack(padx=30, pady=100, fill="x")
        
        tk.Label(login_frame, text="Enter Your Full Name:", bg=self.bg_panel, fg=self.fg_white, font=("Segoe UI", 11)).pack(anchor="w", pady=5)
        self.name_entry = tk.Entry(login_frame, font=("Segoe UI", 11), bg=self.bg_dark, fg=self.fg_bright, insertbackground="white", bd=1, relief="solid")
        self.name_entry.pack(fill="x", pady=10)
        self.name_entry.focus()
        
        start_btn = tk.Button(login_frame, text="ENTER HOMEWORK PORTAL", bg=self.accent_blue, fg=self.fg_bright, font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", pady=10, command=self.process_login)
        start_btn.pack(fill="x", pady=15)

    def process_login(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Sign-In Error", "Please provide your full name to ensure your homework assignment is recorded correctly.")
            return
        self.student_name = name
        self.build_dashboard_screen()

    def build_dashboard_screen(self):
        self.clear_window()
        
        # Welcome Widget Banner Label
        welcome_frame = tk.Frame(self.root, bg=self.bg_panel, pady=15, bd=1, relief="solid")
        welcome_frame.pack(fill="x", padx=20, pady=20)
        tk.Label(welcome_frame, text=f"Student Profile: {self.student_name}", font=("Segoe UI", 11, "bold"), fg=self.accent_blue, bg=self.bg_panel).pack()
        
        menu_frame = tk.LabelFrame(self.root, text=" Choose Module Assignment ", font=("Segoe UI", 11, "bold"), bg=self.bg_panel, fg=self.accent_blue, padx=20, pady=25, bd=1, relief="solid")
        menu_frame.pack(padx=20, pady=40, fill="both", expand=True)
        
        tk.Label(menu_frame, text="Module 1: Vocabulary Training", font=("Segoe UI", 10, "bold"), bg=self.bg_panel, fg=self.fg_white).pack(anchor="w", pady=5)
        flash_btn = tk.Button(menu_frame, text="Open Flashcard Study Mode", bg="#4b5563", fg=self.fg_bright, font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", pady=8, command=self.start_flashcard_mode)
        flash_btn.pack(fill="x", pady=5)
        
        tk.Label(menu_frame, text="Module 2: High-Score Speed Exam", font=("Segoe UI", 10, "bold"), bg=self.bg_panel, fg=self.fg_white).pack(anchor="w", pady=15)
        quiz_btn = tk.Button(menu_frame, text="START QUIZ CHALLENGE", bg=self.accent_green, fg=self.fg_bright, font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", pady=10, command=self.start_quiz_mode)
        quiz_btn.pack(fill="x", pady=5)

    def start_flashcard_mode(self):
        self.current_flashcard_idx = 0
        self.build_flashcard_screen()

    def build_flashcard_screen(self):
        self.clear_window()
        item = COMMENTARY_DATA[self.current_flashcard_idx]
        
        # Module Banner header tracker
        header = tk.Frame(self.root, bg="#4b5563", height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"FLASHCARD STUDY TRACKER ({self.current_flashcard_idx + 1} / {len(COMMENTARY_DATA)})", font=("Segoe UI", 10, "bold"), fg=self.fg_bright, bg="#4b5563").pack(pady=12)
        
        # Massive Flip-Card Component Interface Panel Block Box
        self.card_flipped = False
        self.card_panel = tk.Button(self.root, bg=self.bg_panel, activebackground=self.bg_panel, bd=1, relief="solid", cursor="hand2", command=lambda: self.flip_flashcard(item))
        self.card_panel.pack(padx=30, pady=50, fill="both", expand=True)
        
        self.card_text = tk.Label(self.card_panel, text=item["term"], font=("Segoe UI", 18, "bold"), fg=self.accent_blue, bg=self.bg_panel, wraplength=400)
        self.card_text.pack(expand=True, padx=20, pady=20)
        
        hint_label = tk.Label(self.card_panel, text="(Click Card to Flip & Reveal Definition)", font=("Segoe UI", 9, "italic"), fg=self.fg_white, bg=self.bg_panel)
        hint_label.pack(side="bottom", pady=15)
        
        # Navigation Bar Layout Row Panel Dock Elements
        nav_frame = tk.Frame(self.root, bg=self.bg_dark)
        nav_frame.pack(fill="x", side="bottom", pady=30, padx=30)
        
        prev_btn = tk.Button(nav_frame, text="◀ Previous", font=("Segoe UI", 10, "bold"), bg="#374151", fg=self.fg_bright, bd=0, cursor="hand2", width=12, command=self.prev_flashcard)
        prev_btn.pack(side="left")
        
        home_btn = tk.Button(nav_frame, text="Main Menu", font=("Segoe UI", 10, "bold"), bg=self.accent_blue, fg=self.fg_bright, bd=0, cursor="hand2", width=12, command=self.build_dashboard_screen)
        home_btn.pack(side="left", expand=True)
        
        next_btn = tk.Button(nav_frame, text="Next ▶", font=("Segoe UI", 10, "bold"), bg="#374151", fg=self.fg_bright, bd=0, cursor="hand2", width=12, command=self.next_flashcard)
        next_btn.pack(side="right")

    def flip_flashcard(self, item):
        if not self.card_flipped:
            self.card_text.config(text=item["definition"], font=("Segoe UI", 12, "normal"), fg=self.fg_bright)
            self.card_flipped = True
        else:
            self.card_text.config(text=item["term"], font=("Segoe UI", 18, "bold"), fg=self.accent_blue)
            self.card_flipped = False

    def prev_flashcard(self):
        if self.current_flashcard_idx > 0:
            self.current_flashcard_idx -= 1
            self.build_flashcard_screen()

    def next_flashcard(self):
        if self.current_flashcard_idx < len(COMMENTARY_DATA) - 1:
            self.current_flashcard_idx += 1
            self.build_flashcard_screen()
        else:
            messagebox.showinfo("Study Completed", "You have finished reviewing all the core vocabulary terms! You are completely ready for the High-Score Speed Exam.")
            self.build_dashboard_screen()

    def start_quiz_mode(self):
        self.score = 0
        self.current_quiz_idx = 0
        # Clone data database structures lists arrays entries and randomize layout
        self.quiz_questions = list(COMMENTARY_DATA)
        random.shuffle(self.quiz_questions)
        self.build_quiz_screen()

    def build_quiz_screen(self):
        if self.current_quiz_idx >= len(self.quiz_questions):
            self.finalize_homework_score()
            return
            
        self.clear_window()
        q = self.quiz_questions[self.current_quiz_idx]
        
        # Quiz Stats Header
        header = tk.Frame(self.root, bg=self.accent_green, height=45)
        header.pack(fill="x")
        tk.Label(header, text=f"SPEED EXAM: Q {self.current_quiz_idx + 1} / {len(self.quiz_questions)}  |  Score: {self.score}", font=("Segoe UI", 10, "bold"), fg=self.fg_bright, bg=self.accent_green).pack(side="left", padx=15, pady=10)
        
        self.timer_label = tk.Label(header, text="Time Remaining: 15s", font=("Segoe UI", 10, "bold"), fg=self.fg_bright, bg=self.accent_green)
        self.timer_label.pack(side="right", padx=15, pady=10)
        
        # Real-World Scenario Question Container Display Panel Box Widget
        q_frame = tk.Frame(self.root, bg=self.bg_panel, bd=1, relief="solid", padx=20, pady=25)
        q_frame.pack(padx=20, pady=30, fill="x")
        tk.Label(q_frame, text=q["scenario"], font=("Segoe UI", 11, "bold"), fg=self.fg_bright, bg=self.bg_panel, wraplength=460, justify="center").pack()
        
        # Multiple Choice Options Compilation Generation Engine (Grab correct answer + 2 distractors)
        correct_answer = q["term"]
        pool = [d["term"] for d in COMMENTARY_DATA if d["term"] != correct_answer]
        wrong_choices = random.sample(pool, 2)
        choices = wrong_choices + [correct_answer]
        random.shuffle(choices)
        
        # Option Button Render Dock Stack Grid
        for choice in choices:
            btn = tk.Button(self.root, text=choice, font=("Segoe UI", 11, "bold"), bg=self.bg_panel, fg=self.fg_white, bd=1, relief="solid", activebackground=self.accent_blue, activeforeground="white", cursor="hand2", pady=10)
            btn.config(command=lambda choice_text=choice: self.submit_quiz_answer(choice_text, correct_answer))
            btn.pack(fill="x", padx=30, pady=6)
            
        # Initialize Count Engine Time Parameters
        self.timer_seconds = 15
        self.run_quiz_countdown()

    def run_quiz_countdown(self):
        if self.timer_seconds > 0:
            self.timer_label.config(text=f"Time Remaining: {self.timer_seconds}s")
            if self.timer_seconds <= 5:
                self.timer_label.config(fg="red")
            self.timer_seconds -= 1
            self.timer_job = self.root.after(1000, self.run_quiz_countdown)
        else:
            self.cancel_timer_callback()
            messagebox.showwarning("TIMEOUT", "Clock ran out! That counts as a missed commentary identification.")
            self.current_quiz_idx += 1
            self.build_quiz_screen()

    def cancel_timer_callback(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

    def submit_quiz_answer(self, chosen, correct):
        self.cancel_timer_callback()
        if chosen == correct:
            self.score += 15 # Award points per fast identification
            messagebox.showinfo("CORRECT ✓", f"Excellent scanning tracking response! That is a verified '{correct}' maneuver.")
        else:
            messagebox.showerror("INCORRECT ❌", f"Incorrect driving response. The correct term was '{correct}'.")
            
        self.current_quiz_idx += 1
        self.build_quiz_screen()

    def finalize_homework_score(self):
        self.cancel_timer_callback()
        max_possible_points = len(self.quiz_questions) * 15
        final_percentage = int((self.score / max_possible_points) * 100)
        
        status = "PASSED ASSIGNMENT" if final_percentage >= 70 else "FAILED (Requires Review)"
        
        summary_msg = (
            f"Official Assignment Results sheet for: {self.student_name}\n\n"
            f"Final Tabulated Score: {final_percentage}% ({self.score} pts)\n"
            f"Status Evaluation: {status}\n\n"
            "Results have been hardcoded locked to the verification dashboard database log tracker sheet."
        )
        messagebox.showinfo("Homework Performance Generated", summary_msg)
        
        # Local Database File Storage Tracker Anchor Loop Module Filegen
        log_file = "commentary_homework_records.txt"
        timestamp = datetime.now().strftime("%m/%d/%Y %I:%M %p")
        with open(log_file, mode="a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] Student: {self.student_name.lpad if hasattr(str, 'lpad') else self.student_name} | Score: {final_percentage}% | Status: {status}\n")
            
        self.build_dashboard_screen()

    def clear_window(self):
        self.cancel_timer_callback()
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    app = CommentaryGameApp(window)
    window.mainloop()