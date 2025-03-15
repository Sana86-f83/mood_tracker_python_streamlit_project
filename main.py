import streamlit as st     # Creating the web interface
import pandas as pd        # Data manipulations
import datetime            # Handling dates
import csv                 # Reading & writing CSV files
import os                  # File operations

MOOD_FILE = "mood_log.csv"  # Fixing file name

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE, encoding="utf-8")

def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)  # ✅ Check if the file exists

    # Open file in append mode with UTF-8 encoding
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # ✅ Write header only if the file is new
        if not file_exists:
            writer.writerow(["Date", "Mood"])  

        writer.writerow([date, mood])  # ✅ Write mood entry

# Apply Background & Text Color for Dark Theme Compatibility
st.markdown(
    """
    <style>
    /* Apply background color & text color */
    html, body,label, [class*="stApp"] {
        background-color: black !important;
        color: white !important;
    }
    div.stButton > button {
        background-color: #0d1b85; /* Blue Color */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    
    /* Ensure footer stays at the bottom */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: black;
        text-align: center;
        padding: 10px;
        font-size: 16px;
        color: blue;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color:yellow !important;
        background: linear-gradient(to top, black, blue);
        border-radius:40px;
    }
    </style>
    <h1 class="title">📌 Mood Tracker</h1>
    """,
    unsafe_allow_html=True
)

today = datetime.date.today()

st.subheader("😊 How are you feeling today?")

mood = st.selectbox("🎭 Select your mood", ["😃 Happy", "😢 Sad", "😠 Angry", "😐 Neutral"])

if st.button("📝 Log Mood"):
    save_mood_data(today, mood)
    st.success("✅ Mood logged successfully!")

# Load and Display Mood Trends
data = load_mood_data()

if not data.empty:
   st.subheader("📈 Mood Trends Over Time")

   data["Date"] = pd.to_datetime(data["Date"])
   mood_counts = data.groupby("Mood").count()["Date"]

   st.bar_chart(mood_counts)  # Mood Distribution Chart

# Footer at the bottom
st.markdown('<div class="footer">Build with 💖 by <span style="color:white"> Sana Faisal </span>| © 2024 All Rights Reserved</div>', unsafe_allow_html=True)
