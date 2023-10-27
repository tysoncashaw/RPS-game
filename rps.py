from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

computer =t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose...", computer, "cut", player)
        else:
            print("Yout win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("Your win!", player, "cut", computer)
    else:
        print("Thats not a valid play. Check your spelling!")

    player = False 
    computer = t[randint(0,2)]    