# pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


st.set_page_config(layout="wide", initial_sidebar_state='expanded')
with open('logo.css) as f : 
    st.markdown(f'<style>{f.read()}</logo>',unsafe_allow_html=True)
with st.sidebar:
    st.markdown('###')
    st.sidebar.header ('Programación') 
    selected= option_menu(
        menu_title='Menú',
        options=['Inicio','Equipo','Analisis','reporte'],
        icons=['house','person','glass','book'],
        menu_icon='cast',
        default_index= 0,
    )
    
