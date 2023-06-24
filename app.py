import streamlit as st
from streamlit_option_menu import option_menu
from src.remove_ import remove
from src.About_me import AboutMe
from src.Projects import Projects
from src.contact import Contact

st.set_page_config(page_title="Gyan Prakash Kushwaha", page_icon=":🥸:", layout="wide", initial_sidebar_state="expanded")

remove()

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['About me', 'Projects', 'Skills', 'Contact'],
        icons=['GlyphCraft', 'IconCraft', '😊', '😎'],
        menu_icon='cast',
        default_index=0
    )

if selected == 'About me':
    abt_me = AboutMe()
    abt_me.aboutme()

elif selected == 'Projects':
    project = Projects()
    project.Project()


elif selected == 'Contact':
    contact_ = Contact()
    contact_.contact()


elif selected == 'Achievements':
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1.6rem;
                padding-bottom: 5rem;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Achievements")
