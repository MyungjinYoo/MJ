import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title(':heartbeat: :blue[Economic data 2020~2022] :heartbeat:')

def plotting_basic() :
    money = pd.read_csv("money_data7.csv")
    option = st.selectbox( 'How would you like to choice year ?', ('2020', '2021', '2022') )
    option2 = int(option)
    st.write('You selected:', option)
    money = money[:] [money['A_YEAR']== option2]
    fig, ax = plt.subplots(2,2, figsize=(15,10))

def plotting_line() :
    plt.subplot(221)
    plt.plot( money.A_MONTH , money.A_RATE , color='red' , marker='o' ) 
    plt.xticks( money.A_MONTH )
    plt.title('US Interest')

    plt.subplot(222)
    plt.plot( money.A_MONTH , money.K_RATE' , color='blue' , marker='o' ) 
    plt.xticks( money.A_MONTH )
    plt.title('KR Interest')

    plt.subplot(223)
    plt.plot( money.A_MONTH, money.KOSPI, color='green' , marker='o' )
    plt.xticks( money.A_MONTH )
    plt.title('KOSPI')

    plt.subplot(224)
    plt.plot( money.A_MONTH, money.HOUSE_PRICE, color='yellow' , marker='o' )
    plt.xticks( money.A_MONTH )
    plt.title('Housing Price')

    st.pyplot(fig)
    st.dataframe(money)

with st.form(key ='Form1'):
    with st.sidebar:
        select_language = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie' , 'histogram' , 'corr' , 'wordcloud' , 'box' ))
plotting_basic()
if select_language =='line':
    plotting_line()
