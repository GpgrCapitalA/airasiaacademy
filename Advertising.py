import streamlit as st
import pandas as pd
import pickle

st.write("""
# Advertising Sales Prediction App

This app predicts the **Sales of Media Medium** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 4.3, 7.9, 5.4)
    Radio = st.sidebar.slider('Radio', 2.0, 4.4, 3.4)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 6.9, 1.3)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("AdvertisingLinearRegression.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Sales Prediction')
st.write(prediction[0])
