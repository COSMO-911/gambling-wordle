from random import choice

def start_game():
    print("\n" + "="*30)
    print("WELCOME TO WORDLE GAMBLING")
    print("="*30)
    
    balance = 10000
    try_again = "y"
    
    while try_again == "y":
        try:
            bet = float(input(f"\nCurrent Balance: ${balance}\nEnter bet amount: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if bet > balance:
            print("You don't have enough money for that bet!")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            break

        # Load words
        try:
            with open("random-words.txt", "r") as file:
                words = file.read().splitlines()
            target = choice(words).lower()
        except FileNotFoundError:
            print("Error: 'random-words.txt' not found!")
            break

        print("You have 10 chances to guess the 5-letter word.")
        user_chances = 10
        user_won = False
        for i in range(1, user_chances+1):
            guess = input(f"Guess {i}: ").lower()
            if len(guess) != 5:
                print("Must be 5 letters!")
                continue

            result = ""
            for x in range(5):
                if guess[x] == target[x]:
                    result += "🟩"
                elif guess[x] in target:
                    result += "🟨"
                else:
                    result += "⬛"
            print(result)

            if guess == target:
                print("YOU WON!")
                balance += bet
                user_won = True
                break
        
        if not user_won:
            print(f"Lost! The word was: {target}")
            balance -= bet

        if balance <= 0:
            print("You are out of money! Game Over.")
            break

        print(f"Current Balance: ${balance}")
        try_again = input('Wanna play again?(y/n): ').lower()
        if try_again == "n":
            print("99% of people give up before winning big!")
            try_again = input('Wanna play again?(y/n): ').lower()
            if try_again == 'n':
                break

    print("Thank you for gambling, come again!")