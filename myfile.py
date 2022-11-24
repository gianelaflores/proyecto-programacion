import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
#hora
appointment = st.slider("Programe la asesoria:",value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)

#fechas
d = st.date_input("Fecha de cumpleaños",datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)

st.title('SUNEDU')
st.subheader('Instituciones licenciadas')
url='https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv'
file=pd.read_csv(url, sep=',')
st.line_chart(data=file,x='CODIGO_ENTIDAD', y='PERIODO_LICENCIAMIENTO')
st.subheader('Tabla de datos')
st.table(data=file,columns=('CODIGO_ENTIDAD','NOMBRE'))
