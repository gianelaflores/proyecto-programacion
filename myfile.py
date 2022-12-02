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

#mapa
st.header(' Mapa')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['LATITUD', 'LONGITUD'])
st.map(df)



