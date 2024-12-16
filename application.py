import streamlit as st

st.title('PRACTICE GITHUB MERGING')

st.text('helloooo')

b = st.button(label='Login')
if b:
    st.text('WELCOME TO THIS TUTORIAL')



st.sidebar.header("Filters")
age = st.sidebar.slider("Age", 18, 65, 25)
gender = st.sidebar.radio("Gender", ["Male", "Female", "Other"])



st.write(f"You selected: Age {age}, Gender {gender}")
