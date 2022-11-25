#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np

st.header("LICENCIAMIENTO INSTITUCIONAL")
@st.experimental_memo

def download_data():
   url="https://www.datosabiertos.gob.pe/sites/default/files/Licenciamiento%20Institucional_7.csv"
   filename="Licenciamiento%20Institucional_7.xlsx"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('Licenciamiento%20Institucional_7.xlsx')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

st.title('Universidades') 

#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/Gandy2704/programacion/documentos/Licenciamiento%20Institucional_7%20-%20Licenciamiento%20Institucional_7.csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='CODIGO_ENTIDAD', y='NOMBRE')
