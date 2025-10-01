import streamlit as st
from rps_library import init_pages

if __name__ == "__main__":
    init_pages()
    
    st.header("Welcome to the Rock Paper Scissors Game!")

   
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Play Game"):
            st.switch_page("pages/Game.py")

    with col3:
        if st.button("Exit Game"):
            link = '[Exit Really?](http://tysoncashaw.com)'
            st.markdown(link, unsafe_allow_html=True)