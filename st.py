import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))
st.title('Salary Predection')
#defining object
EX=st.text_input('Enter your experience in years: ')

if st.button('Predict'):
    EX=float(EX)
    st.write("your predicted Salary is: ")
    data=[[EX]]
    result=model.predict(data)
    st.success(result)

    