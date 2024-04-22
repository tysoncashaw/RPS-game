import streamlit as st
from st_pages import hide_pages
from streamlit_extras.switch_page_button import switch_page
from random import randint


def init_pages():
    st.set_page_config(
        page_title="RPS Game",
        initial_sidebar_state="collapsed"
    )
    hide_pages(['rps','Game','Loser','Winner', 'Tie'])

def check_if_tie(player_choice):
    if st.session_state['computer_choice'] == player_choice:
        switch_page("Tie")
    else:
       return False


def check_for_winner(player_choice):
    computer_choice = st.session_state['computer_choice']
    if player_choice == "Rock":
        if computer_choice == "Scissors":
            navigate_to("Winner","You win! Rock smashes Scissors." )
        elif computer_choice == "Paper":
            navigate_to("Loser", "You lose! Paper covers Rock.")
        
    if player_choice == "Paper":
        if computer_choice == "Rock":
            navigate_to("Winner", "You win! Paper covers Rock.")
        elif computer_choice == "Scissors":
            navigate_to("Loser","You lose! Scissors cut Paper." )
    
    if player_choice == "Scissors":
        if computer_choice == "Paper":
            navigate_to("Winner","You win! Scissors cut Paper." )
        elif computer_choice == "Rock":
            navigate_to("Loser", "You lose! Rock smashes Scissors.")

def get_computer_choice():
    r = randint(0,2)
    choices = ["Rock","Paper","Scissors"]
    return choices[r]

def navigate_to(page, message):
    if 'game_message' not in st.session_state:
        st.session_state['game_message'] = message
  
    switch_page(page)