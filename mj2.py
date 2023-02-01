import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def  plotting_line():
    
    uploaded_file = st.file_uploader("Choose a file")
    money=pd.read_csv(uploaded_file)
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

def plotting_bar() :
    url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="
    years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]
    df = pd.DataFrame([])
    for i in years:
        df1 = pd.read_html(url+i)[0]
        df1['년도'] = i
        df = pd.concat([df, df1], axis=0)
    df.팀.replace({'두산':'Doosan','삼성':'Samsung','키움':'Kiwoom','한화': 'Hanhwa','롯데':'Lotte','넥센':'Nexen'}, inplace=True)
    baseball = df
    option = st.selectbox(
        'How would you like to choice year ?',
        ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))
    option2 = option
    st.write('You selected:', option)
    baseball['정규순위'] = baseball.groupby('년도')['승률'].rank(ascending = False).astype(int)
    df7  =  baseball[:] [ baseball.년도==option2 ].sort_values(by = '승률' , ascending = False).reset_index()
    df7 = df7[['순위','팀','경기수','승','패','무','승률','게임차','연속','출루율','장타율','최근 10경기','년도','정규순위']]
    df7['승률'] = round(df7.승률,1)
    x = df7.팀
    y = df7.승률
    fig, ax = plt.subplots(figsize=(15,10))
    colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7' ,'C8', 'C9', 'C10' ]
    plt.bar( x, y, color= colors , alpha = 0.6)
    for num , v in enumerate( y ):
        plt.text ( num -0.3 , v + 0.01 , v , fontsize = 14)
    plt.title( "KBO winrate data", position=(0.5,1.1) , fontsize = 22)
    plt.xticks(size = 14)
    plt.yticks(size = 14)
    st.pyplot(fig)
    st.dataframe(df7)


with st.form(key ='Form1'):
    with st.sidebar:
        select_language = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie' , 'histogram' , 'corr' , 'wordcloud' , 'box' ))

if select_language =='line':           
    try:
          plotting_line()
    except:      
          pass
        
if select_language == 'bar' :
    try :
        plotting_bar()
    except :
        pass
