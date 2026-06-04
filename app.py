
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="EduSight - Dropout Risk Predictor", layout="wide")

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_artifacts():
    model = joblib.load("dropout_risk_model.pkl")
    scaler = joblib.load("feature_scaler.pkl")
    return model, scaler

model, scaler = load_artifacts()

st.title("🎓 EduSight: Student Dropout Risk Prediction System")

st.markdown("""
This system predicts **Dropout Risk Percentage (0-100%)**
using Mental Health, Academic Performance, and Social Factors.
""")

# =========================
# INPUT FORM
# =========================
with st.form("prediction_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        stress_level = st.slider("Stress Level", 0.0, 10.0, 5.0)
        anxiety_score = st.slider("Anxiety Score", 0.0, 10.0, 5.0)
        depression_score = st.slider("Depression Score", 0.0, 10.0, 5.0)

    with col2:
        sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
        burnout_score = st.slider("Burnout Score", 0.0, 10.0, 5.0)
        academic_performance = st.slider("Academic Performance (%)", 0.0, 100.0, 70.0)

    with col3:
        financial_stress = st.slider("Financial Stress", 0.0, 10.0, 5.0)
        family_expectation = st.slider("Family Expectation", 0.0, 10.0, 5.0)
        social_support = st.slider("Social Support", 0.0, 10.0, 5.0)

    submitted = st.form_submit_button("Predict Dropout Risk")

# =========================
# PREDICTION
# =========================
if submitted:

    input_df = pd.DataFrame({
        'stress_level':[stress_level],
        'anxiety_score':[anxiety_score],
        'depression_score':[depression_score],
        'sleep_hours':[sleep_hours],
        'burnout_score':[burnout_score],
        'academic_performance':[academic_performance],
        'financial_stress':[financial_stress],
        'family_expectation':[family_expectation],
        'social_support':[social_support]
    })

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]
    prediction = max(0, min(100, prediction))

    if prediction < 30:
        risk = "LOW RISK 🟢"
        color = "#38a169"
        msg = "Student appears stable. Continue monitoring."
    elif prediction < 60:
        risk = "MODERATE RISK 🟡"
        color = "#d69e2e"
        msg = "Consider early intervention and support services."
    else:
        risk = "HIGH RISK 🔴"
        color = "#e53e3e"
        msg = "Urgent intervention needed. Recommend counseling and academic support."

    st.markdown(f"""
    <div style="padding:20px;border-left:8px solid {color};
    background:#f8f9fa;border-radius:10px;">
    <h2 style="color:{color};">Predicted Dropout Risk: {prediction:.1f}%</h2>
    <h3>{risk}</h3>
    <p>{msg}</p>
    </div>
    """, unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text':"Dropout Risk (%)"},
        gauge={
            'axis': {'range':[0,100]},
            'steps':[
                {'range':[0,30],'color':'lightgreen'},
                {'range':[30,60],'color':'khaki'},
                {'range':[60,100],'color':'lightcoral'}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    comparison = pd.DataFrame({
        "Feature":[
            "Stress","Anxiety","Depression",
            "Burnout","Financial Stress",
            "Family Expectation","Social Support"
        ],
        "Value":[
            stress_level, anxiety_score, depression_score,
            burnout_score, financial_stress,
            family_expectation, social_support
        ]
    })

    chart = px.bar(
        comparison,
        x="Feature",
        y="Value",
        title="Student Risk Factors"
    )

    st.plotly_chart(chart, use_container_width=True)

    st.subheader("Recommendations")

    if prediction < 30:
        st.success(msg)
    elif prediction < 60:
        st.warning(msg)
    else:
        st.error(msg)
