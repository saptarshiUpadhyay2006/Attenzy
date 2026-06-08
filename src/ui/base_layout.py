import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: radial-gradient(circle at top right, #3B429F, #1F235A, #0A0C27) !important;
                }

                .stApp div[data-testid="stColumn"]:has(.role-title) {
                    background: rgba(255, 255, 255, 0.04) !important;
                    backdrop-filter: blur(12px) !important;
                    -webkit-backdrop-filter: blur(12px) !important;
                    border: 1px solid rgba(255, 255, 255, 0.08) !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
                    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
                }

                /* Center the stVerticalBlock inside the stColumn */
                .stApp div[data-testid="stColumn"]:has(.role-title) div[data-testid="stVerticalBlock"] {
                    display: flex !important;
                    flex-direction: column !important;
                    align-items: center !important;
                    justify-content: center !important;
                    width: 100% !important;
                }

                /* Center stImage inside stColumn */
                .stApp div[data-testid="stColumn"]:has(.role-title) div[data-testid="stImage"] {
                    display: flex !important;
                    justify-content: center !important;
                    width: 100% !important;
                }

                /* Center stButton wrapper inside stColumn */
                .stApp div[data-testid="stColumn"]:has(.role-title) div[data-testid="stButton"] {
                    display: flex !important;
                    justify-content: center !important;
                    width: 100% !important;
                }

                .stApp div[data-testid="stColumn"]:has(.role-title):hover {
                    transform: translateY(-8px) !important;
                    border-color: rgba(88, 101, 242, 0.4) !important;
                    box-shadow: 0 12px 40px 0 rgba(88, 101, 242, 0.25) !important;
                    background: rgba(255, 255, 255, 0.07) !important;
                }

                .stApp div[data-testid="stColumn"]:has(.role-title) img {
                    display: block;
                    margin: 0 auto !important;
                    filter: invert(1) brightness(0.95) !important;
                    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
                }

                .stApp div[data-testid="stColumn"]:has(.role-title):hover img {
                    transform: scale(1.06) !important;
                    filter: invert(1) brightness(1) drop-shadow(0 0 8px rgba(255, 255, 255, 0.25)) !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    


def style_background_dashboard():

    st.markdown("""
        <style>
                /* Set standard font for all elements inside dashboard (excluding div and span to avoid overriding icon fonts) */
                body, input, select, textarea, button, label, p {
                    font-family: 'Outfit', sans-serif !important;
                }

                .stApp {
                    background: radial-gradient(circle at top right, #1F235A, #0E102F, #050614) !important;
                }

                .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
                    color: #FFFFFF !important;
                    font-family: 'Outfit', sans-serif !important;
                }

                .stApp p, .stApp label, .stApp span, .stApp div[data-testid="stMarkdown"] p {
                    color: #C4D1FF !important;
                }

                /* Container boxes / borders stylized as premium glassmorphic cards */
                div[data-testid="stVerticalBlockBorderWrapper"] {
                    background: rgba(255, 255, 255, 0.03) !important;
                    backdrop-filter: blur(12px) !important;
                    -webkit-backdrop-filter: blur(12px) !important;
                    border: 1px solid rgba(255, 255, 255, 0.08) !important;
                    border-radius: 1.5rem !important;
                    padding: 1.5rem !important;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2) !important;
                }

                /* Text inputs inside dashboard */
                div[data-testid="stTextInput"] input {
                    background-color: rgba(255, 255, 255, 0.03) !important;
                    color: #FFFFFF !important;
                    border: 1px solid rgba(255, 255, 255, 0.08) !important;
                    border-radius: 1rem !important;
                    padding: 12px 16px !important;
                    font-size: 1rem !important;
                    transition: all 0.3s ease !important;
                }
                
                div[data-testid="stTextInput"] input:focus {
                    border-color: #5865F2 !important;
                    box-shadow: 0 0 12px rgba(88, 101, 242, 0.25) !important;
                    background-color: rgba(255, 255, 255, 0.06) !important;
                }

                div[data-testid="stTextInput"] label {
                    font-size: 0.95rem !important;
                    font-weight: 600 !important;
                    color: #A2B4FF !important;
                    margin-bottom: 0.5rem !important;
                }

                /* Selectboxes inside dashboard */
                div[data-testid="stSelectbox"] > div > div {
                    background-color: rgba(255, 255, 255, 0.03) !important;
                    color: #FFFFFF !important;
                    border: 1px solid rgba(255, 255, 255, 0.08) !important;
                    border-radius: 1rem !important;
                    padding: 4px 8px !important;
                    transition: all 0.3s ease !important;
                }

                div[data-testid="stSelectbox"] > div > div:focus-within {
                    border-color: #5865F2 !important;
                    box-shadow: 0 0 12px rgba(88, 101, 242, 0.25) !important;
                }
                
                div[data-testid="stSelectbox"] svg {
                    fill: white !important;
                }

                div[data-testid="stSelectbox"] label {
                    font-size: 0.95rem !important;
                    font-weight: 600 !important;
                    color: #A2B4FF !important;
                    margin-bottom: 0.5rem !important;
                }

                /* File uploader styling */
                div[data-testid="stFileUploader"] section {
                    background-color: rgba(255, 255, 255, 0.02) !important;
                    border: 1px dashed rgba(255, 255, 255, 0.15) !important;
                    border-radius: 1rem !important;
                    padding: 1.5rem !important;
                    transition: all 0.3s ease !important;
                }
                div[data-testid="stFileUploader"] section:hover {
                    background-color: rgba(255, 255, 255, 0.04) !important;
                    border-color: #5865F2 !important;
                }

                /* Audio input widget */
                div[data-testid="stAudioInput"] {
                    background-color: rgba(255, 255, 255, 0.03) !important;
                    border: 1px solid rgba(255, 255, 255, 0.08) !important;
                    border-radius: 1rem !important;
                    padding: 10px !important;
                }

                /* Camera input widget */
                div[data-testid="stCameraInput"] {
                    border: 1px solid rgba(255, 255, 255, 0.08) !important;
                    border-radius: 1rem !important;
                    padding: 10px !important;
                    background-color: rgba(255, 255, 255, 0.03) !important;
                    overflow: hidden !important;
                }

                /* Subject Card hover styling */
                .subject-card {
                    background: rgba(255, 255, 255, 0.04) !important;
                    backdrop-filter: blur(12px) !important;
                    -webkit-backdrop-filter: blur(12px) !important;
                    border: 1px solid rgba(255, 255, 255, 0.1) !important;
                    border-left: 6px solid #EB459E !important;
                    padding: 25px !important;
                    border-radius: 20px !important;
                    margin-bottom: 20px !important;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2) !important;
                    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
                }
                .subject-card:hover {
                    background: rgba(255, 255, 255, 0.06) !important;
                    border-color: rgba(235, 69, 158, 0.3) !important;
                    box-shadow: 0 12px 40px rgba(235, 69, 158, 0.15) !important;
                    transform: translateY(-4px) !important;
                }

                /* Dialog/Modal customization */
                div[role="dialog"] {
                    background-color: rgba(14, 16, 47, 0.95) !important;
                    backdrop-filter: blur(20px) !important;
                    border: 1px solid rgba(255, 255, 255, 0.1) !important;
                    border-radius: 1.5rem !important;
                    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6) !important;
                }
                div[role="dialog"] h1, div[role="dialog"] h2, div[role="dialog"] h3 {
                    color: white !important;
                }

                /* Alert messages styling */
                div[data-testid="stNotification"] {
                    border-radius: 1rem !important;
                    border: 1px solid rgba(255, 255, 255, 0.1) !important;
                    backdrop-filter: blur(10px) !important;
                }
                div[data-testid="stNotification"] [data-testid="stMarkdown"] p {
                    color: white !important;
                    font-weight: 500 !important;
                }

                /* Table/DataFrame customization */
                div[data-testid="stDataFrame"] {
                    border: 1px solid rgba(255, 255, 255, 0.1) !important;
                    border-radius: 1rem !important;
                    overflow: hidden !important;
                }

                /* Divider line color */
                hr {
                    border-color: rgba(255, 255, 255, 0.1) !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    


    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 900 !important;
                font-size: clamp(2rem, 5vw, 3.5rem) !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                letter-spacing: -1px !important;
            }
                

            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 800 !important;
                font-size: clamp(1.5rem, 3.5vw, 2.2rem) !important;
                line-height:1.2 !important;
                margin-top: 2rem !important;
                margin-bottom: 1.2rem !important;
                letter-spacing: -0.5px !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;    
            }

            h3 {
                font-size: clamp(1.1rem, 2.5vw, 1.6rem) !important;
            }
                
            .glow-title {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 900 !important;
                font-size: clamp(2.5rem, 6vw, 4rem) !important;
                background: linear-gradient(135deg, #FFFFFF 0%, #A2B4FF 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 30px rgba(162, 180, 255, 0.15);
                margin-bottom: 0.5rem !important;
                text-align: center;
            }

            .role-title {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 800 !important;
                font-size: clamp(1.3rem, 3vw, 2rem) !important;
                color: #FFFFFF !important;
                text-align: center;
                margin-bottom: 1.5rem !important;
                background: linear-gradient(135deg, #FFFFFF, #B9C6FF);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            div.stButton {
                text-align: center !important;
                margin-top: 1.5rem !important;
            }

            div.stButton > button {
                width: 100% !important;
                display: inline-flex !important;
                justify-content: center !important;
                align-items: center !important;
            }

            /* Images styled inside background home */

            button{
                border-radius: 2rem !important;
                background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%) !important;
                color: white !important;
                padding: 12px 28px !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                font-size: 1.05rem !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                box-shadow: 0 4px 15px rgba(88, 101, 242, 0.3) !important;
                transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
                }

            button[kind="secondary"]{
                border-radius: 2rem !important;
                background: linear-gradient(135deg, #EB459E 0%, #C43580 100%) !important;
                color: white !important;
                padding: 12px 28px !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                font-size: 1.05rem !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                box-shadow: 0 4px 15px rgba(235, 69, 158, 0.3) !important;
                transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
                }

            button[kind="tertiary"]{
                border-radius: 2rem !important;
                background: rgba(255, 255, 255, 0.06) !important;
                color: white !important;
                padding: 12px 28px !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                font-size: 1.05rem !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                backdrop-filter: blur(5px) !important;
                transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
                }

            button:hover{
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(88, 101, 242, 0.5) !important;
                border-color: rgba(255, 255, 255, 0.2) !important;
            }

            button[kind="secondary"]:hover {
                box-shadow: 0 8px 25px rgba(235, 69, 158, 0.5) !important;
            }

            button[kind="tertiary"]:hover {
                background: rgba(255, 255, 255, 0.12) !important;
                box-shadow: 0 8px 25px rgba(255, 255, 255, 0.08) !important;
            }
        </style>  

                """
            ,unsafe_allow_html=True)