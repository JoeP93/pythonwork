import csv
import os
from datetime import datetime, timedelta

def run_enterprise_dol_evaluator():
    print("==================================================")
    print(" WASHINGTON STATE DOL DRIVE TEST (ENTERPRISE SYSTEM)")
    print("==================================================")
    
    STARTING_SCORE = 100
    PASSING_BAR = 80
    
    rubric = {
        "1": {"name": "Backing", "minor": 2, "major": 4, "cap": 4},
        "2": {"name": "Parallel Parking", "minor": 2, "major": 4, "cap": 4},
        "3": {"name": "Park and Start on Hill", "minor": 2, "major": 4, "cap": 4},
        "4": {"name": "Starting", "minor": 2, "major": 4, "cap": 4},
        "5": {"name": "Lane Travel", "minor": 2, "major": 4, "cap": 4},
        "6": {"name": "Traffic Control Devices", "minor": 2, "major": 4, "cap": 4},
        "7": {"name": "Stop Signs / Flashing Lights", "minor": 2, "major": 4, "cap": 4},
        "8": {"name": "Traffic Signal Lights", "minor": 2, "major": 4, "cap": 4},
        "9": {"name": "Mechanical Operation", "minor": 1, "major": 2, "cap": 2}, 
        "10": {"name": "Left Turns", "minor": 3, "major": 6, "cap": 6},           
        "11": {"name": "Right Turns", "minor": 3, "major": 6, "cap": 6},         
        "12": {"name": "Uncontrolled Intersections", "minor": 2, "major": 4, "cap": 4},
        "13": {"name": "Following", "minor": 2, "major": 4, "cap": 4},
        "14": {"name": "Passing", "minor": 2, "major": 4, "cap": 4},
        "15": {"name": "Right-of-Way", "minor": 2, "major": 4, "cap": 4},
        "16": {"name": "General Driving Performance", "minor": 2, "major": 4, "cap": 4}
    }
    
    category_totals = {key: 0 for key in rubric}
    severity_history = {key: {"minor": False, "major": False} for key in rubric}
    total_deductions = 0
    dangerous_action = False
    da_reason = ""
    infraction_history = []
    
    # Core Data Inputs
    student = input("Enter Applicant Full Name: ").strip()
    
    current_moment = datetime.now()
    test_date = current_moment.strftime("%m/%d/%Y")
    start_time = current_moment.strftime("%I:%M %p")
    
    # 1. Age Verification and Strict Check Validation Logic
    while True:
        dob_str = input("Enter Applicant Date of Birth (MM/DD/YYYY): ").strip()
        try:
            dob_date = datetime.strptime(dob_str, "%m/%d/%Y")
            
            # Use exact calendar day math to avoid leap year drift errors
            age = current_moment.year - dob_date.year - ((current_moment.month, current_moment.day) < (dob_date.month, dob_date.day))
            
            if age < 15:
                print(f"\n[REGULATORY ERROR] Applicant is {age} years old.")
                print("Under Washington state law, an individual must be at least 15 years old to take a skills test.")
                print("Testing blocked. Application terminating.\n")
                return # Exit the function entirely
            else:
                break # Age is valid, continue with test setup
                
        except ValueError:
            print("[INPUT ERROR] Invalid date format. Please look at the guide and use MM/DD/YYYY.")
    
    print(f"-> Applicant Age Verified: {age}")
    print(f"-> Test Date Auto-Logged: {test_date}")
    print(f"-> Test Start Time Auto-Logged: {start_time}")
    
    print("\n--- SECTIONS AVAILABLE TO EVALUATE ---")
    for key, value in rubric.items():
        print(f"[{key}] {value['name']} (Minor: -{value['minor']}, Major: -{value['major']}, Max Cap: -{value['cap']} pts)")
        
    print("\nType 'done' when the road test route is finished.")
    
    # Main Exam Processing Loop
    while True:
        choice = input("\nSelect Section Number (or 'done'): ").strip()
        if choice.lower() == 'done':
            break
            
        if choice in rubric:
            section = rubric[choice]
            current_category_loss = category_totals[choice]
            max_allowed_cap = section['cap']
            
            if current_category_loss >= max_allowed_cap:
                print(f"-> Note: Category '{section['name']}' has already reached its maximum deduction.")
            
            severity = input("Select severity (1=Minor, 2=Major, 3=Dangerous Action): ").strip()
            
            if severity in ("1", "2"):
                severity_key = "minor" if severity == "1" else "major"
                error_type_label = "Minor" if severity == "1" else "Major"
                
                if severity_history[choice][severity_key]:
                    print(f"-> [0 PTS DEDUCTED] A {error_type_label} error has already been recorded for '{section['name']}'.")
                    raw_penalty = 0
                    duplicate_note = " (Duplicate offense - no extra points lost)"
                else:
                    raw_penalty = section[severity_key]
                    duplicate_note = ""
                
                if current_category_loss + raw_penalty > max_allowed_cap:
                    actual_deduction = max_allowed_cap - current_category_loss
                    capped_note = " (Capped at category limit)"
                else:
                    actual_deduction = raw_penalty
                    capped_note = ""
                
                severity_history[choice][severity_key] = True
                
                if actual_deduction > 0 or duplicate_note != "":
                    category_totals[choice] += actual_deduction
                    total_deductions += actual_deduction
                    desc = input(f"Notes for {error_type_label} error: ")
                    infraction_history.append(
                        f"{section['name']} ({error_type_label}): -{actual_deduction} pts{duplicate_note}{capped_note} | {desc}"
                    )
                    print(f"Applied deduction. Running Score: {STARTING_SCORE - total_deductions}")
                
            elif severity == "3":
                dangerous_action = True
                da_reason = input("Describe Dangerous Action: ")
                infraction_history.append(f"DANGEROUS ACTION in {section['name']}: {da_reason}")
                break

    end_time = input("\nEnter Test End Time (e.g., 02:45 PM) [Or Enter for current time]: ").strip()
    if not end_time:
        end_time = datetime.now().strftime("%I:%M %p")

    # Pass/Fail Validation Architecture
    if dangerous_action:
        final_score = 0  
        outcome = "FAILED"
        outcome_desc = f"FAILED due to a Dangerous Action: {da_reason}"
    else:
        final_score = STARTING_SCORE - total_deductions
        if final_score < 0: final_score = 0
        outcome = "PASSED" if final_score >= PASSING_BAR else "FAILED"
        outcome_desc = "PASSED OFFICIAL SKILLS TEST" if final_score >= PASSING_BAR else f"FAILED due to insufficient score (Minimum is {PASSING_BAR})"
        
    # --- PRINT EXTENDED RESULTS SHEET ---
    print("\n" + "="*60)
    print("             WASHINGTON STATE SKILLS TEST RESULT")
    print("="*60)
    print(f"APPLICANT NAME:  {student} (Age: {age})")
    print(f"TEST WINDOW:     {test_date} | {start_time} TO {end_time}")
    print("-"*60)
    print(f"FINAL SCORE:     {final_score} / 100")
    print(f"STATUS OUTCOME:  {outcome_desc}")
    print("==================================================")
    
    # --- DYNAMIC ADVISORY SYSTEM BASED ON WA DOL REGS ---
    if outcome == "PASSED":
        print("\n>>> NEXT STEPS FOR APPLICANT:")
        if age < 18:
            print(" 1. HOLDING REQUIREMENT: Ensure you have held your WA Instructional Permit\n    for at least 6 consecutive months before finalizing processing.")
            print(" 2. PRACTICE LOGS: Confirm completion of 50 hours of certified practice\n    (including 10 hours of dedicated night driving).")
            print(" 3. ISSUANCE: Your score will be uploaded directly to the WA DOL system.\n    Head online to secure your Intermediate Driver License (IDL).")
            print(" 4. RESTRICTIONS: Remember: No passengers under 20 (except immediate family)\n    and no driving between 1:00 AM and 5:00 AM for the first 6 months.")
        else:
            print(" 1. ISSUANCE: Your score will be transmitted directly to the WA DOL data system.")
            print(" 2. PROCESSING: You can log into your License eXpress account online to pay\n    your licensing fees and print your temporary paper license immediately.")
            print(" 3. IDENTIFICATION: Your permanent plastic card will arrive by mail within 7-10 days.")
    else:
        print("\n>>> RETEST PROTOCOLS:")
        print(" • Schedule a remedial training drive block with your examiner.")
        print(" • Per WA DOL guidelines, skills test re-testing windows are subject to provider availability.")
    print("="*60)

    # --- AUTOMATED DATABASE STORAGE (CSV EXPORT) ---
    csv_file = "driving_school_records.csv"
    file_exists = os.path.isfile(csv_file)
    
    flat_log = " | ".join(infraction_history) if infraction_history else "Clean Sheet"
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Student Name", "Age", "Score", "Status", "Details", "Error Log Summary"])
        writer.writerow([f"{test_date} {start_time}", student, age, final_score, outcome, outcome_desc, flat_log])
        
    print(f"\n[SYSTEM ALERT] Complete records successfully appended to secure ledger: '{csv_file}'")

run_enterprise_dol_evaluator()