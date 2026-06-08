print("Guess a secret_number\n")
# To guess a secret_number ranging between 0 and 20 

secret_number = 13
attempts = 0
print("Guess a number between 0 and 20!")

while True:
    guess =int(input("Enter your guess: "))
    attempts += 1

    if  guess < secret_number:
        print("Too low!")
        
    elif guess > secret_number:
        print("Too High!")
    else:
        print(f"Congratulation! You guessed correct in {attempts} attempts")
        break