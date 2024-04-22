import streamlit as st
import sys
from random import randint

def CheckIfTie(computerChoice, playerChoice):
    return playerChoice == computerChoice

def GetComputerChoice():
    t = ["Rock", "Paper", "Scissors"]
    item =t[randint(0,2)]
    st.write("Computer choice is " + item)
    return item

def GetPlayerChoice():
    choice = ""
    rock, paper, scissors = st.columns(3)
    with rock:
        if st.button("Rock"):
            choice = "Rock"
        st.image("limestone.webp")
    with paper:
        if st.button("Paper"):
            choice = "Paper"
        st.image("piece-paper-with-word-organic-it_176841-41450.webp")
    with scissors:
        if st.button("Scissors"):
            choice = "Scissors"
        st.image("tijeras_1_baja.webp")

    return choice

def RPSGame(computer):
    st.write("Computer chooses: " + computer)

    if rock_btn:
        if CheckIfTie(computer, "Rock"):
            st.write("Tie!")
        elif computer == "Paper":
            st.write("You lose... ", computer, "covers Rock")
        else:
            st.write("You win! Rock smashes ", computer)

    
    if paper_btn:
        if CheckIfTie(computer, "Paper"):
            st.write("Tie!")
        elif computer == "Scissors":
            st.write("You lose...", computer, "cut Paper")
        else:
            st.write("You win! Paper covers", computer)


    
    if scissors_btn:
        if CheckIfTie(computer, "Scissors"):
            st.write("Tie!")
        elif computer == "Rock":
            st.write("You lose...", computer, "smashes Scissosrs")
        else:
            st.write("Your win! Scissors cut", computer)



if __name__ == "__main__":
    st.write("Welcome to the Rock Paper Scissors Game!")
    
    computer = GetComputerChoice()
    player = GetPlayerChoice()
    if CheckIfTie(computer,player):
        st.write("Tie!")