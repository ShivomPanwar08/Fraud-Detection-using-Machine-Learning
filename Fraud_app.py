import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction app")

st.markdown('Please enter the transaction details below to check if it is fraudulent or not.')
st.divider()


amount = st.number_input("Amount", min_value=0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value = 0.0)

tx_type = st.selectbox(
    "Transaction Type",
    ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT", "CASH_IN"]
)

if st.button("Check Fraud"):
    input_data = pd.DataFrame([{
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "type": tx_type
    }])

    prediction = model.predict(input_data)[0]


    if prediction == 1:
        st.error("FRAUD")
    else:
        st.success("NOT FRAUD")


