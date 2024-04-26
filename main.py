import requests
import streamlit as st
from PIL import Image
from pathlib import Path
import logging


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
#background-image: url("https://catherineasquithgallery.com/uploads/posts/2021-02/1614380674_69-p-fon-abstraktsiya-svetlii-geometriya-76.jpg");
#background-image: url("https://img.freepik.com/free-photo/glowing-spider-web-dark-abstract-backdrop-generated-by-ai_188544-36464.jpg?t=st=1714086465~exp=1714090065~hmac=eb294949183cf9872d61d6f464e6fd8cea816540d71eeaa88d2852888f97cb96&w=1380");



page_bg_img = """
<style>

[data-testid="stAppViewContainer"] {  
    background-image: url("https://img.freepik.com/free-photo/glowing-spider-web-dark-abstract-backdrop-generated-by-ai_188544-36464.jpg?t=st=1714086465~exp=1714090065~hmac=eb294949183cf9872d61d6f464e6fd8cea816540d71eeaa88d2852888f97cb96&w=1380");   
    
    background-size: cover;

    # background-color: #ffffff;
    # opacity: 0.8;
    # background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #ffffff 350px ), repeating-linear-gradient( #444cf755, #444cf7 );

p { color: white;
background-color: black, transparent 50;}
}
[data-testid="stHeader"]{                    
    background-color: rgba(0, 0, 0, 0);
    color: black;
    font-size: 100px;
    font_weight: bold;
    
}
[data-testid="stSideBar"]{                    
    background-color: #819e66;
}
div[data-baseweb = "select"] > div{
background-color: black;
border-color: #CDFF6A; 
color: white;}
[data-testid = "stForm"]{
background: black;}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

gradient_text_html = """
<style>
.gradient-text {
    font-weight: bold;
    background-color: #CDFF6A;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 3em;
    font-family: 'Courier New', Courier, monospace;
    padding: 20px;
}
</style>
<div class="gradient-text"><Найди профессию мечты></div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)
with st.form("My form"):
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
                                                response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
    st.form_submit_button()

    if nap == "Программирование":
        time = st.selectbox(
        'Сколько ты бы хотел учиться?',
        ('Время обучения не выбрано','6 месяцев', '9 месяцев', '12 месяцев', '24 месяца'))
        tab2 = st.write('Ты выбрал:', time)
        if time!="Время обучения не выбрано":
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
                                        prog = st.selectbox(
                                        'Программирование',
                                        ('Программирование не выбрано', 'Frontend', 'Backend', 'Fullstack'))
                                        tab2 = st.write('Ты выбрал:', prog)
                                        if prog!='Программирование не выбрано':
                                            lung = st.selectbox(
                                            'Языки и технологии',
                                            ('Языки и технологии не выбраны', 'их слишком дофига'))
                                            tab2 = st.write('Ты выбрал:', lung)
                                            if lung!='Языки и технологии не выбраны':

                                                if st.button("Отправить данные"):
                                                    data_to_send = {
                                                        "Направление": nap,
                                                        "Время обучения": time,
                                                        "Знания на выходе": know,
                                                        "Устройства" : ustr,
                                                        "Цель знаний" : celknow,
                                                        "Цель профессии" : celprof,
                                                        "Цель работы" : celrab,
                                                        "Цель изменения дохода" : celdoh,
                                                        "Дополнительные цели" : dop,
                                                        "Программирование" : prog,
                                                        "Языки и технологии" : lung
                                                    }
                                                    response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
                                                    logging.debug(response.text)





