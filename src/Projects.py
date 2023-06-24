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

        st.markdown('---')
        project_dmo.age_gender_prediction()



        
class project_demo:
    def __init__(self):
        pass

    def face_mask_detection_project(self):
        with st.container():
            st.header('  1️⃣. Face Mask detection Project 😷')
            st.video('data\Face_mask_detection.mp4')
            st.markdown('#### Project Link : https://github.com/GyanPrakashkushwaha/FaceMaskDetection')

        
    def laptop_price_prediction(self):
        with st.container():
            st.header('  2️⃣. Laptop Price Prediciton 💻')
            st.image('data\Screenshot (38).png',width=700)
            st.markdown('#### Project Link : https://github.com/GyanPrakashkushwaha/LaptopPricePrediction_Project')

    def age_gender_prediction(self):
        with st.container():
            st.header('  3️⃣. Age Gender Prediciton 🧒')
            st.video('data\Age-GenderDetection.mp4')
            st.markdown('#### Project Link : https://github.com/GyanPrakashkushwaha/AgeGender-Prediciton/tree/main/notebook')
            st.markdown('#### Blog link : https://medium.com/@gyanp7880/the-power-of-functional-api-deep-learning-predicting-two-output-age-and-gender-simultaneously-371f1c5b181e')
    
