import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')
st.info('現在已經棄用st.cache，全面更改為st.cache_data 或 st.cache_resource')
# Using cache

st.subheader('Using st.cache')

@st.cache_resource
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

if st.button('Use cache',key="firstbtn"):
    a0 = time()
    st.write(load_data_a())
    a1 = time()
    st.info(f'耗費時間: {a1-a0}')


# Not using cache

st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
if st.button('Not using cache',key="secondbtn"):
    b0 = time()
    st.write(load_data_b())
    b1 = time()
    st.info(f'耗費時間: {b1-b0}')