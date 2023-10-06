import streamlit as st
import model, eda

page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'EDA', 'Model'])

if page == 'Home Page':
    st.header('Selamat Datang di Home Page')
    st.subheader('Milestone 2', divider='blue')
    st.write('Nama      : Maulana Muhamad Priadhi')
    st.write('Batch     : HCK-007')
    st.write('Membuat model supervised learning untuk memprediksi nasabah berlanganan deposito pada bank')
    st.write('Silakan pilih Page di sebelah kanan! 😁')
    st.write('⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️⬅️')

elif page == 'EDA':
    eda.run()
else:
    model.run()