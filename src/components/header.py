import streamlit as st
import base64

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

def header_home():
    logo_b64 = get_base64_image("assets/logo_transparent.png")
    logo_src = f"data:image/png;base64,{logo_b64}" if logo_b64 else "https://i.ibb.co/Kx7sWmDR/logo.png"
    st.markdown(f"""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:10px;">
            <img src="{logo_src}" class="pulse-logo" style="height:180px;" />
            <h1 class="glow-title">Attenzy</h1>
            </div>
                
                """,unsafe_allow_html=True)
    
def header_dashboard():
    logo_b64 = get_base64_image("assets/logo_transparent.png")
    logo_src = f"data:image/png;base64,{logo_b64}" if logo_b64 else "https://i.ibb.co/Kx7sWmDR/logo.png"
    st.markdown(f"""
            <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
            <img src="{logo_src}" style="height:80px;" />
            <h1 style='text-align:left; color:#E0E3FF; white-space:nowrap; font-size:2.2rem !important; margin:0;'>Attenzy</h1>
            </div>
                
                """,unsafe_allow_html=True)