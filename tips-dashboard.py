#importing libraries
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Tips Dashboard',
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state='expanded')

# loading Data
df= pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Python Course\Data Analysis\tips.csv")

df['total_bill'] = pd.to_numeric(df['total_bill'], errors='coerce')

# sidebar
st.sidebar.header('Tips Dashborad')
st.sidebar.image('https://img.freepik.com/free-vector/glass-money-box-tips_1441-3953.jpg', use_column_width=True, caption="welcome to my Dashboard")
st.sidebar.write('This Dashboard is using Tips dataset from seaborn for educational purposes.')
st.sidebar.write('')
st.sidebar.write('Filter your data:')
cat_filter= st.sidebar.selectbox('Categorical Filtering',[None,'day','sex','smoker','time'])
num_filter= st.sidebar.selectbox('Numerical Filtering',[None,'total_bill','tip'])
row_filter= st.sidebar.selectbox('row Filtering',[None,'day','sex','smoker','time'])
column_filter= st.sidebar.selectbox('column Filtering',[None,'day','sex','smoker','time'])

st.sidebar.write("")
st.sidebar.markdown("Made with :heart_eyes: by Eng. [Ahmed Omar]")


# Body

# row a
a1, a2, a3, a4 = st.columns(4)

a1.metric('Max. Total Bill', df['total_bill'].max())
a2.metric('Max. tip', df['tip'].max())
a3.metric('Min. Total Bill', df['total_bill'].min())
a4.metric('Min. tip', df['tip'].min())

size_col = num_filter if num_filter else None
color_col = cat_filter if cat_filter else None

# row B
st.subheader('Total_bill vs. Tips')
fig = px.scatter(
    df,
    x='total_bill',
    y='tip',
    color=cat_filter,
    size=num_filter,
    facet_row=row_filter,
    facet_col=column_filter,
    color_discrete_sequence=px.colors.qualitative.Set1,
    title=f"Scatter Plot colored by {cat_filter} and sized by {num_filter}"
)

st.plotly_chart(fig, use_container_width=True)

# ROW C

c1,c2,c3 = st.columns((4,3,3))
with c1:
    st.text('Sex Vs Total_bill')
    fig = px.bar(df, x= 'sex', y = 'total_bill', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.text('Smoker \ Non_smoker VS. Tips')
    fig = px.pie(df, names= 'smoker', values = 'tip', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)  

with c3:
    st.text('Days VS. Tips')
    fig = px.pie(df, names='day',
                 values='tip',
                 hole=0.4)
    st.plotly_chart(fig, use_container_width=True)  