

import streamlit as st
import numpy as np
import joblib

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Cyber Risk Predictor",
    page_icon=" ",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    html, body {
        background-color: #e0e5ec;
        font-family: 'Segoe UI', sans-serif;
    }
    .main-box {
        background: #ecf0f3;
        padding: 2rem 3rem;
        border-radius: 20px;
        box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #ffffff;
        margin-top: 20px;
        margin-bottom: 2rem;
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        color: #1a237e;
    }
    .subtitle {
        font-size: 1.25rem;
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    .tip-box {
        background-color: #f0f9ff;
        padding: 1rem 1.5rem;
        border-left: 6px solid #1565c0;
        border-radius: 10px;
        font-size: 1.05rem;
        color: #0d1b2a;
        margin-bottom: 1.5rem;
    } 
    .section-title {
        font-size: 1.6rem;
        font-weight: bold;
        color: #0d47a1;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    footer {visibility: hidden;}

    /* Hide default Streamlit header */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .css-18e3th9 {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

# ------------------ MAIN HEADER ------------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<div class="title">Cyber Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle"> Predict your cyber risk level based on digital habits</div>', unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    
    st.title("About")
    st.info("An ML-powered app to estimate your cybersecurity risk level.")

    st.markdown("#### Developer")
    st.markdown("[**View my Website**](http://www.linkedin.com/in/md-ghouse-mohiuddin-0622a12a6)")
    st.markdown("[GitHub Profile](https://github.com/mohammed-ghouse-99)")
    st.markdown(" ghousenaser2005@gmail.com")

# ------------------ LOAD MODEL ------------------
try:
    model = joblib.load("cyber_risk_model.pkl")
except Exception as e:
    st.error(f"Model loading failed: {e}")

# ------------------ INPUT SECTION ------------------
st.markdown('<div class="section-title"> Enter Your Cybersecurity Habits</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    uses_2fa = st.selectbox("Do you use Two-Factor Authentication (2FA)?", [0, 1])
    reuses_passwords = st.selectbox("Do you reuse the same password?", [0, 1])
    updates_software = st.selectbox("Do you update software regularly?", [0, 1])

with col2:
    clicks_unknown_links = st.selectbox("Do you click on unknown links?", [0, 1])
    uses_public_wifi = st.selectbox("Do you use public Wi-Fi often?", [0, 1])
    shares_personal_data = st.selectbox("Do you share personal data online?", [0, 1])

with col3:
    social_media_apps = st.slider("Number of social media apps you use", 0, 10, 3)
    grants_all_permissions = st.selectbox("Do you grant all app permissions?", [0, 1])
    avg_password_length = st.slider("Average password length", 4, 20, 10)

# ------------------ MAKE PREDICTION ------------------
input_data = np.array([[uses_2fa, clicks_unknown_links, reuses_passwords, uses_public_wifi,
                        social_media_apps, updates_software, shares_personal_data,
                        grants_all_permissions, avg_password_length]])

if st.button(" Predict My Risk Level"):
    try:
        prediction = model.predict(input_data)[0]
        st.markdown('<div class="section-title"> Your Cyber Risk Level:</div>', unsafe_allow_html=True)
        if prediction == "High":
            st.error(" High Risk! You need to improve your cybersecurity practices.")
        elif prediction == "Moderate":
            st.warning(" Moderate Risk. Take some steps to strengthen your security.")
        else:
            st.success(" Low Risk. Your digital hygiene looks good!")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# ------------------ CYBER TIPS ------------------
st.markdown('<div class="section-title"> Cybersecurity Tips</div>', unsafe_allow_html=True)
st.markdown("""
<div class='tip-box'>
<ul>
  <li> Use strong, unique passwords for every account.</li>
  <li> Enable 2FA (Two-Factor Authentication) wherever possible.</li>
  <li> Avoid clicking on unknown or suspicious links.</li>
  <li> Don’t use public Wi-Fi without a VPN.</li>
  <li> Be cautious about app permissions.</li>
  <li> Keep software and apps up to date.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ------------------ FEEDBACK FORM ------------------
st.markdown('<div class="section-title"> Feedback Form</div>', unsafe_allow_html=True)
with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    feedback = st.text_area("Your Feedback")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success(" Thank you for your feedback!")

# ------------------ FOOTER ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; font-size:0.9rem;'>© 2025 Mohammed Ghouse Mohiuddin | Built with using Streamlit</div>",
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)
