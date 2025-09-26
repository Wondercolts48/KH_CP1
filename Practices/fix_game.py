# Kh 2nd 2nd fixing the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0 
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))  #Had to put as an interger. Run-time error
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.") 
            game_over = True
        elif guess == number_to_guess:      # Supposed to be a elif not an if. It was a logic error
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts = attempts + 1     # Attempts had to go up everytime you guessed. Logic Error
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts = attempts + 1   # Attempts had to go up everyime you guessed. Logical Error
        #logic error. The erorr was the continue redundant.
    print("Game Over. Thanks for playing!")
start_game()