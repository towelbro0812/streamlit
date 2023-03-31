import streamlit as st

st.title('機密檔案 st.secrets')
st.write('在跟目錄下新增/.streamlit/secret.toml')
st.write('資料是以字典形式存在，用字典形式調用，因為是秘密文件，要在gitignore中加入檔案')
st.code('''st.secrets['message']''')
st.write(st.secrets['message'])
