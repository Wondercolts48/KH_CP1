# Kh 2nd Rock, paper, scissors practice

import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!\nQuit: 'q'\nrock: 'r\npaper: 'p")
    

while True:
    player_choice = input("Choose, rock, paper, or scissors:\n")
    computer = random.choice(choices)

    if player_choie == "quit":
        break
                
    elif player_choice == "rock"
        if computer == "rock":
            print("It's a tie!")
        elif computer == "scissors":
            print("Ha, You won me.")
        elif computer == "paper":
            print("Ha, I won you.")

    elif player_choice == "paper"
        if computer == "paper":
            print("It's a tie!")
        elif computer == "scissors":
            print("Ha, I won!.")
        elif computer == "paper":
            print("Dang, you won.")

    elif player_choice == "scissors"
        if computer == "scissors":
            print("It's a tie!")
        elif computer == "paper":
            print("Ha, You won me.")
        elif computer == "rock":
            print("Ha, I won you.")
    else:
        print("Try again")
