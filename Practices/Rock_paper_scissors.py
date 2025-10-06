# Kh 2nd Rock, paper, scissors practice

import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!\nQuit: 'q'\nRock: 'r\nPaper: 'p")
    

while True:
    player_choice = input("Choose, rock, paper, or scissors:\n")
    computer = random.choice(choices)

    if player_choie == "quit":
        break
                
    elif player_choice == "rock"
        if computer == "rock":
            print("tie")
        elif computer == "scissors":
            print("Ha, You won me.")
        elif computer == "paper":
            print("Ha, I won you.")

    elif player_choice == "paper"

    elif player_choice == "scissors"

    else:
        print("Try again")