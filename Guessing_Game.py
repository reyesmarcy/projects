def display_title():
    print("Guess the number")
    print()
    print("I'm thinking of a number from 1 to 10")
    print()

def play_game():
    import random

    random_number = random.randint(1,11)
    your_guess = 0
    guess_count = 0

    while your_guess != random_number:
        your_guess = int(input("Your guess: "))

        guess_count += 1

        if your_guess < 1 or your_guess > 11:
            print("This is not a valid number. Try again.")
        elif your_guess > random_number:
            print("Too high.")
        elif your_guess < random_number:
            print("Too low.")
        elif your_guess == random_number:
            print("You guessed it in {} tries!".format(guess_count))


def main():
    display_title()

    choice = "y"
    while choice.lower() == "y":
        play_game()
        print()
        choice = input("Would you like to play again? (y/n): ")
        print()
    print("cya")

if __name__ == "__main__":
    main()



