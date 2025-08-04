# Cyber Risk Analyzer – ML-Powered Behavior-Based Security Tool

This project is a lightweight yet powerful cybersecurity awareness tool that uses Machine Learning to estimate how likely a user is to fall victim to online threats. By analyzing basic behavioral habits — like how often you reuse passwords or connect to public Wi-Fi — the system provides an instant risk level: **Low**, **Medium**, or **High**.

Designed with a focus on human behavior, the app aims to **educate**, **assess**, and **promote better cybersecurity hygiene** in an interactive way.

---

##  Key Highlights
-  Built on a custom-trained machine learning model
-  Simple interface built using Streamlit
-  Real-time cyber risk prediction based on behavior
-  Provides awareness on common cyber habits and pitfalls

---

##  Tech Stack
- `Python 3.12`
- `Streamlit` – for the frontend web app
- `Scikit-learn` – model training & evaluation
- `Pandas` – data preprocessing
- `Pickle` – for saving the trained model

---

##  Dataset Overview

The model was trained on a synthetic but behaviorally grounded dataset with the following features:

- `uses_2fa`: Does the user enable 2-factor authentication?
- `clicks_unknown_links`: Likelihood of clicking suspicious links
- `reuses_passwords`: Reuse habits for passwords
- `uses_public_wifi`: Frequency of connecting to open Wi-Fi
- `social_media_apps`: Usage of potentially vulnerable platforms
- `updates_software`: Regularity of software and OS updates
- `shares_personal_data`: Tendencies to share personal info online
- `grants_all_permissions`: App permission behaviors
- `avg_password_length`: Average length of passwords

The target variable is the overall **`cyber_risk_level`** — classified into `Low`, `Medium`, or `High`.

~Mohammed Ghouse Mohiuddin
