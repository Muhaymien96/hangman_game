import random


def hangman():
    words_list = ["python", "java", "swift", "javascript"]
    words = random.choice(words_list)
    hidden_answer = list(len(words) * '-')
    attempts = 8
    typed = ""
    while attempts > 0 and ''.join(hidden_answer) != words:
        guess = input(f"{''.join(hidden_answer)}\nInput a letter: \n")
        if len(guess) != 1:
            print("Please, input a single letter.\n")
            continue
        elif not (guess.islower() and guess.isalpha()):
            print("Enter a lowercase letter from the English alphabet.\n")
            continue
        if guess in typed:
            print("You've already guessed this letter.\n")
        elif guess in words:
            for check in range(len(words)):
                if words[check] == guess:
                    hidden_answer[check] = guess
        else:
            print("That letter doesn't appear in the word.\n")
            attempts -= 1
        typed += guess

    if ''.join(hidden_answer) == words:
        print(f"You guessed the word {words}!\nYou survived!")
        return True
    else:
        print(f"Sorry, the word was {words}. You lost!")
        return False


def show_score(wins, losses):
    wins_str = "times"
    losses_str = "times"
    print(f"You won: {wins} {wins_str}.")
    print(f"You lost: {losses} {losses_str}.")


def main():
    wins = 0
    losses = 0

    while True:
        choice = input('Print Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

        if choice == "play":
            result = hangman()
            if result:
                wins += 1
            else:
                losses += 1
        elif choice == "results":
            show_score(wins, losses)
        elif choice == "exit":
            break
        else:
            print("Please choose from 'play', 'results', or 'exit'.")


if __name__ == "__main__":
    main()
