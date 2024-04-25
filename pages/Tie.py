import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from rps_library import init_pages

def show_tie_message():
    st.write("Tie!")
    if st.button("Play Again!"):
        del st.session_state['computer_choice']
        switch_page("Game")

if __name__ == "__main__":
    init_pages()
    show_tie_message()