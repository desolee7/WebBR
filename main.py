import requests
import streamlit as st
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
#background-image:  linear-gradient(#868be4 2px, transparent 2px), linear-gradient(90deg, #868be4 2px, transparent 2px), linear-gradient(#868be4 1px, transparent 1px), linear-gradient(90deg, #868be4 1px, #e9e9f8 1px);
#background-size: 50px 50px, 50px 50px, 10px 10px, 10px 10px;
#background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px;
page_bg_img = """
<style>

[data-testid="stAppViewContainer"] {     
    background-color: #ffffff;
    opacity: 0.8;
    background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #ffffff 350px ), repeating-linear-gradient( #444cf755, #444cf7 );


p { color: black;}}
[data-testid="stHeader"]{                    
    background-color: rgba(0, 0, 0, 0);
    color: black;
    font-size: 100px;
    font_weight: bold;
    
}
[data-testid="stSideBar"]{                    
    background-color: #819e66;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# st.title(':gray[Найди профессию мечты]')
gradient_text_html = """
<style>
.gradient-text {
    font-weight: bold;
    background-color: black;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 3em;
}
</style>
<div class="gradient-text">Найди профессию мечты</div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)

nap = st.selectbox(
    'Выбери направление',
    ('Направление не выбрано','ИТ', 'Программирование', 'Аналитика', 'Машинное обучение', 'Тестирование', 'ИТ-архитектура', 'Blockchain', 'Продукт и проекты', 'Маркетинг', 'Игры', 'Дизайн'))
tab1 = st.write('Ты выбрал:', nap)
if nap == "ИТ":
    time = st.selectbox(
    'Сколько ты бы хотел учиться?',
    ('Время обучения не выбрано','6 месяцев', '9 месяцев', '12 месяцев', '24 месяца'))
    tab2 = st.write('Ты выбрал:', time)

    if time!="Время обучения не выбрано":
        spec = st.selectbox(
        'Специализация',
        ('Специализация не выбрана', 'Тестирование', 'Аналитика', 'Программирование', 'Продуктовое управление', 'Проектное управление', 'Архитектура'))
        tab2 = st.write('Ты выбрал:', spec)

        if spec!='Специализация не выбрана':
            know = st.selectbox(
            'Знания на выходе',
            ('Знания на выходе не выбраны', 'Middle+', 'Middle', 'Junior'))
            tab2 = st.write('Ты выбрал:', know)

            if know!='Знания на выходе не выбраны':
                ustr = st.selectbox(
                'Устройства',
                ('Утройство не выбрано', 'Декстоп', 'Веб', 'Mobile', 'Оборудование', 'Умные устройства'))
                tab2 = st.write('Ты выбрал:', ustr)

                if ustr!='Утройство не выбрано':
                    celknow = st.selectbox(
                    'Цель знаний',
                    ('Цель знаний не выбрана', 'Образование', 'Повышение квалификации', 'Увеличить знания по теме'))
                    tab2 = st.write('Ты выбрал:', celknow)

                    if celknow!='Цель знаний не выбрана':
                        celprof = st.selectbox(
                        'Цель профессии',
                        ('Цель профессии не выбрана', 'Сменить профессию', 'Получить первую профессию'))
                        tab2 = st.write('Ты выбрал:', celprof)

                        if celprof!='Цель профессии не выбрана':
                            celrab = st.selectbox(
                            'Цель работы',
                            ('Цель работы не выбрана', 'Начать работать', 'Поменять работу'))
                            tab2 = st.write('Ты выбрал:', celrab)

                            if celrab!='Цель работы не выбрана':
                                celdoh = st.selectbox(
                                'Цель изменения дохода',
                                ('Цель изменения дохода не выбрана', 'Дополнительный доход', 'Увеличить доход'))
                                tab2 = st.write('Ты выбрал:', celdoh)

                                if celdoh!='Цель изменения дохода не выбрана':
                                    dop = st.selectbox(
                                    'Дополнительные цели',
                                    ('Дополнительные цели не выбраны', 'Получить модную профессию', 'Самоопределение', 'Релокация заграницу', 'Фининсовая независимость'))
                                    tab2 = st.write('Ты выбрал:', dop)
                                    if dop!='Дополнительные цели не выбраны':

                                        if st.button("Отправить данные"):
                                            data_to_send = {
                                                "Направление": nap,
                                                "Время обучения": time,
                                                "Специализация": spec,
                                                "Знания на выходе": know,
                                                "Устройства" : ustr,
                                                "Цель знаний" : celknow,
                                                "Цель профессии" : celprof,
                                                "Цель работы" : celrab,
                                                "Цель изменения дохода" : celdoh,
                                                "Дополнительные цели" : dop
                                            }
                                            response = requests.post('ссылка на бек', json=data_to_send)


