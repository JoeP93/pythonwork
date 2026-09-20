import streamlit as str
import random

# Ultimate CSS override to force dark text inside Streamlit inputs
str.markdown("""
    <style>
        /* Force dark text and a light gray background on all text inputs */
        input, .stTextInput input, [data-baseweb="input"] input {
            color: #1e222b !important;
            background-color: #f0f2f6 !important;
            -webkit-text-fill-color: #1e222b !important;
        }
        /* Ensure the input wrapper itself uses a dark font color */
        div[data-baseweb="input"] {
            color: #1e222b !important;
            background-color: #f0f2f6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Ensure page configuration is locked at the absolute top of the runtime execution layout
str.set_page_config(page_title="Commentary Mastery Portal", page_icon="🚗", layout="centered")

# Official Academy DLE-520 IPDE Commentary Driving Database (27 Terms)
COMMENTARY_DATA = [
    {"category": "Identify", "term": "Trap/Closed Zone", "definition": "Slow movers, brake lights, red lights, stop signs, construction, etc.", "scenario": "Up ahead you see brake lights lighting up in a line, or a construction orange sign. What are you calling out?"},
    {"category": "Identify", "term": "Intersections", "definition": "Identify type (2-way, 4-way) and right of way rule (who stops/goes first).", "scenario": "You are approaching cross-traffic. You must call out if it is a 2-way or 4-way control and who goes first. This is identifying..."},
    {"category": "Identify", "term": "Intruder/Thief", "definition": "Any vehicle or person who is an immediate threat or steals space (within 3 car lengths).", "scenario": "A car suddenly cuts directly in front of you into your lane, less than two car lengths away. They are an..."},
    {"category": "Identify", "term": "Safety Stop", "definition": "After a complete stop, when vision is limited, slowly move forward to make sure it's clear.", "scenario": "You stopped completely at a stop sign, but a massive bush blocks your view of cross-traffic. You edge forward slowly. This is a..."},
    {"category": "Identify", "term": "Limited Sight", "definition": "An obstruction in your line of sight (15 seconds ahead).", "scenario": "A massive delivery truck blocks your ability to view the road geometry 15 seconds ahead. You call out..."},
    {"category": "Identify", "term": "Slug", "definition": "Drivers who are generally in no hurry (buses, commercial trucks, oversized loads).", "scenario": "You are sitting behind a slow-moving transit bus or a massive wide-load commercial semi-truck. This vehicle is a..."},
    {"category": "Identify", "term": "Distracted", "definition": "Semi-aware of surroundings, on cell phone, texting, eating, radio tuning, etc.", "scenario": "You glance at the driver next to you and see them looking down typing a text message on their phone. They are..."},
    {"category": "Identify", "term": "Speed Check", "definition": "Every time you see a speed sign, call out the number followed by how fast you are going.", "scenario": "You pass a white sign that says 'Speed Limit 35'. You look at your speedometer and say '35/32'. You just performed a..."},
    {"category": "Identify", "term": "Tag", "definition": "Potential hazard; any roadway user capable of causing a threat to you or others.", "scenario": "A jogger running along the shoulder or a skateboarder approaching a curb is identified as a..."},
    {"category": "Predict", "term": "Check One", "definition": "Check the rearview mirror every 5-8 seconds, before braking, after turning.", "scenario": "You completed a left turn and instantly glance up at your rearview mirror to track traffic behind you. What term is this?"},
    {"category": "Predict", "term": "Sneaky Right", "definition": "A vehicle that makes or intends to make a right turn into your path of travel.", "scenario": "An oncoming vehicle is slowing down to quickly turn right across your intended path. You predict a..."},
    {"category": "Predict", "term": "On-coming Left (BLT)", "definition": "A vehicle that makes or intends to make a left turn in front of you.", "scenario": "A car waiting in the oncoming turn lane turns directly across your grill. You just encountered a..."},
    {"category": "Predict", "term": "Fresh/Stale Green Light", "definition": "A light that just turned green or one that may change soon.", "scenario": "You approach an intersection and realize the traffic signal has been green for a long block. You predict a..."},
    {"category": "Predict", "term": "Tailgater/Charger", "definition": "A driver who follows another vehicle too closely.", "scenario": "You look in your mirror and see a sports car practically glued to your rear bumper. You are tracking a..."},
    {"category": "Predict", "term": "Pedestrian/Foot/Toddler/Dog/Bike", "definition": "Anyone unpredictable crossing your path.", "scenario": "A little kid playing with a basketball near the edge of a driveway represents what group of commentary hazards?"},
    {"category": "Predict", "term": "Pacer", "definition": "Semi-aware driver in a pack of cars, vulnerable to the actions of others.", "scenario": "A vehicle traveling at the exact same speed inside a tight cluster of gridlocked highway cars is called a..."},
    {"category": "Decide", "term": "Safe To Go", "definition": "Before entering an intersection, SCAN to the left, center, and right.", "scenario": "Your light snaps green. Before your foot touches the accelerator, you check Left, Center, Right to make sure it is..."},
    {"category": "Decide", "term": "Go Point/Point of No Return", "definition": "Point beyond which you can no longer stop safely without entering the intersection.", "scenario": "You are 15 feet from the intersection line going 35 MPH when the light turns yellow. You must decide to clear it via your..."},
    {"category": "Decide", "term": "Back Pressure", "definition": "Vehicles to the rear increasing intensity and decreasing space cushion.", "scenario": "An aggressive group of commuters rushes up fast from behind you, shrinking your rear safety buffer. This is..."},
    {"category": "Decide", "term": "Best Path", "definition": "The lane with the best visibility and traffic flow and most escape options.", "scenario": "You choose the middle lane on a 3-lane roadway because it avoids parallel parkers and turning traffic. You chose the..."},
    {"category": "Execute", "term": "Signal 1-2-3", "definition": "Signal, check rear-view, side-view mirrors, and blind spot for lane change.", "scenario": "Before shifting left, you blinker, check your rear mirror, side mirror, and glance over your left shoulder. You ran a..."},
    {"category": "Execute", "term": "Cover Brake", "definition": "As potential hazards appear, take your foot off the accelerator and hover your foot over the brake to reduce reaction time.", "scenario": "You notice brake lights up ahead, so you lift off the gas and float your right foot straight over the pedal. You..."},
    {"category": "Execute", "term": "Closest Lane", "definition": "When turning onto a roadway with multiple lanes, take the closest lane. (Assume a car turning in front of you may cross over).", "scenario": "You execute a sharp right turn at a junction directly into lane 1, rather than swinging wide into lane 2. You used..."},
    {"category": "Execute", "term": "Body Shift", "definition": "Turn your body 180 degrees to the rear while backing. Don't rely on mirrors!", "scenario": "You shift into Reverse, physically twist your torso around to look straight out the back window. You executed a..."},
    {"category": "Execute", "term": "Up 2 Down 2", "definition": "Technique to increase space and break rapport with others. Increase speed by 2 MPH, remain briefly, then decrease by 2 MPH to clear the zone.", "scenario": "You are stuck riding right in another vehicle's blind spot. You click your speed up slightly, then settle back to clear out. This is..."},
    {"category": "Execute", "term": "Space Cushion", "definition": "Maintaining a pocket of space around one's vehicle.", "scenario": "You ease off the gas to create a 4-second safety buffer of open air in front of your bumper. You are establishing a..."},
    {"category": "Execute", "term": "Pocket Surfing", "definition": "Driving in between packs of cars, maintains healthy space cushion.", "scenario": "You cruise calmly in the large, open gap of empty asphalt positioned safely between two massive groups of highway traffic. This is..."}
]

str.title("🚗 Defensive Driving Commentary Vocabulary Homework")
str.caption("Official Student Homework Engine - Powered by IPDE Methodology")

str.sidebar.header("📋 Assignment Navigation")
student_name = str.sidebar.text_input("Enter Student Full Name:", value="").strip()
module = str.sidebar.radio("Select Training Module Assignment:", ["Flashcard Study Mode", "High-Score Quiz Challenge"])

if 'quiz_score' not in str.session_state: str.session_state.quiz_score = 0
if 'current_question_idx' not in str.session_state: str.session_state.current_question_idx = 0
if 'shuffled_questions' not in str.session_state:
    q_list = list(COMMENTARY_DATA)
    random.shuffle(q_list)
    str.session_state.shuffled_questions = q_list
if not student_name:
    str.warning("⚠️ Sign-In Required: Please type your full name in the sidebar menu panel to launch your homework assignment tracking metrics.")
else:
    if module == "Flashcard Study Mode":
        str.header("📚 Vocabulary Training Cards")
        str.write("Click any card below to reveal the official defensive driving definition rules.")
        
        categories = ["Identify", "Predict", "Decide", "Execute"]
        selected_cat = str.selectbox("Filter Terms by IPDE Category:", categories)
        
        for item in COMMENTARY_DATA:
            if item["category"] == selected_cat:
                with str.expander(f"🔍 {item['term']}"):
                    str.markdown(f"**Official Academy Definition:** {item['definition']}")
                    str.info(f"**Real-World Application Example:** {item['scenario']}")

    elif module == "High-Score Quiz Challenge":
        str.header("⚡ High-Score Speed Quiz Challenge")
        
        if str.session_state.current_question_idx >= len(str.session_state.shuffled_questions):
            max_points = len(str.session_state.shuffled_questions) * 10
            percentage = int((str.session_state.quiz_score / max_points) * 100)
            passed = percentage >= 70
            
            str.balloons() if passed else str.snow()
            if passed:
                str.success(f"🎉 Homework Session Finalized, {student_name}!")
            else:
                str.error(f"Review Required, {student_name}.")
            
            str.metric(label="Calculated Performance Grade", value=f"{percentage}%", delta=f"{str.session_state.quiz_score} Total Pts")
            str.info("ℹ️ Take a screenshot of this completed dashboard web screen link and bring it to your next in-car drive lesson session to verify your homework completion tokens.")
            
            if str.button("Restart Quiz Assignment Challenge"):
                str.session_state.quiz_score = 0
                str.session_state.current_question_idx = 0
                random.shuffle(str.session_state.shuffled_questions)
                str.rerun()
        else:
            q_idx = str.session_state.current_question_idx
            current_q = str.session_state.shuffled_questions[q_idx]
            
            str.subheader(f"Question {q_idx + 1} of {len(str.session_state.shuffled_questions)}")
            str.progress((q_idx) / len(str.session_state.shuffled_questions))
            
            str.info(current_q["scenario"])
            
            correct = current_q["term"]
            if 'current_options' not in str.session_state or str.session_state.get('last_q_idx') != q_idx:
                pool = [d["term"] for d in COMMENTARY_DATA if d["term"] != correct]
                wrong_choices = random.sample(pool, 2)
                choices = wrong_choices + [correct]
                random.shuffle(choices)
                str.session_state.current_options = choices
                str.session_state.last_q_idx = q_idx
            
            user_choice = str.radio("Choose the correct IPDE commentary term:", str.session_state.current_options, index=None, key=f"q_radio_{q_idx}")
            
            if str.button("Submit Assessment Identification Choice", type="primary"):
                if user_choice is None:
                    str.warning("Please highlight a tracking option selection button before submitting.")
                else:
                    if user_choice == correct:
                        str.session_state.quiz_score += 10
                        str.toast("✓ Correct Maneuver Identified!", icon="🟢")
                    else:
                        str.toast(f"❌ Incorrect. The correct term was {correct}.", icon="🔴")
                    
                    str.session_state.current_question_idx += 1
                    str.rerun()
