#import streamlit and pandas
import streamlit as st 
import pandas as pd 

myname = st.text_input('nombre:')

if (myname):
    st.write(f"tu nombre es: {myname}")
