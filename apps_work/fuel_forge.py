import streamlit as st

# Force high-performance dark theme layout
st.set_page_config(
    page_title="FuelForge Engine", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Global Style Injection for Clean Dark Backgrounds
st.markdown("""
    <style>
        .reportview-container { background: #0e1117; }
        div.stButton > button:first-child { background-color: #1e293b; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ FUELFORGE: Sovereign Nutrition Engine")
st.markdown("### **Operator Profile:** 6'2\" | 200 lbs | Target: < 20% Body Fat | Target Intake: 2,300 kcal")
st.markdown("---")

# Layout Split: Chronological Timeline vs Biological Core
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📅 Daily Chronological Fuel Schedule")
    st.caption("Click each block to verify your specific clean-cut meal window and exact portions.")
    
    with st.expander("🌅 BLOCK 1 — 07:00 AM | Pre-Workout Activation"):
        st.markdown("🎯 **Menu:** Black Coffee + 1 Whole Banana")
        st.caption("🔒 *Execution Rule: Consume immediately upon waking before hitting Planet Fitness.*")
        
    with st.expander("⚡ BLOCK 2 — 08:30 AM | Post-Workout Muscle Lock"):
        st.markdown("🎯 **Menu:** 1 Core Power / Fairlife Shake + 3 Scrambled Eggs")
        st.caption("🔒 *Execution Rule: Consume within 45 minutes of completing your machine split.*")
        
    with st.expander("🥪 BLOCK 3 — 01:00 PM | Mid-Shift Glycogen Sustain"):
        st.markdown("🎯 **Exact Turkey Sandwich Blueprint:**")
        st.markdown("""
        * 🍞 **2 Slices of True Sourdough** *(Fermented, low-glycemic complex carbs)*
        * 🥩 **5 Ounces of Deli Sliced Turkey Breast** *(Oven-roasted/mesquite; approx. 5-6 thick slices)*
        * 🥑 **1/2 of a Medium Avocado** *(Mashed directly onto the bread instead of using mayo)*
        * 🥬 **Unlimited Romaine Lettuce / Spinach + 2 Slices of Tomato** *(Zero-calorie volume)*
        """)
        st.caption("🔒 *Execution Rule: Clean fuel midway through your instructional driving shifts to crush fatigue.*")
        
    with st.expander("🥩 BLOCK 4 — 06:30 PM | Deep Tissue Recovery"):
        st.markdown("🎯 **Exact Target Dinner Portions (Weighed Raw):**")
        st.markdown("""
        * 🐟 **8 Ounces of WinCo Fish** *(Salmon or Halibut - provides 45-50g of pure muscle-repairing protein)*
        * 🥦 **6 Ounces of Fresh Asparagus** *(Roughly 8 to 10 medium spears - acts as a natural water-flushing diuretic)*
        * 🫒 **1 Teaspoon of Olive Oil** *(For tossing/roasting the asparagus; season with salt, pepper, garlic powder)*
        """)
        st.caption("🔒 *Execution Rule: Solid cuts only. Zero ground meat text rejection protocol. Seasonings must have 0g sugar.*")
        
    with st.expander("🍿 BLOCK 5 — 08:30 PM | Kinetic Window Reward"):
        st.markdown("🎯 **Menu:** 1.5 Cups SkinnyPop + 1 Cold Bai Drink")
        st.caption("🔒 *Execution Rule: Decompression phase while running frames with your dad.*")

with col2:
    st.subheader("🔬 Biological Impact & Action Mechanisms")
    
    # Interactive Selector to decode biochemical processes
    selected_block = st.radio(
        "Select an active meal block to inspect your system's metabolic reaction:",
        ["Pre-Workout", "Post-Workout", "Mid-Shift", "Deep Tissue", "Kinetic Reward"],
        horizontal=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if selected_block == "Pre-Workout":
        st.info("🔬 **Biochemical Strategy:** Accelerated Lipolysis & Glycogen Preservation")
        st.markdown("""
        * **The Caffeine Effect:** Drinking black coffee on an empty stomach spikes circulating epinephrine. This signals your body to mobilize fat cells from adipose tissue, prioritizing fat-burning during your morning lift.
        * **The Carbohydrate Bridge:** The banana provides rapid, low-stress simple sugars. This ensures your brain stays sharp and your muscles have instant energy, keeping you from flatlining or getting dizzy during heavy leg sets.
        """)
        
    elif selected_block == "Post-Workout":
        st.info("🔬 **Biochemical Strategy:** Muscle Retention & Anabolic Signaling")
        st.markdown("""
        * **The Micro-Filtered Protein:** The Fairlife shake floods your bloodstream with rapid-acting amino acids. This halts the muscle-wasting effects of cortisol (stress) that naturally rise during heavy gym training.
        * **The Micronutrient Core:** Whole eggs provide essential dietary cholesterol and healthy fats. This acts as a raw building block for natural hormone production, repairing torn muscle fibers while keeping your blood sugar stable.
        """)
        
    elif selected_block == "Mid-Shift":
        st.info("🔬 **Biochemical Strategy:** Insulin Stabilization & Cognitive Focus")
        st.markdown("""
        * **The Complex Sourdough:** Sourdough has a lower glycemic index than regular bread. It digests slowly over 3–4 hours, providing a steady baseline of energy that prevents afternoon exhaustion while instructing student drivers.
        * **The Lipids:** Monounsaturated fats from the avocado slow down gastric emptying. This keeps you full, prevents food cravings, and protects your focus through the end of your shift without any insulin spikes.
        """)
        
    elif selected_block == "Deep Tissue":
        st.info("🔬 **Biochemical Strategy:** Thermic Induction & Structural Repair")
        st.markdown("""
        * **The Solid-Cut Engine:** Digesting a dense, clean 8oz fish fillet requires massive energetic effort. Your body utilizes roughly 30% of the calories just breaking down the solid protein chains, naturally heating your metabolism.
        * **The Micronutrient Sweep:** Asparagus contains trace elements that act as a natural, safe diuretic. This helps flush sub-cutaneous water retention, giving you a harder, leaner look in the mirror as you drop below 20%.
        """)
        
    elif selected_block == "Kinetic Reward":
        st.info("🔬 **Biochemical Strategy:** Central Nervous System Calming")
        st.markdown("""
        * **The Volumetric Hack:** SkinnyPop provides high-volume fiber. It physically fills your stomach lining to signal fullness to your brain, preventing late-night cravings without depositing unneeded caloric density before sleep.
        * **The Clean Hydration:** The Bai drink delivers polyphenols and hydration with zero artificial sugars, preserving your gut biome health and keeping your system clean for tomorrow's 7:00 AM alarm.
        """)