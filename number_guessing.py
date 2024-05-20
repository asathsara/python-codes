import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        attempts += 1
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")


if __name__ == "__main__":
    number_guessing_game()
