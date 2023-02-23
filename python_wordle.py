import random
from wordlist import word_list

# Color codes for correct/incorrect letters. RESET removes color
BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

def wordle():
    import random
    correct_word = random.choice(word_list)
    # Game loop
    game_over = False

    for tries in range(6):
        guessed_word = input("Guess a 5 letter word:\n>").lower()

        # Check each letter
        for i in range(0, 5):
            if guessed_word[i] == correct_word[i]:
                # end will append empty quotes to the end of a text string
                print(f"{BG_GREEN}{guessed_word[i]}{RESET}", end="")
            elif guessed_word[i] in correct_word:
                print(f"{BG_YELLOW}{guessed_word[i]}{RESET}", end="")
            else:
                print(guessed_word[i], end="")
        print("")

        # Check if guess is correct
        if guessed_word == correct_word:
            print("You win!")
            game_over = True
            break

    # End of game
    if not game_over:
        print("Your guess was not correct.")
        print(f"The correct word was {correct_word}.")

wordle()
