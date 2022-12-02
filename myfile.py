#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import urllib.request
#import matplotlib.pyplot as plt


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
df_otorgada = pd.read_csv('https://raw.githubusercontent.com/gianelaflores/proyecto-programacion/documentos/otorgadas.csv')    
if selected == 'Analisis':
    dataset = st.selectbox(
        'Seleccione una opción:',
        ('Licencia otorgada','Licencia denegada','Con informe de observaciones (IO) notificado','Ninguno')
        )
    option = '-'
    if dataset == 'Licencia otorgada':
        option = 'licencia otorgada'
        st.write('**Gráfico 3. Universidades con '+option+' localizadas en un mapa interactivo mundial.**')
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
        st.markdown("###")
        st.write('**Lista de universidades con '+option+' localizadas en un mapa interactivo mundial.**')
        st.dataframe(df_otorgada)
        n = len(df_otorgada.axes[0]) 
        
                                             
            
            
            
            
            
        
    
