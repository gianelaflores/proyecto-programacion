#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image
#----------------------------------------------------------------------------------------------------------------------------------  

#------------------------------------------------------------------------------------------------------------------------------------------------
#MENU
st.set_page_config(layout="wide", initial_sidebar_state='expanded')
with open('logo.css') as f: 
    st.markdown(f'<style>{f.read()}</logo>',unsafe_allow_html=True)
with st.sidebar:
    st.markdown('###')
    st.sidebar.header ('Programación') 
    selected= option_menu(
        menu_title='Menú',
        options=['Inicio','Equipo','Analisis','Mapa'],
        icons=['house','person','book','book'],
        menu_icon='cast',
        default_index= 0,
    )
    
#--------------------------------------------------------------------------------------------------------------------------------
#introduccion
if selected == 'Inicio':
    st.markdown("<h1 style ='text-align: center'>LICENCIAMIENTO INSTITUCIONAL</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("¿Que es SUNEDU?")
    st.write("La Superintendencia Nacional de Educación Superior Universitaria (SUNEDU) es el organismo público adscrito al Ministerio de Educación, que garantiza una oferta educativa de calidad en favor de los estudiantes, a través del licenciamiento y supervisión, con eficiencia, predictibilidad, transparencia y respeto a la autonomía universitaria.")
    video_file = open('video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.subheader("¿Que es el licenciamiento institucional?")
    st.write("Es un procedimiento obligatorio para todas las universidades del país, a través del cual cada casa de estudios debe demostrar ante la SUNEDU que cumple con las Condiciones Básicas de Calidad (CBC) para poder brindar el servicio educativo.")
    image = Image.open('sunedu.jpeg')
    st.image(image)
    
    st.subheader("Condiciones básicas de calidad en la universidad peruana ")
    st.write("Las universidades para poder conseguir la autorización, deberán cumplir con seis condiciones básicas de calidad:")
    st.write("Condición I: Modelo educativo")
    st.write("Condición II: Constitución, gobierno y gestión de la universidad")
    st.write("Condición III: La oferta educativa propuesta es coherente con sus planes de estudio y con los recursos de la universidad, además de ser sostenible")
    st.write("Condición IV: Propuesta en investigación")
    st.write("Condición V: Responsabilidad social universitaria y bienestar universitario")
    st.write("Condición VI: Transparencia")
    st.write("Estas condiciones básicas de calidad han sido determinadas con la finalidad de que las universidades nuevas cuenten con una propuesta humanística, científica y tecnológica orientada a la investigación Teniendo como pilar el desarrollo de la docencia universitaria que cuenten con los recursos económicos y financieros que aseguran su sostenibilidad y sean conducidas por personas que tienen la legitimidad e idoneidad técnica y moral.")
    
    st.subheader("Proceso de licenciamiento institucional")
    image = Image.open('proceso.jpeg')
    st.image(image)
    @st.experimental_memo

#---------------------------------------------------------------------------------------------------------------------------------
if selected == "Equipo":
    image = Image.open('equipo.png')
    st.image(image)
    
#-------------------------------------------------------------------------------------------------------------------------------------    
if selected == 'Analisis':
    st.header("Dataset")
    st.write("En esta seccion podrá visalizar el análisis y organizacion de los datos (SUNEDU) en diferentes graficos para su mayor compresion")
    def download_data():
        url ="https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv"
        filename ="Licenciamiento%20Institucional_7.csv"
        urllib.request.urlretrieve(url,filename)
        df_cat = pd.read_csv('Licenciamiento%20Institucional_7.csv') 
        return df_cat
download_data()
st.dataframe(download_data())
     #grafico circulo
    df = pd.read_csv('Licenciamiento%20Institucional_7.csv')        
    pie_chart = df.TIPO_GESTION.value_counts()
    pie_chart = pd.DataFrame(pie_chart)
    pie_chart = pie_chart.reset_index()
    pie_chart.columns = ['TIPO_GESTION','TOTAL']
    fig2, ax2 = plt.subplots()
    ax2.pie(pie_chart['TOTAL'], labels = pie_chart['TIPO_GESTION'], autopct='%1.1f%%')
    ax2.axis('equal')
    st.write('Gráfico')
    st.pyplot(fig2)
#-----------------------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------
df_otorgada = pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/otorgadas.csv')
df_denegada = pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/nolicenciadas.csv')
df_io = pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/notificado.csv')
df_ninguno = pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/ninguno.csv')
#-------------------------------------------------------------------------------------------------------------------------------------

if selected=="Mapa":
    dataset = st.selectbox('Seleccione una opción:',('Licenciadas','No Licenciadas','Con informe de observaciones/notificado','Ninguno'))
    #option = '-'
    if dataset == 'Licenciadas':
        option = 'Licencia otorgada'
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
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_otorgada)  
        n=len(df_otorgada.axes[0])
        
    elif dataset == 'No Licenciadas':
        option = 'Licencia denegada'
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
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_denegada)
        n=len(df_denegada.axes[0])
        
    elif dataset == 'Con informe de observaciones/notificado':
        option = 'informe de observaciones (IO) notificado'
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
        
    elif dataset == 'Ninguno':
        option = 'ningún estado de licenciamiento'
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
    st.write('Se encontraron', n,'registros de universidades para su búsqueda.')
    


        
                                             
            
            
            
            
            
        
    
