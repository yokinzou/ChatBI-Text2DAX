
import streamlit as st
from Pages.Chat.Chat_PBI_Page import chatPBI
from Pages.Semantic_Management.PBI_Semantic_Page import PBI_Semantic


# 添加 logo 图片到侧边栏
st.logo(
    "logo.png",
) 

pg = st.navigation(
    [
    st.Page(chatPBI, title="Chat PBI", icon="💬"),
    st.Page(PBI_Semantic, title="Semantic Management", icon="🗄️"),
    #st.Page(file_manager, title="File Manager", icon="🗄️")
])
pg.run()    