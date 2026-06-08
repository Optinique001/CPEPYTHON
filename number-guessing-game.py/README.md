# Guess The Secret Number Game

A simple Python number guessing game where the player tries to guess a secret number between 0 and 20.

The program provides hints after each attempt to help the player guess correctly.

---

## Features

* Interactive command-line gameplay
* Tracks number of attempts
* Gives feedback for incorrect guesses
* Beginner-friendly Python project
* Uses loops, conditionals, and user input

---

## How the Game Works

1. The program selects a secret number.
2. The player enters a guess.
3. The program checks the guess:

   * If the guess is too low, it displays `"Too low!"`
   * If the guess is too high, it displays `"Too high!"`
   * If correct, the player wins
4. The game continues until the correct number is guessed.

---

## Requirements

* Python 3.x

---

## How to Run

1. Clone the repository:

```bash id="1l3ovt"
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate into the project folder:

```bash id="6d6d2w"
cd your-repo-name
```

3. Run the program:

```bash id="6v2v3o"
python main.py
```

---

## Example Gameplay

```text id="h0n4tx"
=== Guess The Secret Number ===

Guess a number between 0 and 20!

Enter your guess: 7
Too low!

Enter your guess: 18
Too high!

Enter your guess: 13

Congratulations! You guessed correctly in 3 attempts.
```

---

## Concepts Practiced

This project helps beginners understand:

* Variables
* Loops (`while`)
* Conditional statements (`if`, `elif`, `else`)
* User input handling
* Counters
* Basic game logic

---

## Future Improvements

Possible upgrades for the project:

* Randomly generated secret number
* Difficulty levels
* Limited attempts
* Score tracking
* Replay feature
* GUI version using Tkinter or Pygame

---

## Author

Developed by Paul Nnaemeka.

---

## License

This project is open-source and free to use for educational purposes.
