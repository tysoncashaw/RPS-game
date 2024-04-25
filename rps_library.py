import streamlit as st
from st_pages import hide_pages
from streamlit_extras.switch_page_button import switch_page
from random import randint

def init_pages():
    st.set_page_config(
        page_title="RPS Game",
        initial_sidebar_state="collapsed"
    )
    hide_pages(['RPS','Game','Loser','Winner','Tie'])
    
    if 'stat_games_played' not in st.session_state:
        init_statistics()

def init_statistics():
    if 'stat_games_played' not in st.session_state:
        st.session_state['stat_games_played'] = 0

    if 'stat_wins' not in st.session_state:
        st.session_state['stat_wins'] = 0

    if 'stat_losses' not in st.session_state:
        st.session_state['stat_losses'] = 0

    if 'stat_ties' not in st.session_state:
        st.session_state['stat_ties'] = 0

def reset_statistics():
    if 'stat_games_played' in st.session_state:
        del st.session_state['stat_games_played'] 

    if 'stat_wins' in st.session_state:
        del st.session_state['stat_wins'] 

    if 'stat_losses' in st.session_state:
        del st.session_state['stat_losses'] 

    if 'stat_ties' in st.session_state:
        del st.session_state['stat_ties'] 

    
def update_statistics(which_stat):
    match which_stat:
        case 'wins':
            wins = st.session_state['stat_wins']
            st.session_state['stat_wins'] = wins + 1
        case 'games':
            games = st.session_state['stat_games_played']
            st.session_state['stat_games_played'] = games + 1
        case 'losses':
            losses = st.session_state['stat_losses']
            st.session_state['stat_losses'] = losses + 1
        case 'ties':
            ties = st.session_state['stat_ties']
            st.session_state['stat_ties'] = ties + 1
        case _:
            print('Invalid Statistics!')

def check_if_tie(player_choice):
    if st.session_state['computer_choice'] == player_choice:
        update_statistics('ties')
        switch_page("Tie")
    else:
       return False


def check_for_winner(player_choice):
    computer_choice = st.session_state['computer_choice']
    if player_choice == "Rock":
        if computer_choice == "Scissors":
            update_statistics('wins')
            navigate_to("Winner","You win! Rock smashes Scissors." )
        elif computer_choice == "Paper":
            update_statistics('losses')
            navigate_to("Loser", "You lose! Paper covers Rock.")
        
    if player_choice == "Paper":
        if computer_choice == "Rock":
            update_statistics('wins')
            navigate_to("Winner", "You win! Paper covers Rock.")
        elif computer_choice == "Scissors":
            update_statistics('losses')
            navigate_to("Loser","You lose! Scissors cut Paper." )
    
    if player_choice == "Scissors":
        if computer_choice == "Paper":
            update_statistics('wins')
            navigate_to("Winner","You win! Scissors cut Paper." )
        elif computer_choice == "Rock":
            update_statistics('losses')
            navigate_to("Loser", "You lose! Rock smashes Scissors.")

def get_computer_choice():
    r = randint(0,2)
    choices = ["Rock","Paper","Scissors"]
    return choices[r]

def navigate_to(page, message):
    if 'game_message' not in st.session_state:
        st.session_state['game_message'] = message
  
    switch_page(page)