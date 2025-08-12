# 🎯 Number Guessing Game

A simple **Python terminal game** where the player tries to guess a random number within a limited number of chances.

## 📜 Description
This is a beginner-friendly project that uses:
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Random number generation (`random.randint`)
- User input with `input()`

The game gives the player **7 chances** to guess the correct number within a given range. After each round, the player can choose to play again.

---

## 🚀 How to Run
1. Make sure you have **Python 3** installed.
2. Save the game code into a file named `number_guessing_game.py`.
3. Open a terminal (or command prompt) and run:
   ```bash
   python number_guessing_game.py
🕹 How to Play
The game will ask you for:

A starting number (smallest possible number).

An ending number (largest possible number).

The program will secretly pick a random number between your start and end.

You will have 7 chances to guess the number.

After each guess:

If correct → 🎉 You win!

If incorrect → You’ll be told if it’s too high or too low.

If you use all chances without guessing correctly → The number will be revealed.

You can choose to play again or quit.

📂 Example Gameplay
mathematica
Copy
Edit
Hi! Welcome to the Number Guessing Game.
You have 7 chances to guess the number. Let's start!
Enter Starting Number: 1
Enter Ending Number: 10
Enter Your Guess: 5
Too low!
Enter Your Guess: 8
Too high!
Enter Your Guess: 7
🎉 Congratulations! You guessed it in 3 tries.
Do you want to play again? (y/n): n
Thanks for playing! Goodbye! 😊
🛠 Features
Custom number range

7 chances to guess

Hints: "Too high" or "Too low"

Play again option

💡 Ideas for Improvement
Add difficulty levels (Easy, Medium, Hard).

Allow the player to choose the number of chances.

Improve input validation (handle non-integer inputs).

Use functions to organize the code better.

📄 License
This project is free to use for learning purposes.
