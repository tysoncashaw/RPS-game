import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from rps_library import init_pages

def show_tie_message():
    st.write("Tie!")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play Again!"):
            del st.session_state['computer_choice']
            switch_page("Game")
    with col2:
        if st.button("Exit Game"):
            link = '[Exit Really?](http://tysoncashaw.com)'
            st.markdown(link, unsafe_allow_html=True)

if __name__ == "__main__":
    init_pages()
    show_tie_message()