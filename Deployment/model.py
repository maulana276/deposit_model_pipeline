import streamlit as st
import pandas as pd
import numpy as np
import pickle

def run():
    with open('full_process.pkl', 'rb') as file_1:
        full_process = pickle.load(file_1)


    # input data widget
    age = st.number_input(label='Please enter your age', min_value=18)
    job = st.radio(label='Please enter your occupation', options=['blue-collar', 'management', 'technician', 'admin.', 'services', 'retired', 'self-employed', 'entrepreneur', 'unemployed', 'housemaid', 'student', 'unknown'], index=1)
    education = st.radio(label='Please enter your education background', options=['primary', 'secondary', 'tertiary', 'unknown'], index=1)
    balance = st.number_input(label='Please enter your balance amount')
    housing = st.radio(label='Do you have a housing loan?', options=['Yes', 'No'])
    if housing == 'Yes':
        housing = 1
    else:
        housing = 0

    loan = st.radio(label='Do you have an ongoing personal loan?', options=['Yes', 'No'])
    if loan == 'Yes':
        loan = 1
    else:
        loan = 0

    duration = st.number_input(label='Please input last contact duration')
    pdays = st.number_input(label='Please input number of days since last contact')
    poutcome = st.radio(label='Please select the outcome of last campaign', options=['unknown', 'failure', 'other', 'success'], index=1)

    # make the dataframe
    data_inf = pd.DataFrame({
            'age' : [age],
            'job' : [job],
            'education' : [education],
            'balance' : [balance],
            'housing' : [housing],
            'loan' : [loan],
            'duration' : [duration],
            'pdays' : [pdays],
            'poutcome' : [poutcome],
            }, index = [0]) #index = 0 karena listnya cuma ada satu
    st.table(data_inf)


    if st.button(label='predict'):
        
            # Melakukan prediksi data dummy
            y_pred_inf = full_process.predict(data_inf)

            st.write(y_pred_inf[0])

            if y_pred_inf[0] == 0:
                st.write('Nasabah kemungkinan tidak akan berlangganan deposito')

            else:
                st.write('Nasabah kemungkinan akan berlangganan deposito')
