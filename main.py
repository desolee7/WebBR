import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from pathlib import Path


# def get_project_root() -> str:
#     return str(Path(__file__).parent.parent.parent)


# def load_image(image_name: str) -> Image:
#     return Image.open(Path(get_project_root()) / f"references/{image_name}")


# st.sidebar.image(load_image("img/logo.png"), use_column_width=True)
# with st.sidebar:
#     selected = option_menu('SimiLo', ["Intro", 'Search','About'],
#         icons=['play-btn','search','info-circle'],menu_icon='intersect', default_index=0)

# import streamlit as st
# from streamlit_option_menu import option_menu

# # 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {          
background-color: #e9e9f8;
opacity: 1;
background-image:  linear-gradient(#444772 1px, transparent 1px), linear-gradient(to right, #444772 1px, #e9e9f8 1px);
background-size: 20px 20px;
}
[data-testid="stHeader"]{                    
background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title(':gray[Найди профессию мечты]')