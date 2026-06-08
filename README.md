# 🎓 EduSight: Student Dropout Risk Prediction System

Edusight is an end-to-end Machine Learning web application built using **Streamlit** that predicts a student's **Dropout Risk Percentage (0-100%)**. The system utilizes a combination of **Mental Health indicators, Academic Performance, and Socio-Economic factors** to identify vulnerable students early and provide actionable administrative recommendations.

---

## 🚀 Key Features

* **Three-Core Input Assessment**: Organizes student metrics into logical input categories via an interactive sidebar/form layout:
  * *Psychological Metrics*: Stress Levels, Anxiety, Depression, and Burnout.
  * *Academic Indicators*: Sleep Hours and Academic Performance (%).
  * *Social Environment*: Financial Stress, Family Expectations, and Social Support networks.
* **Real-time Predictive Analytics**: Processes inputs through a pre-trained feature scaler and machine learning regression engine to provide instant risk estimates.
* **Interactive Data Visualizations**:
  * An intuitive **Gauge Chart** illustrating the exact risk tier (Low, Moderate, High).
  * A dynamic **Factor Breakdown Bar Chart** displaying the student's primary risk exposures for rapid diagnostic review.
* **Automated Support Alerts**: Generates contextual warning flags and distinct action plans based on critical score boundaries.

---

## 📊 System Feature Matrix

The prediction model calculates risk scores using the following 9 operational features:

| Feature Name | Interface Label | Range | Description |
| :--- | :--- | :--- | :--- |
| `stress_level` | Stress Level | 0.0 – 10.0 | Self-reported scale of daily psychological stress. |
| `anxiety_score` | Anxiety Score | 0.0 – 10.0 | Standardized assessment score for anxiety symptoms. |
| `depression_score` | Depression Score | 0.0 – 10.0 | Standardized tracking index for depressive indicators. |
| `sleep_hours` | Sleep Hours | 0.0 – 12.0 | Average duration of sleep captured per night. |
| `burnout_score` | Burnout Score | 0.0 – 10.0 | Calculated burnout index relating to institutional workload. |
| `academic_performance` | Academic Performance (%) | 0.0% – 100.0% | Cumulative percentage representing academic standing. |
| `financial_stress` | Financial Stress | 0.0 – 10.0 | Perceived level of external financial hardship or strain. |
| `family_expectation` | Family Expectation | 0.0 – 10.0 | Perceived degree of familial academic pressure. |
| `social_support` | Social Support | 0.0 – 10.0 | Strength of accessible peer and mentor support networks. |

---

## 🧭 Risk Threshold Matrix & Interventions

Calculated risk percentages map directly to specific severity tiers and recommendation workflows:

| Risk Score | Tier Classification | UI Alert Style | System Recommendation & Guidelines |
| :--- | :--- | :--- | :--- |
| **< 30.0%** | **LOW RISK** 🟢 | Green Border / Success | Student appears stable. Continue monitoring routine indicators. |
| **30.0% - 59.9%** | **MODERATE RISK** 🟡 | Yellow Border / Warning | Consider early intervention strategies and support services. |
| **≥ 60.0%** | **HIGH RISK** 🔴 | Red Border / Error | Urgent intervention needed. Recommend counseling and academic support. |

---

## 📂 Project Architecture

Ensure your workspace directory tree is structured exactly as follows for the app to successfully read the pipeline artifacts:

```text
.
├── app.py                     # Main Streamlit web application script
├── dropout_risk_model.pkl     # Pre-trained serialized Machine Learning model
└── feature_scaler.pkl         # Pre-trained serialized MinMaxScaler/StandardScaler artifact<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/4a71de12-d9e4-447b-9445-444bf03695a0" />
