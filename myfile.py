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

st.header('tABLA DE ANALISIS')
st.write('ANALICEMOS RANGOS')
st.line_chart(data=datos, x='PERIODO_LICENCIAMIENTO', y=['Price', 'High', 'Low'])


st.header('Ejemplo de mapa')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['LATITUD', 'LONGITUD'])
st.map(df)

st.header('tabla de datos')
st.table(df.head(5))

st.header('Ejemplo de dataframe')
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['LATITUD', 'LONGITUD'])

st.header('AÑO DE LICENCIAMIENTO')
periodo = st.slider('Seleccionar un año', 2014, 2022, 2014, 1)
st.write("MosTRANDO CODIGO IDENTIDAD DE UNIVERSIDADES", periodo)
# acá se actualiza el periodo desde el archivo datos (filtrar con lo visto en la unidad 2)


st.header('Ejemplo de mapa')
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=5,
        pitch=70,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[LONGITUD ,LATITUD]',
           radius=200, #acumula los valores
           elevation_scale=4, #da una escala de 0 a 4
           elevation_range=[0, 1000], # total de posibles valores
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[LONGITUD,LATITUD]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))


    



