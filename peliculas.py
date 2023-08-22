import streamlit as st
import pandas as pd
import numpy as np


@st.cache
def data(filas):
    df=pd.read_csv("movies.csv").head(filas)
    return df

def buscarfilm(filmes):
    dffiltrado = df[df['name'].str.upper().str.contains(filmes)]
    return dffiltrado

def buscarDirector

df = data(500)
sidebar = st.sidebar
sidebar.title("Películas")
st.title('Netfilx')

if st.sidebar.button('Buscar: '):
    dfBusqueda = buscarfilm(input.upper)

if sidebar.checkbox("Mostrar todos los filmes"):
    st.write(data(500))

input = st.sidebar.text_input('ingresa: ')

if st.sidebar.button('Buscar por nombre: '):
    dfBusqueda = buscarfilm(input.upper())
    st.write(dfBusqueda)

selectedBox = st.sidebar.selectbox('Seleccionar', df['director'])

if st.sidebar.button('')




