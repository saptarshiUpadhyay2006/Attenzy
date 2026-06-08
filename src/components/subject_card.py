import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="subject-card">
        <h3 style="margin:0; color: #FFFFFF; font-size: 1.5rem; font-family: 'Outfit', sans-serif; font-weight: 700;">{name}</h3>
        <p style="color:#C4D1FF; margin:10px 0; font-family: 'Outfit', sans-serif; font-size: 0.95rem;">Code : <span style="background:rgba(255, 255, 255, 0.08); color:#A2B4FF; padding:3px 10px; border-radius:8px; border: 1px solid rgba(255, 255, 255, 0.1); font-weight: 600;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top: 15px;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(235, 69, 158, 0.12); color:#FFFFFF; padding:6px 14px; border-radius:12px; font-size:0.9rem; border: 1px solid rgba(235, 69, 158, 0.2); font-family: \'Outfit\', sans-serif; display: flex; align-items: center; gap: 6px;"><span>{icon}</span> <b style="color:white; font-size: 1rem;">{value}</b> <span style="color:#C4D1FF; font-size: 0.85rem;">{label}</span> </div>'
        
        html+= "</div>"
    html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()