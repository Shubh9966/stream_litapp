import streamlit as st
import joblib
import pickle
import numpy as np

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Credit Risk Predictor", layout="centered")
st.title("💳 Credit Risk Predictor")

# ── Load model ────────────────────────────────────────────────────────────────
rf_model = joblib.load('credit_risk_pipeline.pkl')

# ── Load your encoders dict (contains only: Sex, Housing, Saving, Purpose) ────
with open('encoders (1).pkl', 'rb') as f:
    encoders = pickle.load(f)

# Pull the 4 available encoders
le_sex     = encoders['Sex']
le_housing = encoders['Housing']
le_saving  = encoders['Saving']
le_purpose = encoders['Purpose']

# Manual mapping for Checking account (since no encoder was saved for it)
checking_mapping = {
    'little': 0,
    'moderate': 1,
    'rich': 2,
    'nan': 3
}

# ── User Inputs ───────────────────────────────────────────────────────────────
age            = st.number_input('Age', min_value=18, max_value=100, step=1)
sex            = st.selectbox('Sex', le_sex.classes_.tolist())
job            = st.selectbox('Job (0–3)', [0, 1, 2, 3])
housing        = st.selectbox('Housing', le_housing.classes_.tolist())
saving_account = st.selectbox('Saving accounts', le_saving.classes_.tolist())
checking_acc   = st.selectbox('Checking account', list(checking_mapping.keys()))
credit_amount  = st.number_input('Credit Amount', min_value=1, step=1)
duration       = st.number_input('Duration (months)', min_value=1, step=1)
purpose        = st.selectbox('Purpose', le_purpose.classes_.tolist())

# ── Prediction ────────────────────────────────────────────────────────────────
if st.button('Submit'):
    try:
        # Encode categorical inputs
        sex_enc      = le_sex.transform([sex])[0]
        housing_enc  = le_housing.transform([housing])[0]
        saving_enc   = le_saving.transform([saving_account])[0]
        purpose_enc  = le_purpose.transform([purpose])[0]
        checking_enc = checking_mapping[checking_acc]

        # Build feature vector in the exact order your model expects
        X = np.array([[ 
            age,
            sex_enc,
            job,
            housing_enc,
            saving_enc,
            checking_enc,
            credit_amount,
            duration,
            purpose_enc
        ]])

        # Predict
        pred = rf_model.predict(X)[0]
        conf = rf_model.predict_proba(X).max() * 100

        # Display
        label = "✅ safe Credit Risk" if pred == 0 else "⚠️ Bad Credit Risk"
        st.success(f"Prediction: {label}")
        st.info(f"Model confidence: {conf:.2f}%")

    except Exception as e:
        st.error(f"Error during prediction: {e}")
