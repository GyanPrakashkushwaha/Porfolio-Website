import streamlit as st

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

        st.markdown('### Gmail:  gyanprakashkushwaha95@gmail.com')
        
        st.markdown('---')

        st.markdown('### [GitHub account:](https://github.com/GyanPrakashkushwaha)')

        
        st.image('data\github.png')


        st.markdown('---')
        st.markdown('### [Linkedin account:](https://www.linkedin.com/in/gyan-prakash-kushwaha-412838263/)')
        
        st.image('data\linkedin.png')

        st.markdown('---')
        st.markdown('### [Kaggle account:](https://www.kaggle.com/gyanprakashkushwaha)')
        
        st.image('data\kaggle.png')





