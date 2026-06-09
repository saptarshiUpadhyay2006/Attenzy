import streamlit as st
from src.components.header import header_home 
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():
    header_home()
    
    style_background_home()
    style_base_layout()

    # Custom css for metrics and cards on home screen
    st.markdown("""
        <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            width: 100%;
            margin-bottom: 2rem;
        }
        .metrics-grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            width: 100%;
            margin-bottom: 2rem;
        }
        .feature-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 1.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
            min-height: 160px;
            height: auto;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .feature-card:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(88, 101, 242, 0.3);
            transform: translateY(-4px);
        }
        .feature-title {
            color: #FFFFFF !important;
            font-size: 1.25rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.5rem !important;
        }
        .feature-desc {
            color: #C4D1FF !important;
            font-size: 0.95rem !important;
            line-height: 1.4 !important;
        }
        .stat-card {
            text-align: center;
            background: linear-gradient(135deg, rgba(88, 101, 242, 0.06) 0%, rgba(235, 69, 158, 0.06) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 1.5rem;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }
        .stat-card:hover {
            background: linear-gradient(135deg, rgba(88, 101, 242, 0.1) 0%, rgba(235, 69, 158, 0.1) 100%);
            transform: translateY(-2px);
        }
        .stat-val {
            font-size: 2.2rem !important;
            font-weight: 900 !important;
            color: #FFFFFF !important;
            margin-bottom: 0.25rem !important;
            background: linear-gradient(135deg, #FFFFFF, #B9C6FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stat-label {
            font-size: 0.9rem !important;
            color: #A2B4FF !important;
            font-weight: 600 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Subtitle Tagline
    st.markdown("<p style='text-align:center; font-size:1.3rem; margin-top:-20px; margin-bottom:40px; color:#C4D1FF;'>Smart, secure, and seamless AI attendance using facial & voice biometrics.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1: 
        st.markdown("<h2 class='role-title'>I'm Teacher</h2>", unsafe_allow_html=True)
        st.image("assets/teacher.svg", width=240)
        if st.button('Teacher Portal', type="primary", icon=':material/arrow_outward:', key='teacher_portal_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col2:
        st.markdown("<h2 class='role-title'>I'm Student</h2>", unsafe_allow_html=True)
        st.image("assets/student.svg", width=240)
        if st.button('Student Portal', type="primary", icon=':material/arrow_outward:', key='student_portal_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    # Metrics Section
    st.markdown("<h2 class='home-section-title'>Metrics That Matter</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='metrics-grid-container'>
            <div class='stat-card'>
                <div class='stat-val'>99.8%</div>
                <div class='stat-label'>Recognition Accuracy</div>
            </div>
            <div class='stat-card'>
                <div class='stat-val'>&lt; 3s</div>
                <div class='stat-label'>Average Scan Time</div>
            </div>
            <div class='stat-card'>
                <div class='stat-val'>100%</div>
                <div class='stat-label'>Automated & Paperless</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("<h2 class='home-section-title'>Core Capabilities</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='grid-container'>
            <div class='feature-card'>
                <div class='feature-title'>🤖 Face Recognition</div>
                <div class='feature-desc'>Verify entire classrooms instantly. Built using cutting-edge facial embeddings and secure classifiers.</div>
            </div>
            <div class='feature-card'>
                <div class='feature-title'>🎙️ Voice Enrollment</div>
                <div class='feature-desc'>Multi-factor validation. Students verify presence using neural voice print recognition.</div>
            </div>
            <div class='feature-card'>
                <div class='feature-title'>📊 Analytics Records</div>
                <div class='feature-desc'>Access real-time visual records, view subject analytics, and export student attendance logs easily.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # FAQs Section
    st.markdown("<h2 class='home-section-title'>Frequently Asked Questions</h2>", unsafe_allow_html=True)
    
    with st.expander("How does the face recognition system work?"):
        st.write("Attenzy processes uploaded classroom photos or live camera inputs, extracting unique 128-dimensional facial embeddings. These are matched against enrolled student records in real time using a pre-trained SVM classifier.")

    with st.expander("Is my personal biometric data safe?"):
        st.write("Yes! We prioritize privacy. The app does not save any image or audio records. Instead, secure vector embeddings (numerical maps) are extracted and safely stored in the database for presence verification.")

    with st.expander("What should I do if my face is not recognized?"):
        st.write("Ensure you face the camera directly in a well-lit space. If you are a new student, register your profile first using the 'Register New Profile' option in the Student Portal.")

    st.space()
    footer_home()