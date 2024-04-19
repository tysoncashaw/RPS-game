import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.write(f" {st.session_state['game_message']}")
if st.button("Play Again!"):
    del st.session_state['computer_choice']
    switch_page("Game")
