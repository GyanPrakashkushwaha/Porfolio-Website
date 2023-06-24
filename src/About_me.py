import streamlit as st

class AboutMe:
    def __init__(self):
        pass

    def aboutme(self):
        st.markdown("""
            <style>
                .block-container {
                    padding-top: 1.6rem;
                    padding-bottom: 5rem;
                }
            </style>
        """, unsafe_allow_html=True)

        with st.container():
            st.title("Hi, I am Gyan Prakash Kushwaha😊")
            st.header("A data scientist from India.")
            st.markdown('---')

            st.markdown('> ### My Journey of Data Science and AI\n > Like many others, my initial interest lay in app development, and I have experience in basic app development. However, as a student whose favorite character is Iron Man and who is curious about how mobile devices can recognize their owners, I realized that my true passion lies in AI. Data science has been my major point of interest for a year now, with a strong focus on deep learning. I am comfortable working with Python.')
            st.markdown('---')

            st.header('Video Resume')
            st.video(data=r'data\Face_mask_detection.mp4')