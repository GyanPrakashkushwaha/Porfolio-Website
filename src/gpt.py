import streamlit as st
option_names = ["a", "b", "c"]

output_container = st.empty()

next = st.button("Next/save")

if next:
    if st.session_state["radio_option"] == 'a':
        st.session_state.radio_option = 'b'
    elif st.session_state["radio_option"] == 'b':
        st.session_state.radio_option = 'c'
    else:
        st.session_state.radio_option = 'a'

option = st.sidebar.radio("Pick an option", option_names , key="radio_option")
st.session_state

if option == 'a':
    output_container.write("You picked 'a' :smile:")
elif option == 'b':
    output_container.write("You picked 'b' :heart:")
else:
    output_container.write("You picked 'c' :rocket:")