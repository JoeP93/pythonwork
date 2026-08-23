import streamlit as st
import csv
import os
from datetime import datetime

# 1. Official WA DOL Rubric Database Configuration
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

st.set_page_config(page_title="WA DOL Drive Test Evaluator", page_icon="🚗", layout="centered")

st.title("🚗 WA DOL Driving Test Evaluator")
st.markdown("### Enterprise Compliance Platform v1.5")
st.write("---")

# Initialize Session States to preserve data across page refreshes
if 'score' not in st.session_state: st.session_state.score = 100
if 'category_losses' not in st.session_state: st.session_state.category_losses = {name: 0 for name in RUBRIC}
if 'severity_history' not in st.session_state: st.session_state.severity_history = {name: {"minor": False, "major": False} for name in RUBRIC}
if 'infraction_history' not in st.session_state: st.session_state.infraction_history = []
if 'dangerous_action' not in st.session_state: st.session_state.dangerous_action = False
if 'da_reason' not in st.session_state: st.session_state.da_reason = ""
if 'verified_age' not in st.session_state: st.session_state.verified_age = None
if 'test_started' not in st.session_state:
    st.session_state.test_started = datetime.now().strftime("%I:%M %p")

# --- APPLICANT PROFILE SETUP ---
st.subheader("📋 1. Applicant Profile Setup")
student_name = st.text_input("Applicant Full Name:")
dob_input = st.text_input("Date of Birth (MM/DD/YYYY):", placeholder="e.g. 10/24/1998")

if st.button("Verify Eligibility Gate", type="primary"):
    if not student_name or not dob_input:
        st.error("Please provide both Name and Date of Birth to proceed.")
    else:
        try:
            current_moment = datetime.now()
            dob_parsed = datetime.strptime(dob_input.strip(), "%m/%d/%Y")
            age = current_moment.year - dob_parsed.year - ((current_moment.month, current_moment.day) < (dob_parsed.month, dob_parsed.day))
            
            if age < 15:
                st.error(f"❌ REGULATORY REJECTION: Applicant is only {age} years old. Testing is strictly blocked below 15 years of age.")
                st.session_state.verified_age = None
            else:
                st.success(f"✅ Access Granted: Applicant age verified at {age} years old. Evaluation panel unlocked.")
                st.session_state.verified_age = age
        except ValueError:
            st.error("❌ Format Error: Please enter birthdate using the layout pattern MM/DD/YYYY.")

# --- ROAD EVALUATION WORKSPACE ---
if st.session_state.verified_age is not None:
    st.write("---")
    st.subheader("🎛️ 2. Road Evaluation Workspace")
    
    # Visual Progress Bar Readout Dynamic Component
    display_score = 0 if st.session_state.dangerous_action else st.session_state.score
    if display_score >= 80:
        st.success(f"### CURRENT SCORE: {display_score} / 100")
    else:
        st.error(f"### CURRENT SCORE: {display_score} / 100 (FAIL BOUNDARY)")
        
    if st.session_state.dangerous_action:
        st.warning(f"⚠️ TEST TERMINATED: Dangerous Action Active ({st.session_state.da_reason})")

    # Entry Choice Selector Menu Box
    selected_category = st.selectbox("Select Evaluation Criteria Field Category:", list(RUBRIC.keys()))
    
    # Read state metrics
    current_loss = st.session_state.category_losses[selected_category]
    max_cap = RUBRIC[selected_category]["cap"]
    st.caption(f"Current Category Deficit for {selected_category}: -{current_loss} / -{max_cap} max")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Log Minor Error", use_container_width=True):
            if not st.session_state.dangerous_action:
                rules = RUBRIC[selected_category]
                if current_loss >= max_cap:
                    st.toast(f"'{selected_category}' has hit its point ceiling!")
                else:
                    if st.session_state.severity_history[selected_category]["minor"]:
                        st.toast("Duplicate infraction. 0 points deducted.")
                    else:
                        penalty = rules["minor"]
                        deduction = max_cap - current_loss if current_loss + penalty > max_cap else penalty
                        st.session_state.severity_history[selected_category]["minor"] = True
                        st.session_state.category_losses[selected_category] += deduction
                        st.session_state.score = max(0, self_score := st.session_state.score - deduction)
                        st.session_state.infraction_history.append(f"• {selected_category} (MINOR): -{deduction} pts")
                        st.rerun()

    with col2:
        if st.button("Log Major Error", use_container_width=True):
            if not st.session_state.dangerous_action:
                rules = RUBRIC[selected_category]
                if current_loss >= max_cap:
                    st.toast(f"'{selected_category}' has hit its point ceiling!")
                else:
                    if st.session_state.severity_history[selected_category]["major"]:
                        st.toast("Duplicate infraction. 0 points deducted.")
                    else:
                        penalty = rules["major"]
                        deduction = max_cap - current_loss if current_loss + penalty > max_cap else penalty
                        st.session_state.severity_history[selected_category]["major"] = True
                        st.session_state.category_losses[selected_category] += deduction
                        st.session_state.score = max(0, st.session_state.score - deduction)
                        st.session_state.infraction_history.append(f"• {selected_category} (MAJOR): -{deduction} pts")
                        st.rerun()

    with col3:
        da_input_reason = st.text_input("Danger Reason:", placeholder="e.g. Struck Curb", key="da_box")
        if st.button("Dangerous Action", use_container_width=True, type="secondary"):
            if da_input_reason:
                st.session_state.dangerous_action = True
                st.session_state.da_reason = da_input_reason
                st.session_state.infraction_history.append(f"❌ DANGEROUS ACTION in {selected_category}: {da_input_reason}")
                st.rerun()
            else:
                st.toast("Please specify a reason into the input field text box first!")

    # Audit Logs Tracking Monitor Display
    st.write("#### Live Exam History Audit Feed Log:")
    if not st.session_state.infraction_history:
        st.info("Clean driving sheet logged. Ideal tracking performance.")
    else:
        for item in st.session_state.infraction_history:
            st.text(item)

    # --- TEST FINALIZATION ---
    st.write("---")
    if st.button("FINALIZE ROAD EXAM & ARCHIVE RECORDS", type="primary", use_container_width=True):
        end_time_stamp = datetime.now().strftime("%I:%M %p")
        test_date_stamp = datetime.now().strftime("%m/%d/%Y")
        
        final_score = 0 if st.session_state.dangerous_action else st.session_state.score
        pass_fail_status = "FAILED" if st.session_state.dangerous_action or final_score < 80 else "PASSED"
        outcome_desc = "PASSED OFFICIAL SKILLS EXAM RUN" if pass_fail_status == "PASSED" else "FAILED due to inadequate compliance tracking metrics."
        
        st.subheader("📊 Final Examination Form Composed")
        st.code(
            f"Candidate Name: {student_name} (Age: {st.session_state.verified_age})\n"
            f"Testing Window: {st.session_state.test_started} to {end_time_stamp}\n"
            f"Final Tabulated Score: {final_score} / 100\n"
            f"Status Evaluation: {pass_fail_status}\n"
            f"Summary: {outcome_desc}"
        )
        
        if pass_fail_status == "PASSED":
            if st.session_state.verified_age < 18:
                st.info("💡 NEXT STEPS (MINOR IDL):\n1. Hold permit 6 full consecutive months.\n2. Certify 50 hours of driver log time (10 at night).\n3. Process licensing profile processing fees online via License eXpress.")
            else:
                st.info("💡 NEXT STEPS (ADULT LICENSE):\n1. Exam data updates directly to the WA DOL systems network database.\n2. Print temporary card via License eXpress immediately.\n3. Photo card arrives in post mail inside 7-10 business days.")
        else:
            st.error("💡 RETEST PROTOCOLS:\n• Schedule a targeted driver performance review training drive block before re-booking testing.")

        # Save to spreadsheet ledger database file
        csv_file_name = "driving_school_records.csv"
        file_present = os.path.isfile(csv_file_name)
        flat_log = " | ".join(st.session_state.infraction_history) if st.session_state.infraction_history else "Clean Sheet"
        
        with open(csv_file_name, mode="a", newline="") as active_file:
            data_writer = csv.writer(active_file)
            if not file_present:
                # 1. Writes the header columns if the Excel spreadsheet is brand new
                data_writer.writerow(["Timestamp Header", "Applicant Full Name", "Age Demographics", "Final Score Metrics", "Pass/Fail Status", "Detailed Performance Breakdown", "Raw Audit Strings Log"])
            
            # 2. Writes the actual student data row under those columns
            data_writer.writerow([f"{test_date_stamp} {st.session_state.test_started}", student_name, f"Age: {st.session_state.verified_age}", final_score, pass_fail_status, outcome_desc, flat_log])
            
        # 3. Prints the green success banner inside your web browser
        st.success(f"Complete test ledger records appended line to file: '{csv_file_name}'")