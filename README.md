# 🎓 EduSight – Student Dropout Risk Prediction System

## 📌 Overview

EduSight is a Machine Learning-based web application designed to predict the risk of student dropout using mental health, academic, financial, and social factors.

The system analyzes student data and generates a dropout risk percentage (0–100%), helping educational institutions identify at-risk students and take early intervention measures.

---

## 🚀 Features

- Predicts student dropout risk in real time
- Interactive Streamlit web interface
- Risk categorization:
  - 🟢 Low Risk
  - 🟡 Moderate Risk
  - 🔴 High Risk
- Dynamic visualizations using Plotly
- Personalized recommendations based on predicted risk
- Model comparison and performance evaluation

---

## 📊 Dataset Information

- Total Records: **2,000 Students**
- Original Features: **20 Features**
- Selected Features for Prediction: **9 Features**

### Selected Features

1. Stress Level
2. Anxiety Score
3. Depression Score
4. Sleep Hours
5. Burnout Score
6. Academic Performance
7. Financial Stress
8. Family Expectation
9. Social Support

---

## 🧠 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Model Deployment

---

## 🤖 Models Implemented

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

---

## 📈 Model Performance

| Model | R² Score | MAE | RMSE |
|---------|---------|---------|---------|
| Linear Regression | 0.6338 | 6.5987 | 8.4200 |
| Random Forest | 0.6001 | 6.9087 | 8.7987 |
| XGBoost | 0.5800 | 7.0997 | 9.0180 |

### 🏆 Best Model: Linear Regression

- R² Score: **0.6338**
- MAE: **6.60**
- RMSE: **8.42**

The Linear Regression model achieved the highest performance and was selected for deployment.

---

## 🖥️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib
- Plotly

### Framework
- Streamlit

---

## 📷 Application Workflow

1. User enters student information.
2. Data is preprocessed and scaled.
3. Trained ML model predicts dropout risk.
4. Risk percentage is displayed.
5. Interactive charts visualize risk factors.
6. Recommendations are generated based on risk level.

---

## 📁 Project Structure
