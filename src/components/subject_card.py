import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: rgba(255, 255, 255, 0.04); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom:20px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);">
        <h3 style="margin:0; color: #FFFFFF; font-size: 1.5rem; font-family: 'Outfit', sans-serif;">{name}</h3>
        <p style="color:#C4D1FF; margin:10px 0; font-family: 'Outfit', sans-serif;">Code : <span style="background:rgba(255, 255, 255, 0.08); color:#A2B4FF; padding:2px 8px; border-radius:5px; border: 1px solid rgba(255, 255, 255, 0.1);">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(235, 69, 158, 0.12); color:#FFFFFF; padding:5px 12px; border-radius:12px; font-size:0.9rem; border: 1px solid rgba(235, 69, 158, 0.2); font-family: \'Outfit\', sans-serif;">{icon} <b style="color:white;">{value}</b> <span style="color:#C4D1FF;">{label}</span> </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()