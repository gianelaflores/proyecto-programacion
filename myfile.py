import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

url ='https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv'
datos = pd.read_csv(url, sep=',')

st.title('LICENCIAMIENTO INSTITUCIONAL-SUNEDU')
st.header('DATA SUNEDU')
st.write('Analicemos los datos')
st.line_chart(data=datos, x='CODIGO_ENTIDAD', y='PERIODO_LICENCIAMIENTO')

urp='https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/MODIFICADA%20TABLA%20SUNEDU.csv'
datos2=pd.read_csv(urp,sep=',')



