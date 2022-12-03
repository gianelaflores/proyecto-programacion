#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image 

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
if selected =="Inicio":
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
    
    
    st.subheader("INFORMACION DE DATASET")
    st.write("Finalmente, para mayor informacion sobre el data set que se analizara puede ingresar al siguiente link :")
    st.write("https://www.datosabiertos.gob.pe/dataset/sunedu-licenciamiento-institucional")
#--------------------------------------------------------------------------------------------------------------------------------------
if selected=="Equipo" :
    image = Image.open('equipo.png')
    st.image(image)  
#-------------------------------------------------------------------------------------------------------------------------------------    
if selected == "Analisis":
    st.header("Dataset")
    st.write("En esta seccion podrá visalizar el análisis y organizacion de los datos (SUNEDU) en diferentes graficos para su mayor compresión:")
    @st.experimental_memo
    def download_data():
        url ="https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/Licenciamiento%20Institucional_7.csv"
        filename ="Licenciamiento%20Institucional_7.csv"
        urllib.request.urlretrieve(url,filename)
        df_cat = pd.read_csv('Licenciamiento%20Institucional_7.csv') 
        return df_cat
    download_data()
    st.dataframe(download_data())
    st.subheader("GRÁFICO 1: UNIVERSIDADES PUBLICAS Y PRIVADAS") 
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
#--------------------------------------------------------------------------------------------------------------------------------------
#BARRAS POR DEPARTAMENTO
    st.markdown("###") 
    st.header('GRÁFICO 2: UNIVERSIDADES EXISTENTES POR DEPARTAMENTO')
    df = pd.read_csv('Licenciamiento%20Institucional_7.csv')
    df_dep = pd.DataFrame(df["DEPARTAMENTO"].value_counts())
    st.bar_chart(df_dep)
#----------------------------------------------------------------------------------------------------------------------------------------
#BARRAS POR PROVINCIA
    st.markdown("###") 
    st.header('GRÁFICO 3: UNIVERSIDADES EXISTENTES POR PROVINCIA')
    df = pd.read_csv('Licenciamiento%20Institucional_7.csv')
    df_pro = pd.DataFrame(df["PROVINCIA"].value_counts())
    st.bar_chart(df_pro)
#------------------------------------------------------------------------------------------------------
#BARRAS POR DISTRITO
    st.markdown("###") 
    st.header('GRÁFICO 4: UNIVERSIDADES EXISTENTES POR DISTRITO')
    df = pd.read_csv('Licenciamiento%20Institucional_7.csv')
    df_dist = pd.DataFrame(df["DISTRITO"].value_counts())
    st.bar_chart(df_dist)
#------------------------------------------------------------------------------------------------------------------------------

    
    
#------------------------------------------------------------------------------------------------------------------------------------------------
    
    st.write('**A continuación, seleccione una zona geográfica para visualizar el registro de universidades.**')
    st.markdown("###")
    df = pd.read_csv('Licenciamiento%20Institucional_7.csv')
    df = df.drop(columns = ["CODIGO_ENTIDAD","NOMBRE","FECHA_INICIO_LICENCIAMIENTO","FECHA_FIN_LICENCIAMIENTO","LATITUD","LONGITUD","UBIGEO","FECHA_CORTE"])
    
    set1 = np.sort(df['DEPARTAMENTO'].dropna().unique())
    sel1 = st.selectbox('Seleccione un departamento:', set1)
    df_DEPARTAMENTO = df[df['DEPARTAMENTO'] == sel1]
    n = len(df_DEPARTAMENTO.axes[0])

    set2 = np.sort(df_DEPARTAMENTO['PROVINCIA'].dropna().unique())
    sel2 = st.selectbox('Seleccione una provincia:', set2)
    df_PROVINCIA = df_DEPARTAMENTO[df_DEPARTAMENTO['PROVINCIA'] == sel2]
    n = len(df_PROVINCIA.axes[0]) 
    
    set3 = np.sort(df_DEPARTAMENTO['DISTRITO'].dropna().unique())
    sel3 = st.selectbox('Seleccione un distrito:', set3)
    df_DISTRITO = df_DEPARTAMENTO[df_DEPARTAMENTO['DISTRITO'] == sel3]
    n = len(df_DISTRITO.axes[0])
    st.write('Se encontraron', n,'registros de universidades para su búsqueda.')
    
    st.markdown("###")
    pie_chart = df_DISTRITO.ESTADO_LICENCIAMIENTO.value_counts()
    pie_chart = pd.DataFrame(pie_chart)
    pie_chart = pie_chart.reset_index()
    pie_chart.columns = ['ESTADO_LICENCIAMIENTO','TOTAL']
    fig1, ax1 = plt.subplots()
    ax1.pie(pie_chart['TOTAL'], labels = pie_chart['ESTADO_LICENCIAMIENTO'], autopct='%1.1f%%')
    ax1.axis('equal')
    st.write('**Gráfico 4.1. Estado de Licenciamiento (en %) de las universidades según zona geográfica seleccionada.**')
    st.markdown("###")
    st.pyplot(fig1)
    
#--------------------------------------------------------------------------------------------------------------------    
    st.markdown("###")
    st.hearder('GRÁFICO 5:PERIODO DE LICENCIAMIENTO-UNIVERSIDAD')
    st.write("El seguiente grafico ,presenta el periodo de licenciamiento para cada universidad.Cada universidad se encuentra identificada con un código (CODIGO DE IDENTIDAD).En la parte inferior encontrará una tabla con el código perteneciente a cada universidad.")
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
if selected== "Mapa":
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
    


        
                                             
            
            
            
            
            
        
    
