import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px


df = st.cache(pd.read_csv)("sample_2.csv")

types = st.sidebar.multiselect('Show types of Restaurants', df['CATEGORY'].unique())

price = st.sidebar.multiselect('Filter by price range', df['AVG_PRICE'].unique())

new_df = df[(df['CATEGORY'].isin(types)) & (df['AVG_PRICE'].isin(price))]

st.write(new_df)# Create distplot with custom bin_size

fig = px.bar(new_df, x ='CATEGORY',y='RATING',color='SENTIMENT')
'''
### Visualization
'''
st.plotly_chart(fig)