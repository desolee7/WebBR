import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from pathlib import Path


def get_project_root() -> str:
    return str(Path(__file__).parent.parent.parent)


def load_image(image_name: str) -> Image:
    return Image.open(Path(get_project_root()) / f"references/{image_name}")


st.sidebar.image(load_image("img/logo.png"), use_column_width=True)
with st.sidebar:
    selected = option_menu('SimiLo', ["Intro", 'Search','About'],
        icons=['play-btn','search','info-circle'],menu_icon='intersect', default_index=0)