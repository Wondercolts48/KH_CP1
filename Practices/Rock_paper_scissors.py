# Kh 2nd Rock, paper, scissors practice

import random

choices = ["rock", "paper", "scissors"]
score_user = 0
bot_score = 0
print("Welcome to Rock, Paper, Scissors!\nQuit: 'q'\nrock: 'r\npaper: 'p")
    

while True:
    player_choice = input("Choose, rock, paper, or scissors:\n")
    computer = random.choice(choices)

    if player_choice == "quit":
        print("This is your score", score_user, "This is my score", bot_score)
        break
                
    elif player_choice == "rock":
        if computer == "rock":
            print("It's a tie!")
        elif computer == "scissors":
            print("Ha, You won me.")
            score_uesr = score_user + 1
        elif computer == "paper":
            print("Ha, I won you.")
            bot_score = bot_score + 1

    elif player_choice == "paper":
        if computer == "paper":
            print("It's a tie!")
        elif computer == "scissors":
            print("Ha, I won!.")
            bot_score = bot_score + 1
        elif computer == "paper":
            print("Dang, you won.")
            score_user = score_user + 1

    elif player_choice == "scissors":
        if computer == "scissors":
            print("It's a tie!")
        elif computer == "paper":
            print("Ha, You won me.")
            score_user = score_user + 1
        elif computer == "rock":
            print("Ha, I won you.")
            bot_score = bot_score + 1

        
        else:
            print("Try again")
