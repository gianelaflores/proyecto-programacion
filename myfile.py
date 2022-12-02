import streamlit as st
import pandas as pd

#titulo del app
st.title("LICENCIAMIENTO INSTITUCIONAL DE LAS UNIVERSIDADES PERUANAS")
st.subheader("DATA SENEDU")
st.write("!Bienvenido¡")
st.write("Les presentamos nuestra plataforma con los datos organizados de SENEDU, para su mejor compresion y visualizacion")

#add s sidebar
st.sidebar.subheader("visualizacion de configuraciones")

#setup file upload
uploaded_file=st.sidebar.file_uploader(label="subir tu CVS o archivo excel",
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

global numeric_columns
try:
    st.write(df)
    numeric_columns=list (df.select_dtypes(["float","int"]).columns)
except Exception as e:
    print(e)
    st.write("porfavor subir archivopara la aplicacion")
#agregar a seleccion de barra
chart_select= st.sidebar.selectbox( label="seleccionar el tipo grafico" ,
                                      options= ["histograma", "grafico de intervalos"])

if chart_select=="histograma":
    st.sidebar.subheader("histograma configuraciones")
    try:
      x_valores=st.sidebar.selectbox("X axis",options=[numeric_columns])
      y_valores=st.sidebar.selectbox("Y axis",options=[numeric_columns])
    except Exception as e :
        print(e)        
