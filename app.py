
import pickle
import pandas as pd
import streamlit as st

# Load the trained ML model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Predictor")
st.write(
    "Enter student details to estimate their final exam score "
    "using a Machine Learning model."
)

st.info(
    "This is a learning demo using a small synthetic dataset. "
    "Predictions are estimates, not guaranteed results."
)

# Input fields
st.subheader("Student Details")

study_hours = st.number_input(
    "Daily study hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

attendance = st.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

previous_score = st.slider(
    "Previous exam score",
    min_value=0,
    max_value=100,
    value=60
)

# Prediction button
if st.button("Predict Final Score", type="primary"):
    input_data = pd.DataFrame(
        [[study_hours, attendance, previous_score]],
        columns=["study_hours", "attendance", "previous_score"]
    )

    prediction = float(model.predict(input_data)[0])
    prediction = max(0.0, min(100.0, prediction))

    st.subheader("Prediction Result")
    st.metric("Estimated Final Score", f"{prediction:.1f} / 100")

    if prediction >= 75:
        st.success("Estimated score range: High")
    elif prediction >= 50:
        st.warning("Estimated score range: Moderate")
    else:
        st.error("Estimated score range: Low")

    st.caption(
        "This estimate is based on the patterns in the training data. "
        "Actual results may differ."
    )
