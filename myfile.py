import streamlit as st
import pandas as pd
import numpy as np
import urllib_request
from streamlit_option_menu import option_menu
import matplotlib_pyplot as plt
import plotly_figure_factory as ff
import scipy

st.set_page_config(layout="wide",initial_sidebar_state='expanded')
with open('upch.css') as f :
    st.markdown(f'<style>{f.read()}</upch>',unsafe_allow_html=True)
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
    
