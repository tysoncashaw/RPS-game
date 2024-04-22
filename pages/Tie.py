import streamlit as st
from streamlit_extras.switch_page_button import switch_page

init_pages()
st.write("Tie!")
if st.button("Play Again!"):
    del st.session_state['computer_choice']
    switch_page("Game")
