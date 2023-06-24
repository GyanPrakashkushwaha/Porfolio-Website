import streamlit as st
from st_clickable_images import clickable_images

class Contact:
    def __init__(self):
        pass

    def contact(self):
        st.markdown("""
            <style>
                .block-container {
                    padding-top: 1.6rem;
                    padding-bottom: 5rem;
                }
            </style>
        """, unsafe_allow_html=True)
        st.title("Contact")

        st.markdown('## [GitHub account:](https://github.com/GyanPrakashkushwaha)')

        
        st.image('github.png')


        st.markdown('---')
        st.markdown('## [Linkedin account:](https://github.com/GyanPrakashkushwaha)')
        
        st.image('linkedin.png')




