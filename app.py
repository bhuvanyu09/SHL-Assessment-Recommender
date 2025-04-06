import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("shl_model.ipynb")

st.title("🔍 SHL Assessment Recommendation Engine")

# Input form
job_role = st.selectbox("Job Role", [
    'Software Engineer', 'Sales Manager', 'Data Analyst', 'HR Executive',
    'Marketing Manager', 'Business Analyst', 'Customer Support',
    'Product Manager', 'Finance Associate', 'UX Designer'
])

experience_years = st.slider("Years of Experience", 0, 20, 2)

skill_level = st.selectbox("Skill Level", ['Low', 'Medium', 'High'])
education_level = st.selectbox("Education Level", ['High School', 'Bachelors', 'Masters'])
industry = st.selectbox("Industry", ['Technology', 'Finance', 'HR', 'Marketing', 'Customer Service', 'Design'])
region = st.selectbox("Region", ['North America', 'Europe', 'Asia', 'Australia'])

if st.button("Recommend Assessment"):
    input_data = pd.DataFrame([{
        'job_role': job_role,
        'experience_years': experience_years,
        'skill_level': skill_level,
        'education_level': education_level,
        'industry': industry,
        'region': region
    }])

    # Categorical encoding if necessary (assumes model pipeline handles it)
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Assessment: {prediction}")