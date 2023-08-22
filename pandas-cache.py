#import streamlit and pandas
import streamlit as st 
import pandas as pd 

#print title
st.title('Streamlit con cache')
st.header('Información de primeros 1,000')
#set dataset url
DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    #create dataframe data, con n rows
    data = pd.read_csv(DATA_URL, nrows=nrows)
    #return dataframe
    return data

#print text loading data...
data_load_state = st.text('Loading data...')
#call function load_data, aparte le decimos que sólo queremos mil registros
data = load_data(1001)
#print text done
data_load_state.text("Done!")

#print dataframe
st.dataframe(data)