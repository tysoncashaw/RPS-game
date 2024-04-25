import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from rps_library import init_pages, check_if_tie, get_computer_choice, check_for_winner, update_statistics

if __name__ == "__main__":
    init_pages()
    
    st.header("ROCK  PAPER   SCISSORS")
    if 'game_message' in st.session_state:
        del st.session_state['game_message']

    if 'computer_choice' not in st.session_state:
        computer = get_computer_choice()
        st.session_state['computer_choice'] = computer
        
    
    st.write("Choose your weapon: ")
    main, stats = st.columns([.7, .3], gap = 'large')

    with main:
        rock, paper, scissors = st.columns(3)
        with rock:
            if st.button("Rock"):
                update_statistics('games')
                if not check_if_tie("Rock"):
                    check_for_winner("Rock")
                    
        with paper:
            if st.button("Paper"):
                update_statistics('games')
                if not check_if_tie("Paper"):
                    check_for_winner("Paper")

        with scissors:
            if st.button("Scissors"):
                update_statistics('games')
                if not check_if_tie("Scissors"):    
                    check_for_winner("Scissors")

    with stats: 
        with st.container(border=True):
            st.write("Player Stats")
            st.write("Games Played: " + str(st.session_state['stat_games_played']))
            st.write("Games Won: " + str(st.session_state['stat_wins']))
            st.write("Games Lost: " + str(st.session_state['stat_losses']))
            st.write("Games Tied: " + str(st.session_state['stat_ties']))
