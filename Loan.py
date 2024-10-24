import numpy as np
import streamlit as st
# import joblib  # pip install joblib
from sklearn.ensemble import RandomForestClassifier as rfc
import pandas as pd
import pickle
import joblib
st.set_page_config("Loan Approvel",page_icon=":credit_card:")
st.title("Loan Approvel ")
# 'loan_id', ' no_of_dependents', ' education', ' self_employed',
#        ' income_annum', ' loan_amount', ' loan_term', ' cibil_score',
#        ' residential_assets_value', ' commercial_assets_value',
#        ' luxury_assets_value', ' bank_asset_value', ' loan_status'

val1 = st.number_input("No of Dependents")
val2 = st.radio(label="Education",options=["Graduate","Not Graduate"])
val3 = st.radio(label="Do You have any job",options=["Yes","No"])
val4 = st.number_input("Annual Income", placeholder="Enter your Annual Income")
val5 = st.number_input("Loan Amount", placeholder="Enter the Loan Amount")
val6 = st.number_input("Loan Term", placeholder="Enter the Loan Amount")
val7 = st.number_input("Cibil Score", placeholder="Enter Your Cibil Score")
val8 = st.number_input("Resident Asset", placeholder="Enter Your Resident Asset Value")
val9 = st.number_input("Commercial Asset", placeholder="Enter Your Commercial Asset Value")
val10 = st.number_input("Luxury Asset", placeholder="Enter Your Luxury Asset Value")
val11 = st.number_input("Bank Asset", placeholder="Enter Your Bank Asset Value")
val2 = 1 if val2 == 'Graduate' else 0
val3 = 1 if val3 == 'Yes' else 0
# df=pd.read_csv("loan_approval_dataset.csv")
from sklearn.ensemble import RandomForestClassifier as rfc
model=joblib.load('Loan.pkl')
with open('Loan.pkl', 'rb') as file:
    model1 = pickle.load(file)
if st.button("Check Loan status"):
    features=[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11]
    prediction=model.predict([features])
    st.write(f"Loan: {prediction[-1]}") 
    # if prediction[-1]=="	Approved":
    #     st.success("Loan Approved!")
    # else:
    #     st.error("Loan Denied")