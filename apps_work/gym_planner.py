import streamlit as str

# Lock page configuration parameters tightly at the top of runtime execution
str.set_page_config(page_title="PPL Machine Tracker", page_icon="🏋️‍♂️", layout="centered")

# Custom CSS Theme Configuration injection loop to match your Royal Blue, Yellow, and White academy colors
str.markdown("""
    <style>
        .stApp {
            background-color: #ffffff !important;
            color: #1e222b !important;
        }
        .main-header {
            color: #0d47a1 !important; 
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            text-align: center;
            margin-bottom: 5px;
            line-height: 1.3;
        }
        .sub-caption {
            color: #555555 !important;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 25px;
            font-weight: 500;
        }
        [data-testid="stSidebar"] {
            background-color: #0d47a1 !important; 
        }
        [data-testid="stSidebar"] * {
            color: #ffffff !important; 
        }
        .streamlit-expanderHeader {
            background-color: #fff9c4 !important; 
            border-left: 5px solid #0d47a1 !important;
            color: #1e222b !important;
            font-weight: bold !important;
            font-size: 1.05rem !important;
        }
        .stAlert {
            background-color: #e3f2fd !important; 
            border-left: 5px solid #0d47a1 !important;
            color: #0d47a1 !important;
        }
        input {
            color: #0d47a1 !important;
            background-color: #f0f2f6 !important;
            -webkit-text-fill-color: #0d47a1 !important;
        }
    </style>
""", unsafe_allow_html=True)

# App Custom Branded Header Strings
str.markdown('<div class="main-header">Planet Fitness PPL Machine Training System</div>', unsafe_allow_html=True)
str.markdown('<div class="sub-caption">Calculated Hypertrophy Engine • Powered by 6\'2\" Athlete Specs</div>', unsafe_allow_html=True)

# Sidebar Gym Tracking Parameters Navigation Controls Dock
str.sidebar.header("🏋️‍♂️ Active Session")
workout_day = str.sidebar.radio("Select Today's Training Split:", ["Day 1: PUSH (Chest/Shoulders/Triceps)", "Day 2: PULL (Back/Biceps)", "Day 3: LEGS (Lower Body/Foundation)"])

str.sidebar.markdown("---")
str.sidebar.markdown(f"**Current Athlete Profile:**\n* Height: 6'2\"\n* Current Weight: 205 lbs (Lean Base)")

if "PUSH" in workout_day:
    str.header("🔥 Day 1: Push Routine")
    str.info("Target Focus: Building upper-body frame width (Chest & Shoulders) while priming your arm extensions.")
    
    with str.expander("1. Seated Chest Press Machine (3 Sets x 10 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 70 lbs – 90 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** If you hit 10 reps easily, go to 90 lbs. If rep 8 shakes, stick to 70 lbs.")
        str.markdown("**Gym Setup Guide:** Adjust the seat bottom height until the horizontal handles line up perfectly across the middle of your chest. Plant your feet flat on the floor.")
        str.markdown("**Execution:** Press the handles forward smoothly without locking your elbows entirely at the top. Return slowly until your chest stretches.")

    with str.expander("2. Seated Overhead Shoulder Press Machine (3 Sets x 10 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 50 lbs – 60 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Shoulders are smaller muscle joints; start conservative at 50 lbs to protect your posture.")
        str.markdown("**Gym Setup Guide:** Sit completely flat against the back pad. Grab the vertical handles to target your front deltoids cleanly.")
        str.markdown("**Execution:** Push straight up toward the ceiling. Control the weight on the way down until handles drop just below chin level.")

    with str.expander("3. Cable Tricep Rope Pushdowns (3 Sets x 12 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 30 lbs – 40 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Hook the pin on the 30 or 40 lb plate on the vertical cable tower stack.")
        str.markdown("**Gym Setup Guide:** Connect the black nylon rope attachment to the high pulley tower. Take a step back and lean your upper body slightly forward.")
        str.markdown("**Execution:** Pin your elbows tightly against your ribs like hinges. Push the rope straight down to your thighs, flaring your hands apart at the bottom.")

elif "PULL" in workout_day:
    str.header("⚡ Day 2: Pull Routine")
    str.info("Target Focus: High-iron back thickness and bicep contraction to build a powerful athletic posture.")
    
    with str.expander("1. Wide-Grip Lat Pulldown Machine (3 Sets x 10 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 80 lbs – 100 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Your back muscles are big and strong; your 6'2\" frame can leverage an 80 lb start easily.")
        str.markdown("**Gym Setup Guide:** Adjust the knee pads so your thighs are locked down securely under the cushions. Grab the long bar at the outer bends.")
        str.markdown("**Execution:** Pull the bar straight down to your upper chest while leaning back slightly. Squeeze your shoulder blades together tightly at the bottom.")

    with str.expander("2. Seated Cable Row Machine (3 Sets x 12 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 70 lbs – 90 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Focus entirely on pulling with your back elbows, not swinging your spine.")
        str.markdown("**Gym Setup Guide:** Sit down on the bench, place feet flat on the metal pads, and grab the V-bar attachment. Keep a slight bend in your knees.")
        str.markdown("**Execution:** Pull the handle straight into your belly button. Drive your elbows back past your ribs and puff your chest forward.")

    with str.expander("3. Dumbbell Bicep Hammer Curls (3 Sets x 12 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 15 lb – 20 lb Dumbbells**")
        str.markdown("🔍 **The Rep 8 Rule:** Pick up the 15 or 20 lb silver-capped weights from the heavy free-weight rack row.")
        str.markdown("**Gym Setup Guide:** Grab a pair of mid-weight dumbbells from the free-weight rack. Stand up tall with palms facing inwards toward each other.")
        str.markdown("**Execution:** Curl the weights up like you are swinging a hammer. Keep your palms facing each other the entire time to thicken the forearms and biceps.")

elif "LEGS" in workout_day:
    str.header("🦵 Day 3: Legs Routine")
    str.info("Target Focus: Building a solid lower foundation to increase fat-burning speed and power your 1.5-mile running pace.")
    
    with str.expander("1. Seated Leg Press Sled Machine (3 Sets x 10 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 110 lbs – 130 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Since you weigh 205 lbs, your legs already carry heavy mass. Start at 110 or 130 lbs.")
        str.markdown("**Gym Setup Guide:** Sit down flat in the low sled seat and place your feet flat on the metal platform, hip-width apart. Disengage the safety locks cleanly.")
        str.markdown("**Execution:** Lower the weight slowly until your knees form a 90-degree angle. Push through your heels to return to the top—never lock your knees out!")

    with str.expander("2. Seated Leg Extension Machine (3 Sets x 12 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 50 lbs – 70 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Focus on isolating the front thighs without swinging your upper body.")
        str.markdown("**Gym Setup Guide:** Adjust the back pad so your knees bend perfectly at the edge of the seat. Position the padded shin bar right above your ankles.")
        str.markdown("**Execution:** Extend your legs straight out until your quads flex completely. Hold for one second, then lower the weight under control.")

    with str.expander("3. Seated Leg Curl Machine (3 Sets x 12 Reps)"):
        str.markdown("🎯 **TARGET STARTING WEIGHT: 50 lbs – 60 lbs**")
        str.markdown("🔍 **The Rep 8 Rule:** Squeeze hard behind your knees at the bottom of the movement.")
        str.markdown("**Gym Setup Guide:** Sit down with the back cushion supporting your spine. Place the top leg rollers tightly over your lower thighs.")
        str.markdown("**Execution:** Pull your heels straight down and backward toward your seat, flexing your hamstrings. Return slowly to the top position.")

# Global Midsection Tightening Protocol Block (Appears on every single screen layout)
str.markdown("---")
str.subheader("🎯 Core Tightening & Compression Protocol")
str.success("Execute these two stability maneuvers at the end of your session to pull your stomach inward and flatten the midsection.")
str.markdown("*   **Stomach Vacuums:** 4 Sets x 10-Second Holds (Suck your belly button deeply toward your spine on an empty stomach).")
str.markdown("*   **Forearm Plank Hold:** 3 Sets x 45-Second Holds (Keep your glutes squeezed, hips level, and core completely braced).")

# ==============================================================================
# 🛡️ SOVEREIGN ABS MATRIX (HYPERTROPHY DEFINITION MATRIX)
# ==============================================================================
str.markdown("---")
str.subheader("🎯 Core Tightening & Hypertrophy Finisher")
str.success("Execute these targeted movements at the end of your scheduled PPL sessions to thicken abdominal rows and force them through your 16-18% body fat layer.")

# Multi-column layout to split the training days cleanly
col1, col2, col3 = str.columns(3)

with col1:
    str.markdown("### 🔴 Pull Day")
    str.markdown("**1. Hanging Knee Raises**")
    str.markdown("*   *Volume:* 3 Sets x 12-15 Reps")
    str.markdown("*   *Form Key:* Curl your pelvis upward toward your chest. Focus on tilting your hips to activate the lower abs.")
    str.markdown("**2. Cable Woodchoppers**")
    str.markdown("*   *Volume:* 3 Sets x 12 Reps (Each Side)")
    str.markdown("*   *Form Key:* Lock your hips completely forward. Use only your obliques to rotate your torso.")

with col2:
    str.markdown("### 🔵 Push Day")
    str.markdown("**1. Kneeling Cable Crunches**")
    str.markdown("*   *Volume:* 4 Sets x 10-12 Reps")
    str.markdown("*   *Form Key:* Grab rope from high pulley. Flex spine downward, pulling elbows into thighs right above the knee.")
    str.markdown("**2. RKC Plank Finisher**")
    str.markdown("*   *Volume:* 2 Sets x Max Time")
    str.markdown("*   *Form Key:* Pull elbows toward toes and squeeze glutes maximally to create extreme internal wall tension.")

with col3:
    str.markdown("### 跑 Leg Day")
    str.markdown("**1. Incline Bench Crunches**")
    str.markdown("*   *Volume:* 3 Sets x 12 Reps")
    str.markdown("*   *Form Key:* Hold a 10-25 lb plate flat against your chest. Lower slowly, crunching up entirely via ab contraction.")
    str.markdown("**2. Stomach Vacuums**")
    str.markdown("*   *Volume:* 4 Sets x 10-Second Holds")
    str.markdown("*   *Form Key:* Blow all air out of lungs. Suck your belly button deeply toward your spine and compress tightly.")

str.info("💡 Reminder: Abs grow during the recovery phase. Do not add heavy core work to your Day 4 Active Recovery Flush. Keep your rest days sacred to drop cortisol fat-retention plateaus.")