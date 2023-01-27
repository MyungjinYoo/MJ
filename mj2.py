import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title(':heartbeat: :blue[Economic data 2020~2022] :heartbeat:')
uploaded_file = st.file_uploader("Choose a file")
money=pd.read_csv(uploaded_file)

def plotting_line() :

    #money = pd.read_csv("money_data7.csv")
    option = st.selectbox( 'How would you like to choice year ?', ('2020', '2021', '2022') )
    option2 = int(option)
    st.write('You selected:', option)
    money = money[:] [money['A_YEAR']== option2]
    fig, ax = plt.subplots(2,2, figsize=(15,10))
    
    plt.subplot(221)
    plt.plot(  money.A_MONTH , money.A_RATE , color='red' , marker='o'     ) 
    plt.xticks( money.A_MONTH )
    plt.title('America rate')

    plt.subplot(222)
    plt.plot(  money.A_MONTH , money.K_RATE , color='blue' , marker='o'     ) 
    plt.xticks( money.A_MONTH )
    plt.title('Korea rate')

    plt.subplot(223)
    plt.plot(  money.A_MONTH , money.KOSPI , color='green' , marker='o'     ) 
    plt.xticks( money.A_MONTH )
    plt.title('Kospi Rate')

    plt.subplot(224)
    plt.plot(  money.A_MONTH , money.HOUSE_PRICE , color='yellow' , marker='o'     ) 
    plt.xticks( money.A_MONTH )
    plt.title('House Price')

    st.pyplot(fig)
    st.dataframe(money)
    try:
          plotting_demo()
    except:
          pass

with st.form(key ='Form1'):
    with st.sidebar:
        select_language = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie' , 'histogram' , 'corr' , 'wordcloud' , 'box' ))

