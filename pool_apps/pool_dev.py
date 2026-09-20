import streamlit as st
import pandas as pd
import os

# 🎨 1. Set Page Configuration & Title
st.set_page_config(page_title="CueCombat Tracker", page_icon="🎱", layout="wide")

# 💾 2. DATABASE LOCAL SYSTEM SETUP (Persistent CSV Tracking)
DB_FILE = "cuecombat_data.csv"

if not os.path.exists(DB_FILE):
    df_init = pd.DataFrame(columns=["Result", "Stroke Quality", "Turning Point"])
    df_init.to_csv(DB_FILE, index=False)

# Injecting clean Custom CSS for border rounding and metrics look
st.markdown("""
    <style>
    .stMetric {
        background-color: #1E293B;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    div[data-testid="stForm"] {
        border-radius: 12px;
        background-color: #0F172A;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎱 CueCombat // The Sovereign Player Console")
st.caption("Track the variance, calibrate your cue stroke, and dominate the felt.")

# 🧱 3. Read Database to Update Top Metric Banner Cards dynamically
df_current = pd.read_csv(DB_FILE)
total_frames = len(df_current)
wins_count = len(df_current[df_current["Result"] == "I Won"])

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(label="Your Target Speed", value="600 Fargo", delta="Database Clean")
with metric_col2:
    st.metric(label="Total Logged Frames", value=f"{total_frames} Frames", delta="Real-time Tracker")
with metric_col3:
    st.metric(label="Total Wins Secured", value=f"{wins_count} Wins", delta="Velocity High")

st.divider()

# 📐 4. Main Interface Split - 2 Large Custom Horizontal Areas
left_panel, right_panel = st.columns(2)

with left_panel:
    st.subheader("📝 Ultra-Fast Post-Frame Log")
    st.caption("Log your data during the rack. Zero typing required.")
    
    with st.form("fast_log_form", clear_on_submit=True):
        result = st.radio("Frame Result", ["I Won", "I Lost"], horizontal=True)
        execution_quality = st.slider("Your Overall Stroke Quality (1-10)", 1, 10, 7)
        st.write("What was the primary turning point of the frame?")
        turning_point = st.selectbox(
            "Select the major factor:",
            [
                "Pure Mechanical Success (Ran out)",
                "Unlucky Roll / Anomaly",
                "Missed Position / Shape Error",
                "Dogged a Ball (Form Defect)",
                "Opponent Safe / Locked Up"
            ]
        )
        
        fast_submit = st.form_submit_button("Lock Frame Into Registry")
        if fast_submit:
            new_row = pd.DataFrame([[result, execution_quality, turning_point]], columns=["Result", "Stroke Quality", "Turning Point"])
            new_row.to_csv(DB_FILE, mode='a', header=False, index=False)
            st.toast("Frame locked into hard drive database successfully!")
            st.rerun()

with right_panel:
    st.subheader("🎯 Active Daily Calibration Challenge")
    
    tab1, tab2 = st.tabs(["🔥 Today's Drill", "📈 Your Performance Metrics"])
    
    with tab1:
        # 🤖 ADAPTIVE AUTOMATION ENGINE
        # The script calculates your primary failure patterns from your data history
        if total_frames > 0 and len(df_current[df_current["Result"] == "I Lost"]) > 0:
            losses_df = df_current[df_current["Result"] == "I Lost"]
            primary_weakness = losses_df["Turning Point"].mode()[0] # Finds the most frequent reason for losing
            
            if primary_weakness == "Missed Position / Shape Error":
                st.warning("⚠️ **System Feedback: Position Defect Detected**")
                st.info("🎯 **Adaptive Drill: The 3-Ball Line-Up Control**")
                st.write("Set 3 balls in a straight line down the center rail. You must pocket all three in numerical order, forcing the cue ball to return to the center diamond after every single contact. Do not touch side cushions.")
                
            elif primary_weakness == "Dogged a Ball (Form Defect)":
                st.error("⚠️ **System Feedback: Mechanical Deflection Detected**")
                st.info("🎯 **Adaptive Drill: The Straight-In Stop-Shot Calibration**")
                st.write("Place the object ball on the foot spot. Shoot 10 straight-in shots from the head string. The cue ball must freeze completely dead on impact without any spin drift.")
                
            elif primary_weakness == "Opponent Safe / Locked Up":
                st.success("🧠 **System Feedback: High tactical safety environments**")
                st.info("🎯 **Adaptive Drill: The Two-Cushion Escape Drill**")
                st.write("Lock the object ball tight behind the point of the pocket. Practice executing systematic two-cushion safety escapes using the diamond kick systems.")
                
            else:
                st.info("🎯 **Standard Drill: The 15-Ball Clear Out Matrix**")
                st.write("Throw all 15 balls randomly onto the cloth. You must pocket them in absolute open rotation. Focus entirely on steady breathing and standard cue tip alignment.")
        else:
            # Baseline drill if no matches are logged yet
            st.info("🎯 **Baseline Drill: Center-Ball Stroke Alignment**")
            st.write("Shoot the cue ball straight down the center diamond lines to the foot rail. It must bounce straight back and hit your exact cue tip without drifting off course.")

        score = st.number_input("Successful Execution Run / 10", min_value=0, max_value=10, value=8)
        if score >= 8:
            st.success("Elite mechanics. Your 600 speed is completely wired into your nervous system.")
        else:
            st.warning("Form deviation noted. Continue garage table calibration frames.")
            
    with tab2:
        st.write("Your long-term performance vector analytics data logs:")
        if total_frames > 0:
            st.success("📊 Local Ledger Active!")
            st.dataframe(df_current, hide_index=True, use_container_width=True)
            win_pct = (wins_count / total_frames) * 100
            st.info(f"🏆 Current Analytical Session Win Rate: **{win_pct:.1f}%**")
        else:
            st.info("📊 Data logs compiling... Log your first frame to unlock local tracking metrics.")

st.divider()
st.subheader("📊 Live Variance Dashboard & Form Matrix")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    if total_frames > 0:
        avg_stroke = df_current["Stroke Quality"].mean()
        st.metric(label="Average Stroke Quality (Session)", value=f"{avg_stroke:.1f} / 10", delta="Live Baseline")
    else:
        st.metric(label="Average Stroke Quality (Session)", value="N/A", delta="Awaiting Logs")

with chart_col2:
    loss_count = len(df_current[df_current["Result"] == "I Lost"])
    unlucky_count = len(df_current[(df_current["Result"] == "I Lost") & (df_current["Turning Point"] == "Unlucky Roll / Anomaly")])
    
    if loss_count > 0:
        variance_pct = (unlucky_count / loss_count) * 100
        st.metric(label="Environmental Variance Loss Rate (Unlucky Rolls)", value=f"{variance_pct:.1f}%", delta="Anomaly State")
    else:
        st.metric(label="Environmental Variance Loss Rate (Unlucky Rolls)", value="0.0%", delta="Clean Felt")