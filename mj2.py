import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title(':heartbeat: blue[Economic data 2020~2022]	:heartbeat:')

def  Monthly_economic_data():
    
    uploaded_file = st.file_uploader("Choose a file")
    money=pd.read_csv(uploaded_file)
    option = st.selectbox( 'How would you like to choice year ?', ('2020', '2021', '2022') )
    option2 = int(option)
    st.write('You selected:', option)
    money.rename(columns = {'A_YEAR' : 'Year' , 'A_MONTH' : 'Month' ,'A_DOLLAR':'Dollar_currency', 'A_RATE' : 'US_interest', 'KOSPI': 'KOSPI', 'SALARY_INCREASE' : 'Salary_Index', 'K_RATE': 'KOR_interest' ,'OIL_PRICE': 'brent_oil_price' ,'HOUSE_PRICE': 'House_price_index'} , inplace = True )
    money = money[:] [money['Year']== option2]
    fig, ax = plt.subplots(2,2, figsize=(15,10))
    
    plt.subplot(221)
    plt.plot(  money.Month , money.US_interest , color='red' , marker='o'     ) 
    plt.xticks( money.Month )
    plt.title('US Interest')

    plt.subplot(222)
    plt.plot(  money.Month , money.KOR_interest , color='blue' , marker='o'     ) 
    plt.xticks( money.Month )
    plt.title('KOR Interest')

    plt.subplot(223)
    plt.plot(  money.Month , money.KOSPI , color='green' , marker='o'     ) 
    plt.xticks( money.Month )
    plt.title('Kospi Index')

    plt.subplot(224)
    plt.plot(  money.Month , money.House_price_index , color='yellow' , marker='o'     ) 
    plt.xticks( money.Month )
    plt.title('House Price')

    st.pyplot(fig)
    st.dataframe(money)

def KBO_standings() :
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
    df7 = df7[['순위','정규순위','팀','경기수','승','패','무','승률','게임차','연속','출루율','장타율','최근 10경기','년도']]
    df7.rename(columns = {'순위' : 'PO순위'} , inplace = True )
    df7['게임차'] = round(df7.게임차,1)
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
        select_graph = st.sidebar.radio('Which graph are you looking for?', ('Monthly economic data','KBO standings'))

if select_graph =='Monthly economic data':
    try:
          Monthly_economic_data()
    except:      
          pass
        
elif select_graph == 'KBO standings' :
    try :
        KBO_standings()
    except :
        pass
