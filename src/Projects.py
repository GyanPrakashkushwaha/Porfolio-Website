import streamlit as st

class Projects:
    def __init__(self):
        st.markdown("""
            <style>
                .block-container {
                    padding-top: 1.6rem;
                    padding-bottom: 5rem;
                }
            </style>
        """, unsafe_allow_html=True)

    def Project(self):
        project_dmo = project_demo()
        project_dmo.face_mask_detection_project()

        st.markdown('---')
        project_dmo.laptop_price_prediction()



        
class project_demo:
    def __init__(self):
        pass

    def face_mask_detection_project(self):
        with st.container():
            st.header('  1️⃣. Face Mask detection Project 😷')
            st.video('data\Face_mask_detection.mp4')
            st.markdown('Project Link : https://github.com/GyanPrakashkushwaha/FaceMaskDetection')

        
    def laptop_price_prediction(self):
        with st.container():
            st.header('  2️⃣. Laptop Price Prediciton 💻')
            st.image('data\Screenshot (38).png',width=700)
            st.markdown('Project Link : https://github.com/GyanPrakashkushwaha/LaptopPricePrediction_Project')
    
