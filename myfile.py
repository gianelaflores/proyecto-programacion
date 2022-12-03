#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image



st.set_page_config(layout="wide", initial_sidebar_state='expanded')
with open('logo.css') as f: 
    st.markdown(f'<style>{f.read()}</logo>',unsafe_allow_html=True)
with st.sidebar:
    st.markdown('###')
    st.sidebar.header ('Programación') 
    selected= option_menu(
        menu_title='Menú',
        options=['Inicio','Equipo','Analisis','reporte'],
        icons=['house','person','book','book'],
        menu_icon='cast',
        default_index= 0,
    )
    
#--
if selected == 'Inicio':
    st.markdown("<h1 style ='text-align: center'>Licenciamiento de instituciones</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("colocar info")
    st.header("Dataset")
    @st.experimental_memo
    def download_data():
        url ="https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv"
        filename ="Licenciamiento%20Institucional_7.csv"
        urllib.request.urlretrieve(url,filename)
        df_cat = pd.read_csv('Licenciamiento%20Institucional_7.csv') 
        return df_cat
    download_data()
    st.dataframe(download_data())

#--
if selected == 'Equipo':
    image = Image.open('amigos.jpg')
    st.image(image) 
    
#---------------------------------------    
df_otorgada = pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/otorgadas.csv')
df_denegada=pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/otorgadas.csv')
df_io=pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/otorgadas.csv')
df_ninguno=pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/otorgadas.csv')

#--------------------------------------------
if selected == 'Analisis':
    dataset = st.selectbox(
        'Seleccione una opción:LICENCIA...',
        ('otorgada','no otorgada','Con informe de observaciones (IO) notificado','Ninguno')
        )
    #option = '-'
    if dataset == 'licenciada':
        option = 'otorgada'
        st.write('*Gráfico')
        @st.cache
        def otorgada_data():
            df_otorgada = pd.read_csv('otorgadas.csv')
            df_otorgada = df_otorgada.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_otorgada
        data = otorgada_data()
        st.map(data)        
        #st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        #st.dataframe(df_otorgada)  
        
      if dataset == 'no licenciada':
        option = 'no otorgada'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def denegada_data():
            df_denegada = pd.read_csv('nolicenciadas.csv')
            df_denegada = df_denegada.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_denegada
        data = denegada_data()
        st.map(data)
       # st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
       # st.dataframe(df_denegada)
       # n = len(df_denegada.axes[0])
      if dataset == 'Con informe de observaciones (IO) notificado':
        #option = 'informe de observaciones (IO) notificado'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def io_data():
            df_io = pd.read_csv('notificado.csv')
            df_io = df_io.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_io
        data = io_data()
        st.map(data)
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_io)
        n = len(df_io.axes[0])
        
      if dataset == 'Ninguno':
        #option = 'ningún estado de licenciamiento'
        st.markdown("###")
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        @st.cache
        def ninguno_data():
            df_ninguno = pd.read_csv('ninguno.csv')
            df_ninguno = df_ninguno.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
            return df_ninguno
        data = ninguno_data()
        st.map(data)
        
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_ninguno)
        n = len(df_ninguno.axes[0])
     
    st.write('Se encontraron', n,'registros de universidades para esta busqueda')

        
        #grafico lineas
        urp='https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv'
        datos=pd.read_csv(urp,sep=',')
        st.line_chart(data=datos,x='CODIGO_ENTIDAD',y='PERIODO_LICENCIAMIENTO')
        
         def download_data():
        url ="https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/MODIFICADA%20TABLA%20SUNEDU.csv"
        filename ="MODIFICADA%20TABLA%20SUNEDU.csv"
        urllib.request.urlretrieve(url,filename)
        df_cat = pd.read_csv('MODIFICADA%20TABLA%20SUNEDU.csv') 
        return df_cat
    download_data()
    st.dataframe(download_data())
        
        #grafico circulo
        df = pd.read_csv('Licenciamiento%20Institucional_7.csv')        
        pie_chart = df.ESTADO_LICENCIAMIENTO.value_counts()
        pie_chart = pd.DataFrame(pie_chart)
        pie_chart = pie_chart.reset_index()
        pie_chart.columns = ['ESTADO_LICENCIAMIENTO','TOTAL']
        fig1, ax1 = plt.subplots()
        ax1.pie(pie_chart['TOTAL'], labels = pie_chart['ESTADO_LICENCIAMIENTO'], autopct='%1.1f%%')
        ax1.axis('equal')
        st.write('Gráfico')
        st.pyplot(fig1)

        
                                             
            
            
            
            
            
        
    
