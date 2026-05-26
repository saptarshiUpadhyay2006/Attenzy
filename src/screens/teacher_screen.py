import streamlit as st

from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher_exists,create_teacher,teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()

    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data['name']}""")

def login_teacher(username,password):
    if not username or not password:
        return False
    teacher=teacher_login(username,password)
    if teacher:
        st.session_state.user_role="teacher"
        st.session_state.user_data=teacher
        st.session_state.logged_in=True
        return True
    else:
        return False

def teacher_screen_login():
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

    st.header('Login using password', text_alignment='center')
    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder='Spuk', key='username_teacher_login')

    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password", key='password_teacher_login')
    st.divider()

    btnc1, btnc2 = st.columns(2)
    with btnc1:
        if st.button('Login', icon=':material/passkey:', shortcut='control+enter', width='stretch', key='loginbtn_teacher_login'):
            if login_teacher(teacher_username,teacher_pass):
                st.toast("welcome back!",icon=":wave:")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password! Please try again.")

    with btnc2:
        if st.button('Register instead', type="primary", icon=':material/passkey:', width='stretch', key='registerbtn_teacher_login'):
            st.session_state.teacher_login_type = 'register'
    footer_dashboard()

def register_teacher(username,name,password,password_confirm):
    if not username or not name or not password or not password_confirm:
        return False,"Please fill all the fields!"
    if check_teacher_exists(username):
        return False,"Username already exists! Please choose a different username."
    if password != password_confirm:
        return False,"Passwords do not match! Please confirm your password correctly."
    try:
        create_teacher(username,password,name)
        return True,"Registration successful! You can now login with your credentials."
    except Exception as e:
        return False,"An error occurred during registration. Please try again later."

def teacher_screen_register():
    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='large')
    with c1:
        header_dashboard()
    with c2:
        # Ensure unique key for "Go back to Home" button in register screen
        if st.button("Go back to Home", type='secondary', key='loginbackbtn_teacher_register_screen', shortcut='control+backspace'):
            st.session_state['login-type'] = None
            st.rerun()

    st.header('Register with your details', text_alignment='center')
    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder='Spuk', key='username_teacher_register')
    teacher_name = st.text_input("Enter name", placeholder='Spuk', key='name_teacher_register')

    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password", key='password_teacher_register')
    teacher_pass_confirm = st.text_input("Confirm your password", type='password', placeholder="Enter password", key='password_confirm_teacher_register')
    st.divider()

    btnc1, btnc2 = st.columns(2)
    with btnc1:
        if st.button('Register', icon=':material/passkey:', shortcut='control+enter', width='stretch', key='registerbtn_teacher_register'):
            success,message=register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button('Login instead', type="primary", icon=':material/passkey:', width='stretch', key='loginbtn_teacher_register'):
            st.session_state.teacher_login_type = 'login'
    footer_dashboard()