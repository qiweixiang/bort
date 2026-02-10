import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="气味香",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("qwx的聊天")
st.header("头")
st.subheader("耳机头")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
# st.markdown('Streamlit is **_really_ cool**.')
# st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

st.image('C:\\Users\\60566\Desktop\\u=2892873496,2351386762&fm=253&gp=0.jpg')
st.logo('C:\\Users\\60566\Desktop\\u=2892873496,2351386762&fm=253&gp=0.jpg')
st.button(label='请输入')
aa = st.text_input(label='你好啊')
st.write(f'名字是:{aa}')