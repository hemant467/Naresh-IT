import streamlit as st 
import numpy as np 
import joblib
import sklearn 

MedInc=st.number_input('enter MedInc')
HouseAge=st.number_input('enter HouseAge')
AveRooms=st.number_input('enter AveRooms')
Population=st.number_input('enter Population')
AveOccup=st.number_input('enter AveOccup')
Latitude=st.number_input('enter Latitude')

location= 'california_model.joblib'
saved_model=joblib.load(location)
if st.button('predict'):
    Input=[MedInc,HouseAge,AveRooms,Population,AveOccup,Latitude]
    op=saved_model['model'].predict([Input])
    st.success(f"the Median house value is: {op}")

