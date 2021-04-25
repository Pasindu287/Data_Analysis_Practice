import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.

import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("sample.csv")
types = st.multiselect('Show categories?', df['CATEGORY'].unique())
sentiment = st.multiselect('Show positve/negative reviews?', df['sentimentt'].unique())# Filter dataframe
new_df = df[(df['CATEGORY'].isin(types)) & (df['sentimentt'].isin(sentiment))]# write dataframe to screen
st.write(new_df)