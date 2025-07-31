import random


def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = 10
    attempts = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        # Get player's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Validate input range
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue

            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            # Show remaining attempts
            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # If player runs out of attempts
    if attempts == max_attempts and guess != secret_number:
        print(f"Game Over! The number was {secret_number}.")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()


# Start the game
number_guessing_game()