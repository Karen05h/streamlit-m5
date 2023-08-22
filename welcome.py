#import streamlit and pandas
import streamlit as st 
import pandas as pd 

def bienvenida(nombre) :
    mymensaje = 'bienvenido/a: ' + nombre
    return mymensaje

myname = st.text_input('nombre:')

if (myname):
    mensaje = bienvenida(myname)
    st.write(f"{mensaje}")
