import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title('Financial Inclusion Prediction')
st.write('Predict whether an individual has a bank account or not.')

# Input fields for all features
st.subheader("Enter the Feature Values:")

# Numeric features
age_of_respondent = st.number_input('Age of Respondent', min_value=0, max_value=120)
household_size = st.number_input('Household Size', min_value=1, max_value=50)
year = st.number_input('Year', min_value=2000, max_value=2030)

# Categorical features (binary and one-hot encoded)
gender_of_respondent_Male = st.selectbox('Gender', ['Female', 'Male'])
cellphone_access_Yes = st.selectbox('Cellphone Access', ['No', 'Yes'])
location_type_Urban = st.selectbox('Location Type', ['Rural', 'Urban'])

# Job Type Grouped
job_type = st.selectbox('Job Type', [
    'Formally employed', 'Self employed', 'Informally employed',
    'Low Income/Dependent', 'Other'
])

# Education Level
education_level = st.selectbox('Education Level', [
    'No formal education', 'Primary education', 'Secondary education',
    'Tertiary education', 'Vocational/Specialised training', 
    'Other/Dont know/RTA'
])

# Marital Status
marital_status = st.selectbox('Marital Status', [
    'Single/Never Married', 'Married/Living together', 'Widowed',
    'Dont know'
])

# Relationship with Head
relationship_with_head = st.selectbox('Relationship with Head', [
    'Head of Household', 'Spouse', 'Parent', 'Other relative', 'Other non-relatives'
])

# Country
country = st.selectbox('Country', ['Uganda', 'Tanzania', 'Rwanda'])

# Feature transformation (convert categorical inputs into binary features)
def process_input():
    features = {
        'remainder__age_of_respondent': age_of_respondent,
        'age_of_respondent': age_of_respondent,
        'household_size': household_size,
        'remainder__household_size': household_size,
        'job_type_grouped_Formally employed': int(job_type == 'Formally employed'),
        'education_level_Tertiary education': int(education_level == 'Tertiary education'),
        'location_type_Urban': int(location_type_Urban == 'Urban'),
        'education_level_Vocational/Specialised training': int(education_level == 'Vocational/Specialised training'),
        'cellphone_access_Yes': int(cellphone_access_Yes == 'Yes'),
        'education_level_Secondary education': int(education_level == 'Secondary education'),
        'education_level_Primary education': int(education_level == 'Primary education'),
        'gender_of_respondent_Male': int(gender_of_respondent_Male == 'Male'),
        'job_type_grouped_Self employed': int(job_type == 'Self employed'),
        'year': year,
        'relationship_with_head_Head of Household': int(relationship_with_head == 'Head of Household'),
        'job_type_grouped_Informally employed': int(job_type == 'Informally employed'),
        'marital_status_Married/Living together': int(marital_status == 'Married/Living together'),
        'remainder__year': year,
        'marital_status_Single/Never Married': int(marital_status == 'Single/Never Married'),
        'job_type_grouped_Low Income/Dependent': int(job_type == 'Low Income/Dependent'),
        'country_Uganda': int(country == 'Uganda'),
        'job_type_grouped_Other': int(job_type == 'Other'),
        'country_Tanzania': int(country == 'Tanzania'),
        'relationship_with_head_Spouse': int(relationship_with_head == 'Spouse'),
        'marital_status_Widowed': int(marital_status == 'Widowed'),
        'country_Rwanda': int(country == 'Rwanda'),
        'relationship_with_head_Other relative': int(relationship_with_head == 'Other relative'),
        'relationship_with_head_Parent': int(relationship_with_head == 'Parent'),
        'relationship_with_head_Other non-relatives': int(relationship_with_head == 'Other non-relatives'),
        'education_level_Other/Dont know/RTA': int(education_level == 'Other/Dont know/RTA'),
        'marital_status_Dont know': int(marital_status == 'Dont know'),
    }
    return np.array([list(features.values())])

# Prediction
if st.button('Predict'):
    input_features = process_input()
    prediction = model.predict(input_features)

    # Display result in human-readable form
    if prediction[0] == 1:
        st.success('Prediction: The individual **HAS a bank account**.')
    else:
        st.error('Prediction: The individual **DOES NOT HAVE a bank account**.')
