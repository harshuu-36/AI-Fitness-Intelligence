import streamlit as st

st.set_page_config(
    page_title="AI Fitness Intelligence Platform",
    page_icon="💪",
    layout="wide"
)

# ===========================
# Custom Header
# ===========================

st.markdown("""
<div style='
background: linear-gradient(90deg,#0F2027,#203A43,#2C5364);
padding:25px;
border-radius:15px;
text-align:center;
margin-bottom:20px;'>

<h1 style='
color:#00E5FF;
font-size:48px;
margin-bottom:5px;'>
💪 AI Fitness Intelligence Platform
</h1>

<h4 style='
color:white;'>
SQL • Python • Machine Learning • Streamlit • Power BI
</h4>

</div>
""", unsafe_allow_html=True)

# ===========================
# Welcome Section
# ===========================

st.write("""
Welcome to the **AI Fitness Intelligence Platform**.

Use the **sidebar** to navigate between different modules of the application.

### Available Modules

- 📊 Dashboard
- 🤖 AI Weight Prediction
- 🏥 Health Report
- 💡 AI Recommendations
""")

st.info("👈 Select a page from the left sidebar to get started.")