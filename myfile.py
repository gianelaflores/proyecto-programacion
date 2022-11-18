import streamlit as st
import pandas as pd
import numpy as np

st.title('SUNEDU')
st.subheader('Instituciones licenciadas')
url=https://github.com/gianelaflores/proyecto-programacion/blob/documentos/Licenciamiento%20Institucional_7.csv1
file=pd.read_csv(url, sep=',')
st.line_chart(data=file,x='Nombre de universidad', y='Periodo de licenciamiento')
