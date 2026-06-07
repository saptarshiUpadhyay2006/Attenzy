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

                .stApp {
                    background: radial-gradient(circle at top right, #1F235A, #0E102F, #050614) !important;
                }

                .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
                    color: #FFFFFF !important;
                }

                .stApp p, .stApp label, .stApp span, .stApp div[data-testid="stMarkdown"] p {
                    color: #C4D1FF !important;
                }

                /* Columns remain transparent layout blocks in dashboard */

                /* Text inputs inside dashboard */
                div[data-testid="stTextInput"] input {
                    background-color: rgba(255, 255, 255, 0.05) !important;
                    color: white !important;
                    border: 1px solid rgba(255, 255, 255, 0.1) !important;
                    border-radius: 0.8rem !important;
                    padding: 10px 15px !important;
                    transition: all 0.3s ease !important;
                }
                
                div[data-testid="stTextInput"] input:focus {
                    border-color: #5865F2 !important;
                    box-shadow: 0 0 10px rgba(88, 101, 242, 0.3) !important;
                }

                /* Selectboxes inside dashboard */
                div[data-testid="stSelectbox"] > div > div {
                    background-color: rgba(255, 255, 255, 0.05) !important;
                    color: white !important;
                    border: 1px solid rgba(255, 255, 255, 0.1) !important;
                    border-radius: 0.8rem !important;
                }
                
                div[data-testid="stSelectbox"] svg {
                    fill: white !important;
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
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                letter-spacing: -1px !important;
            }
                

            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 800 !important;
                font-size: 2.2rem !important;
                line-height:1.2 !important;
                margin-top: 2rem !important;
                margin-bottom: 1.2rem !important;
                letter-spacing: -0.5px !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;    
            }
                
            .glow-title {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 900 !important;
                font-size: 4rem !important;
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
                font-size: 2rem !important;
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