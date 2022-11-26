import streamlit as st
import pandas as pd

#titulo del app
st.title("DATA SUNEDU")

#add s sidebar
st.sidebar.subheader("visualizacion de configuraciones")

#setup file upload
uploaded_file=st.sidebar.file_uploader(label="upload your CSV or Excel file",
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
st.write(df)



