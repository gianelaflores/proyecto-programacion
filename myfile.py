import streamlit as st
import pandas as pd
import numpy as np

st.title('SUNEDU')
st.subheader('Instituciones licenciadas')
url='https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv'
file=pd.read_csv(url, sep=',')
st.line_chart(data=file,x='CODIGO_ENTIDAD', y='PERIODO_LICENCIAMIENTO')
st.subheader('Tabla de datos')

st.table(data=file, 'CODIGO_ENTIDAD', 'NOMBRE')
df = pd.DataFrame(data=file,columns=('col %d' % i for i in range(2)))
st.table(df)
