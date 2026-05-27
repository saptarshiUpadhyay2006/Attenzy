import streamlit as st

from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np

def student_screen():
    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='large')
    with c1:
        header_dashboard()
    with c2:
        # Ensure unique key for "Go back to Home" button in login screen
        if st.button("Go back to Home", type='secondary', key='loginbackbtn_teacher_login_screen', shortcut='control+backspace'):
            st.session_state['login-type'] = None
            st.rerun()

    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()

    photo_source=st.camera_input("Show your face to login")

    if photo_source:
        np.array(Image.open(photo_source))
    footer_dashboard()