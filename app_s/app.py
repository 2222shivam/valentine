import streamlit as st
import time
import base64
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Someone Special ❤️",
    page_icon="❤️",
    layout="centered",
)

# ---------------- MOBILE FIRST DESIGN ----------------
st.markdown("""
<style>

/* Hide Streamlit UI */
[data-testid="stSidebar"] {display:none;}
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* iPhone safe area */
.stApp {
padding-top: env(safe-area-inset-top);
background: linear-gradient(180deg,#fff0f6 0%, #ffe4ec 45%, #fff7fa 100%);
font-family:-apple-system,BlinkMacSystemFont,sans-serif;
}

/* Center content width for phones */
.block-container {
max-width: 420px;
padding-top: 1rem;
padding-bottom: 2rem;
}

/* Romantic card */
.love-box{
background:rgba(255,255,255,0.85);
padding:20px;
border-radius:20px;
text-align:center;
box-shadow:0 8px 28px rgba(255,75,110,0.25);
animation:fadeIn 0.7s ease;
font-size:17px;
line-height:1.6;
}

/* Animation */
@keyframes fadeIn{
from{opacity:0;transform:translateY(12px);}
to{opacity:1;transform:translateY(0);}
}

/* Title mobile optimized */
.title{
text-align:center;
font-size:26px;
font-weight:700;
margin-top:8px;
margin-bottom:10px;
}

/* iPhone touch buttons */
.stButton button{
height:56px;
border-radius:14px;
font-size:17px;
transition:0.25s;
}

.stButton button:hover{
transform:scale(1.03);
box-shadow:0 6px 18px rgba(255,75,110,0.35);
}

</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING HEARTS ----------------
if os.path.exists("assets/hearts.html"):
    with open("assets/hearts.html", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=0)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = 0

# =====================================================
# PAGE 0
# =====================================================
if st.session_state.page == 0:

    st.markdown("<div class='title'>🌸 A Small Surprise 🌸</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='love-box'>
💖 Someone made this specially for you 💖<br><br>
Just follow along… and smile a little 😊
</div>
""", unsafe_allow_html=True)

    if st.button("Start ❤️", use_container_width=True):
        st.session_state.page = 1
        st.rerun()

# =====================================================
# PAGE 1
# =====================================================
elif st.session_state.page == 1:

    st.markdown("<div class='title'>😊 Before We Start</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='love-box'>
🌷 Answer honestly<br>
✨ No overthinking<br>
💫 Just smile
</div>
""", unsafe_allow_html=True)

    if st.button("I'm Ready ✨", use_container_width=True):
        st.session_state.page = 2
        st.rerun()

# =====================================================
# PAGE 2
# =====================================================
elif st.session_state.page == 2:

    st.markdown("<div class='title'>😄 Round 1</div>", unsafe_allow_html=True)

    st.radio("💬 Your perfect free time:",
        ["Sleeping like panda 🐼",
         "Scrolling reels 📱",
         "Talking to someone special ☎️",
         "Annoying one favorite person 😏"],
        key="q1")

    st.radio("✨ Your superpower:",
        ["Being naturally cute 💫",
         "Making someone smile 😊",
         "Winning arguments 😄",
         "All of these 😌"],
        key="q2")

    if st.button("Continue 💭", use_container_width=True):
        st.session_state.page = 3
        st.rerun()

# =====================================================
# PAGE 3
# =====================================================
elif st.session_state.page == 3:

    st.markdown("<div class='title'>💭 Round 2</div>", unsafe_allow_html=True)

    st.radio("🌙 Best date sounds like:",
        ["Long walk 🌙",
         "Food + talking 🍜",
         "Doing nothing together 🤍",
         "Right person matters ❤️"],
        key="q3")

    st.radio("💖 When someone truly cares:",
        ["Smile secretly 😊",
         "Feel safe 🤍",
         "Heart becomes soft ❤️"],
        key="q4")

    if st.button("Almost There 👀", use_container_width=True):
        st.session_state.page = 4
        st.rerun()

# =====================================================
# PAGE 4 — ANALYZER
# =====================================================
elif st.session_state.page == 4:

    st.markdown("<div class='title'>💘 Love Compatibility Analyzer</div>", unsafe_allow_html=True)

    box = st.empty()
    progress = st.progress(0)

    steps = [
        "Reading answers... 💭",
        "Measuring smiles 😊",
        "Checking heart connection ❤️",
        "Calculating warmth ✨",
        "Preparing surprise 💖"
    ]

    percent = 0
    for step in steps:
        for i in range(20):
            percent += 1
            progress.progress(percent)
            time.sleep(0.04)

        box.markdown(f"<div class='love-box'>{step}</div>", unsafe_allow_html=True)

    time.sleep(1.2)
    st.session_state.page = 5
    st.rerun()

# =====================================================
# PAGE 5 — SURPRISE
# =====================================================
elif st.session_state.page == 5:

    st.balloons()

    st.markdown("<div class='title'>💖 Happy Valentine's Day 💖</div>", unsafe_allow_html=True)

    with open("assets/her_photo.jpg","rb") as img:
        img_base64 = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <div style="text-align:center;margin-top:10px;">
        <img src="data:image/jpeg;base64,{img_base64}"
        style="
        width:72%;
        max-width:280px;
        border-radius:22px;
        box-shadow:0 12px 30px rgba(255,75,110,0.35);
        ">
    </div>
    """, unsafe_allow_html=True)

    message = """
🌷 You thought this was just a small quiz…  

But every answer led to you 💕  

✨ You make ordinary days special  
🌸 You bring calm into chaos  
💫 And unknowingly became my favorite person  

❤️ Happy Valentine's Day ❤️
"""

    box = st.empty()
    text=""

    for char in message:
        text += char
        box.markdown(f"<div class='love-box'>{text}</div>", unsafe_allow_html=True)
        time.sleep(0.03)
