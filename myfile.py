import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk

url = 'https://raw.githubusercontent.com/PeterTXS09/streamlit_demo/main/USD_PEN%20Historical%20Data2.csv'
datos = pd.read_csv(url, sep=',')

st.title('Precio del dólar')
st.header('Precio del dólar a lo largo del tiempo')
st.write('Analicemos el precio del dólar a lo largo del perido')
st.line_chart(data=datos, x='Date', y='Price')

st.header('Precio del dólar en el día - valor más alto y bajo')
st.write('Analicemos el precio del dólar a lo largo del perido establecido vs el valor más alto y más bajo')
st.line_chart(data=datos, x='Date', y=['Price', 'High', 'Low'])


st.header('Ejemplo de mapa')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

st.header('tabla de datos')
st.table(df.head(5))

st.header('Ejemplo de dataframe')
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.header('Precio del dolar por año')
periodo = st.slider('Seleccionar un año', 2014, 2022, 2014, 1)
st.write("Mostrando precio del dolar en el periodo", periodo)
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
           get_position='[lon, lat]',
           radius=200, #acumula los valores
           elevation_scale=4, #da una escala de 0 a 4
           elevation_range=[0, 1000], # total de posibles valores
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

    



