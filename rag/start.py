import streamlit as st
import knowleage_base as kb

print('hahahah')
st.title("Hello World")

# streamlit的上传文件方法  很简单
file_upload = st.file_uploader("Choose a file",type=['txt', 'csv','md'], accept_multiple_files=False)

if 'service' not in st.session_state:
    st.session_state['service'] = kb.KnowleageService()

if file_upload is not None:
    print(file_upload.name)
    print(file_upload.type)
    file_size = file_upload.size
    st.write(f'大小:{file_size}')
    result = st.session_state['service'].update_to_chroma(file_upload.getvalue().decode('utf-8'))
    st.success(result, icon="✅")



