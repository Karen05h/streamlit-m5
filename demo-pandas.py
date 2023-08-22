#import streamlit
import streamlit as st
import pandas as pd

st.title('Karen Zayde Hurtado Romero')
st.header('App demo de Streamlit')
st.write('hola mundo de streamlit usando codespaces de github')

name_link = 'dataset.csv'
#read csv
names_data = pd.read_csv(name_link)

#create title
st.title('Streamlit and pandas')

#print data frame
st.dataframe(names_data)