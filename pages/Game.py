import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from rps_library import init_pages, check_if_tie, get_computer_choice, check_for_winner

if __name__ == "__main__":
    init_pages()
    st.header("ROCK  PAPER   SCISSORS")
    if 'game_message' in st.session_state:
        del st.session_state['game_message']

    if 'computer_choice' not in st.session_state:
        computer = get_computer_choice()
        st.session_state['computer_choice'] = computer
        
    
    st.write("Choose your weapon: ")
    rock, paper, scissors = st.columns(3)
    with rock:
        if st.button("Rock"):
            if not check_if_tie("Rock"):
                check_for_winner("Rock")
                 
    with paper:
        if st.button("Paper"):
            if not check_if_tie("Paper"):
                check_for_winner("Paper")

    with scissors:
        if st.button("Scissors"):
            if not check_if_tie("Scissors"):    
                check_for_winner("Scissors")
