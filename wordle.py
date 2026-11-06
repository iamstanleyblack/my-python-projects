from words import get_random_word

NUM_ATTEMPTS = 6

def main():
    # Print welcome message
    print("Welcome to Wordle!")

    # Set the secret word
#    secret_word = get_random_word()
    secret_word = input("Player 1, type a secret 5-letter word: ").lower()
    for i in range(30):
        print()
    # Let the player guess up to NUM_ATTEMPTS
    for attempt in range(NUM_ATTEMPTS):

        # Get the guess from the user
        guess = input("Enter your guess: ").lower()
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()

        # Initialize remaining_letters to contain
        # the remaining letters in the secret word
        remaining_letters = []
        for i in range(5):
            remaining_letters.append(secret_word[i])

        # Compare the guess to the secret word
        result = []
        for i in range(5):
            if secret_word[i] == guess[i]:
                # It's a match!
                result.append("G")

                # Update the remaining letters
                remaining_letters.remove(secret_word[i])
            else:
                # Not an exact match
                result.append("B")

        # Look for the yellow letters
        for i in range(5):
            # Look for letters that were not exact matches
            if result[i] == "B":
                # Check if the guessed letter is somewhere else in the secret word
                if guess[i] in remaining_letters:
                    result[i] = "Y"
                    remaining_letters.remove(guess[i])

        # Build a string from the list and print the result
        result_str = "Result:"
        for i in range(5):
            # Append each letter using an f string
            if result[i] == "G":
                # Put the letter in brackets
                result_str = f"{result_str} [{guess[i]}]"

            if result[i] == "Y":
                # Put the letter in parentheses
                result_str = f"{result_str} ({guess[i]})"

            if result[i] == "B":
                result_str = f"{result_str} {guess[i]}"

        # Print out the result string
        print(result_str)

        # Check if they got it correct
        if secret_word == guess:
            print(f"Congratulations! You guessed the word in {attempt + 1} tries!")
            break

        # Check if it's their last attempt
        if attempt == NUM_ATTEMPTS - 1:
            print(f"Better luck next time! The correct word was '{secret_word}'.")

if __name__ == "__main__":
    main()
