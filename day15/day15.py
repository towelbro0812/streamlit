import streamlit as st

st.header('數學公式顯示 st.latex')
st.write("這裡我們可以用latex語法來寫")
st.write("> https://reurl.cc/b7NAKv")

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')