import streamlit as st
import numpy as np
import pandas as pd
import pickle

# load model here
model = pickle.load(open('model.pkl','rb'))

# creating web app using streamlit
st.title("Concrete Age Prediction In Days")
Cement = st.text_input("Enter Cement Value")
Water = st.text_input("Enter Water Level")
Strength = st.text_input("Enter Strength value")
features = np.array([[Cement,Water,Strength]])

prediction = model.predict(features).reshape(1,-1)

if st.button("Get Age"):
    st.write("Concrete Age in Days is :", prediction[0])
