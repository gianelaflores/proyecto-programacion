import streamlit as st
import pandas as pd

#titulo del app
st.title("DATA SUNEDU")

#add s sidebar
st.sidebar.subheader("visualizacion de configuraciones")

#setup file upload
uploaded_file=st.sidebar.file_uploader(label="upload your CSV or Excel file",
                         type=["csv","xlsx"])
global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")
    
    try:
       df=pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df=pd.read_excel(uploaded_file)
st.write(df)

import numpy as np
from datetime import time
import datetime 
#hora
appointment = st.slider("Programe la asesoria:",value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)

#fechas
d = st.date_input("Fecha",datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

#coordenadas
f = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
#titulo (aqui inicia)
st.title('SUNEDU')
st.subheader('Instituciones licenciadas')
url='https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv'
file=pd.read_csv(url, sep=',')
st.line_chart(data=file,x='CODIGO_ENTIDAD', y='PERIODO_LICENCIAMIENTO')
st.subheader('Tabla de datos')
