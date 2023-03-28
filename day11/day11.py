import streamlit as st

st.header('多重選擇 st.multiselect()')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
st.write(f"這是{type(options)}型態的")
st.write('You selected:', options)