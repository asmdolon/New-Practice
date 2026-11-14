
import random
import time

def show_intro():
    print("=" * 40)
    print("       NUMBER GUESSING BATTLE")
    print("=" * 40)
    print("Welcome to the game!")
    print("Guess the secret number to win!")
    print("=" * 40)


def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1-20)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        return 20, 10
    elif choice == "2":
        return 50, 7
    elif choice == "3":
        return 100, 5
    else:
        print("Invalid choice! Defaulting to Easy.")
        return 20, 10


def play_game():
    max_number, attempts = choose_difficulty()

    secret_number = random.randint(1, max_number)
    score = 100
    used_attempts = 0

    print("\nComputer is choosing a number...")
    time.sleep(1)
    print(f"I have selected a number between 1 and {max_number}!")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        print(f"Current Score: {score}")

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > max_number:
            print("Number is out of range!")
            continue

        used_attempts += 1
        attempts -= 1

        if guess == secret_number:
            print("\nCONGRATULATIONS! YOU WON!")
            print(f"Secret Number: {secret_number}")
            print(f"Attempts Used: {used_attempts}")
            print(f"Final Score: {score}")
            return score

        elif guess < secret_number:
            print("Too LOW! Try a higher number.")

        else:
            print("Too HIGH! Try a lower number.")

        score = max(0, score - 10)

        if attempts > 0:
            hint = input("Want a hint? (yes/no): ").lower()

            if hint == "yes":
                if secret_number % 2 == 0:
                    print("Hint: The number is EVEN.")
                else:
                    print("Hint: The number is ODD.")

    print("\nGAME OVER!")
    print(f"The secret number was: {secret_number}")
    return 0


def main():
    total_score = 0

    show_intro()

    while True:
        earned = play_game()
        total_score += earned

        print("\nTotal Score:", total_score)

        again = input("\nPlay Again? (yes/no): ").lower()

        if again != "yes":
            break

    print("\nThanks for playing!")
    print("Your Final Total Score:", total_score)


if __name__ == "__main__":
    main()
