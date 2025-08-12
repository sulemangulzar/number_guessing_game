import random

print(
    "Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!"
)

play_again_or_not = True

while play_again_or_not:
    start_num = int(input("Enter Starting Number: "))
    end_num = int(input("Enter Ending Number: "))

    number = random.randint(start_num, end_num)
    guess_chance = 7
    guesses = 0
    win = False

    while guesses < guess_chance:
        take_guess_input = int(input("Enter Your Guess: "))
        guesses += 1

        if take_guess_input < number:
            print("Too low!")
        elif take_guess_input > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {guesses} tries.")
            win = True
            break

    if not win:
        print(f"Sorry, you ran out of chances! The number was {number}.")

    # Ask to play again after each round
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        play_again_or_not = False

print("Thanks for playing! Goodbye!")
