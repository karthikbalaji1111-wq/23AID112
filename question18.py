secret_number = 7

guess_number = int(input("Guess the number: "))

while guess_number != secret_number:
    if guess_number > secret_number:
        print("Too high")
    else:
        print("Too low")
    
    guess_number = int(input("Guess again: "))

print("Correct! You guessed the number.")
