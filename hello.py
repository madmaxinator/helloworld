import random


def play_game():
    random.seed(0)
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("You guessed it!")
    else:
        print(f"Sorry, the number was {number}.")


if __name__ == "__main__":
    print("HELLOWORLD")
    play_game()

