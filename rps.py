import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from rps_library import init_pages

if __name__ == "__main__":
    init_pages()
    
    st.header("Welcome to the Rock Paper Scissors Game!")
   
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Play Game"):
            switch_page("Game")
