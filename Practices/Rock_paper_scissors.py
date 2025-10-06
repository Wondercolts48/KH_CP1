# Kh 2nd Rock, paper, scissors practice

import random

score = 0
user_score = 0
choices = ["rock", "paper", "scissors"]

game = input("Welcome to Rock, Paper, Scissors! Would you like to play today? ")
if game == "yes":
    print("then let's start the game!")
    

while game:
    user = ("rock", "paper", "scissors")
    input("Choose, rock, paper, or scissors")
    computer = random.choice(choices)

if user == computer:
    print("HA, it's a tie!")
    user_score += 0
elif (user == "paper" and computer == "scissors"):
    print("I win! ")
    user_score += 1