import requests
import streamlit as st
from PIL import Image
from pathlib import Path
import logging
import base64



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
#background-image: url("https://understandbrain.com/wp-content/uploads/2023/09/glowing-spider-web-dark-abstract-backdrop-generated-by-ai.jpg");   
#background-image: url("https://thecharnelhouse.org/wp-content/uploads/2014/06/al-3-1926-lc3a1szlc3b3-moholy-nagy-oil-industrial-paints-and-pencil-on-aluminum-40-x-40-cm.jpg");
#color: #E8E6BB
#color: #DEFFA8;
page_bg_img = """
<style>

[data-testid="stAppViewContainer"] {  
    background-image: url("https://sun9-23.userapi.com/impg/XiO97rsW6bxg28kT5PH2JzV0j9St0JeHe8mWxQ/BSwgAokPBQ0.jpg?size=2560x1440&quality=96&sign=d30f4a2726161edc785e389ec67e5c2e&type=album");   
    # background-image: url("https://understandbrain.com/wp-content/uploads/2023/09/glowing-spider-web-dark-abstract-backdrop-generated-by-ai.jpg");   

    
    background-size: cover;

    # background-color: #ffffff;
    # opacity: 0.8;
    # background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #ffffff 350px ), repeating-linear-gradient( #444cf755, #444cf7 );

p { color: black;
background-color: black, transparent 50;
font-size: 20px;
}
}
[data-testid="stHeader"]{                    
    background-color: rgba(0, 0, 0, 0);
    color: black;
    font-size: 100px;
    font_weight: bold;
    
}
[data-testid="stSidebar"]{                    
    background-color: black;
}
[data-testid="stButton"]{                    
    border-color: rgba(0, 0, 0, 0);
}
div[data-baseweb = "select"] > div{
    # background-color: black;
    # border-color: #CDFF6A;
    background-color: #DEFFA8;
    border-color: rgba(0, 0, 0, 0);
    border-radius: 10px;
    #color: #E8E6BB;
    color: black;
}
[data-testid = "stForm"]{
background: black;}


[data-baseweb="icon"]{
#color: #DEFFA8;
color: black;
}

[class="st-emotion-cache-sy3zga e1gc5fo21"]{
color: #E8E6BB;
}

[class="st-emotion-cache-9ycgxx e1b2p2ww12"]{
#color: #E8E6BB;
color: black;
#подпись drag and drop
}

[class="st-emotion-cache-7oyrr6 e1bju1570"]{
#color: #E8E6BB;
color: black;
#подпись лимит
}

[class="st-emotion-cache-19rxjzo ef3psqc12"]{
background-color: #DEFFA8;
color: black;
border-color: #DEFFA8;
#browse file in drag and drop
}

[role="button"]{
background-color: #DEFFA8;
border-color: rgba(0,0,0,0);
border-radius: 10px;
}
[role="textbox"]{
background-color: #DEFFA8;
border-radius: 10px;
}
[class="st-emotion-cache-wn8ljn e1b2p2ww13"]{
#color: #E8E6BB;
color: black;
# Подписи в дропдауне
}

[data-baseweb="input"]{
border-color: #DEFFA8;
}
[data-baseweb="base-input"]{
background-color: #DEFFA8;
color: black;
border-color: #DEFFA8;
-webkit-text-fill-color: black;
caret-color: red;
}
[data-baseweb="textarea"]{
border-color: #DEFFA8;
color: black;
caret-color: red;
}
[class="st-emotion-cache-1mdkfbq e1b2p2ww3"]{
color: black; #вет загруженного пдф
}

[class="st-emotion-cache-1lp7pgu ef3psqc9"]{
color: black; #вет загруженного пдф
}



[class="stFileUploaderFileData st-emotion-cache-1l4firl e1b2p2ww7"]{
color: black; #вет загруженного пдф
font-size: 20px;
}

# [class="st-emotion-cache-7oyrr6 e1bju1570"]{
# color: #3A0603;
# }


.st-cc > div > div > div > input {
    border-color: rgba(0, 0, 0, 0);
    #border-width: 2px;
    #border-style: solid;
    border-radius: 5px;
    
}

.stTextInput > div > div > input {
    background-color: #DEFFA8;
    color: black;
}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

gradient_text_html = """
<style>
.gradient-text {
    # background-color: #CDFF6A;
    # background-color: #3A0603;
    background-color: black;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 46px;
    font-family: 'Courier New', Courier, monospace;
    # font-family: Franklin Gothic;
    font-weight: bold;
    padding: 10px;
}
</style>
<div class="gradient-text"><Найди профессию мечты/></div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)
#options = ['Пройти опрос', 'Посмотреть результат']

#file = st.sidebar.radio('Выберите:', options)

# if st.button("Browse", className="file-upload-btn"):
#     uploaded_file = st.file_uploader("Choose a file")
#     if uploaded_file is not None:
#         # Process the uploaded file
#         st.write("File uploaded successfully!")

def extract_data(uploaded_file):
    file_content = uploaded_file.read()
    # st.write(file_content)
    encoded_file_content = base64.b64encode(file_content).decode('utf-8')
    # st.write(encoded_file_content)
    return {
        "file_content": encoded_file_content
    }




with st.container():
    select = st.selectbox(
         'Выберите формат добавления вакансии',
         ('Загрузить PDF','Вставить ссылку на вакансию', 'Ввести текстовое описание вакансии'))
    if select == 'Загрузить PDF':

        # uploaded_files = st.file_uploader(    #рабочий код для драг н дропа
        # "Загрузить PDF",
        # accept_multiple_files=True,
        # type=['pdf'],
        # help='Перетащите PDF файл'
        # )

        uploaded_file = st.file_uploader('Перетащите PDF файл', type="pdf")
        if uploaded_file is not None:
            df = extract_data(uploaded_file)
            if st.button("Найти по PDF"):
                data_to_send = df
                response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
                print(response.text)

    elif select == 'Вставить ссылку на вакансию':
        url_vac = st.text_input('Вставьте ссылку на вакансию', key="text_input", help='Вставьте сюда ссылку')
        if st.button("Найти по ссылке"):
            data_to_send = {
                "url_vac": url_vac
            }
            response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
            print(response.text)

    elif select == 'Ввести текстовое описание вакансии':
        text_desc_vac = st.text_area('Введите текстовое описание вакансии', key="text_input", help='Введите сюда описание',height=150)
        if st.button("Найти по описанию"):
            data_to_send = {
                "text_vac": text_desc_vac
            }
            response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
            print(response.text)


          
     



# for uploaded_file in uploaded_files:     ОБРАБОТКА И ВЫВОД ПДФ
#     bytes_data = uploaded_file.read()

#     st.write("filename:", uploaded_file.name)
#     base64_pdf = base64.b64encode(bytes_data).decode('utf-8')
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)





# with st.form("My form"):
#     nap = st.selectbox(
#         'Выбери направление',
#         ('Направление не выбрано','ИТ', 'Программирование', 'Аналитика', 'Машинное обучение', 'Тестирование', 'ИТ-архитектура', 'Blockchain', 'Продукт и проекты', 'Маркетинг', 'Игры', 'Дизайн'))
#     tab1 = st.write('Ты выбрал:', nap)
#     if nap == "ИТ":
#         time = st.selectbox(
#         'Сколько ты бы хотел учиться?',
#         ('Время обучения не выбрано','6 месяцев', '9 месяцев', '12 месяцев', '24 месяца'))
#         tab2 = st.write('Ты выбрал:', time)

#         if time!="Время обучения не выбрано":
#             spec = st.selectbox(
#             'Специализация',
#             ('Специализация не выбрана', 'Тестирование', 'Аналитика', 'Программирование', 'Продуктовое управление', 'Проектное управление', 'Архитектура'))
#             tab2 = st.write('Ты выбрал:', spec)

#             if spec!='Специализация не выбрана':
#                 know = st.selectbox(
#                 'Знания на выходе',
#                 ('Знания на выходе не выбраны', 'Middle+', 'Middle', 'Junior'))
#                 tab2 = st.write('Ты выбрал:', know)

#                 if know!='Знания на выходе не выбраны':
#                     ustr = st.selectbox(
#                     'Устройства',
#                     ('Утройство не выбрано', 'Декстоп', 'Веб', 'Mobile', 'Оборудование', 'Умные устройства'))
#                     tab2 = st.write('Ты выбрал:', ustr)

#                     if ustr!='Утройство не выбрано':
#                         celknow = st.selectbox(
#                         'Цель знаний',
#                         ('Цель знаний не выбрана', 'Образование', 'Повышение квалификации', 'Увеличить знания по теме'))
#                         tab2 = st.write('Ты выбрал:', celknow)

#                         if celknow!='Цель знаний не выбрана':
#                             celprof = st.selectbox(
#                             'Цель профессии',
#                             ('Цель профессии не выбрана', 'Сменить профессию', 'Получить первую профессию'))
#                             tab2 = st.write('Ты выбрал:', celprof)

#                             if celprof!='Цель профессии не выбрана':
#                                 celrab = st.selectbox(
#                                 'Цель работы',
#                                 ('Цель работы не выбрана', 'Начать работать', 'Поменять работу'))
#                                 tab2 = st.write('Ты выбрал:', celrab)

#                                 if celrab!='Цель работы не выбрана':
#                                     celdoh = st.selectbox(
#                                     'Цель изменения дохода',
#                                     ('Цель изменения дохода не выбрана', 'Дополнительный доход', 'Увеличить доход'))
#                                     tab2 = st.write('Ты выбрал:', celdoh)

#                                     if celdoh!='Цель изменения дохода не выбрана':
#                                         dop = st.selectbox(
#                                         'Дополнительные цели',
#                                         ('Дополнительные цели не выбраны', 'Получить модную профессию', 'Самоопределение', 'Релокация заграницу', 'Фининсовая независимость'))
#                                         tab2 = st.write('Ты выбрал:', dop)
#                                         if dop!='Дополнительные цели не выбраны':

#                                             if st.button("Отправить данные"):
#                                                 data_to_send = {
#                                                     "Направление": nap,
#                                                     "Время обучения": time,
#                                                     "Специализация": spec,
#                                                     "Знания на выходе": know,
#                                                     "Устройства" : ustr,
#                                                     "Цель знаний" : celknow,
#                                                     "Цель профессии" : celprof,
#                                                     "Цель работы" : celrab,
#                                                     "Цель изменения дохода" : celdoh,
#                                                     "Дополнительные цели" : dop
#                                                 }
#                                                 response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
#     st.form_submit_button()

#     if nap == "Программирование":
#         time = st.selectbox(
#         'Сколько ты бы хотел учиться?',
#         ('Время обучения не выбрано','6 месяцев', '9 месяцев', '12 месяцев', '24 месяца'))
#         tab2 = st.write('Ты выбрал:', time)
#         if time!="Время обучения не выбрано":
#             know = st.selectbox(
#             'Знания на выходе',
#             ('Знания на выходе не выбраны', 'Middle+', 'Middle', 'Junior'))
#             tab2 = st.write('Ты выбрал:', know)
#             if know!='Знания на выходе не выбраны':
#                 ustr = st.selectbox(
#                 'Устройства',
#                 ('Утройство не выбрано', 'Декстоп', 'Веб', 'Mobile', 'Оборудование', 'Умные устройства'))
#                 tab2 = st.write('Ты выбрал:', ustr)

#                 if ustr!='Утройство не выбрано':
#                     celknow = st.selectbox(
#                     'Цель знаний',
#                     ('Цель знаний не выбрана', 'Образование', 'Повышение квалификации', 'Увеличить знания по теме'))
#                     tab2 = st.write('Ты выбрал:', celknow)

#                     if celknow!='Цель знаний не выбрана':
#                         celprof = st.selectbox(
#                         'Цель профессии',
#                         ('Цель профессии не выбрана', 'Сменить профессию', 'Получить первую профессию'))
#                         tab2 = st.write('Ты выбрал:', celprof)

#                         if celprof!='Цель профессии не выбрана':
#                             celrab = st.selectbox(
#                             'Цель работы',
#                             ('Цель работы не выбрана', 'Начать работать', 'Поменять работу'))
#                             tab2 = st.write('Ты выбрал:', celrab)

#                             if celrab!='Цель работы не выбрана':
#                                 celdoh = st.selectbox(
#                                 'Цель изменения дохода',
#                                 ('Цель изменения дохода не выбрана', 'Дополнительный доход', 'Увеличить доход'))
#                                 tab2 = st.write('Ты выбрал:', celdoh)

#                                 if celdoh!='Цель изменения дохода не выбрана':
#                                     dop = st.selectbox(
#                                     'Дополнительные цели',
#                                     ('Дополнительные цели не выбраны', 'Получить модную профессию', 'Самоопределение', 'Релокация заграницу', 'Фининсовая независимость'))
#                                     tab2 = st.write('Ты выбрал:', dop)
#                                     if dop!='Дополнительные цели не выбраны':
#                                         prog = st.selectbox(
#                                         'Программирование',
#                                         ('Программирование не выбрано', 'Frontend', 'Backend', 'Fullstack'))
#                                         tab2 = st.write('Ты выбрал:', prog)
#                                         if prog!='Программирование не выбрано':
#                                             lung = st.selectbox(
#                                             'Языки и технологии',
#                                             ('Языки и технологии не выбраны', 'их слишком дофига'))
#                                             tab2 = st.write('Ты выбрал:', lung)
#                                             if lung!='Языки и технологии не выбраны':

#                                                 if st.button("Отправить данные"):
#                                                     data_to_send = {
#                                                         "Направление": nap,
#                                                         "Время обучения": time,
#                                                         "Знания на выходе": know,
#                                                         "Устройства" : ustr,
#                                                         "Цель знаний" : celknow,
#                                                         "Цель профессии" : celprof,
#                                                         "Цель работы" : celrab,
#                                                         "Цель изменения дохода" : celdoh,
#                                                         "Дополнительные цели" : dop,
#                                                         "Программирование" : prog,
#                                                         "Языки и технологии" : lung
#                                                     }
#                                                     response = requests.post('https://echo.free.beeceptor.com', json=data_to_send)
#                                                     logging.debug(response.text)





