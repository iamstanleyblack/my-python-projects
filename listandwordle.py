import random
"""
Making a game similar to the wordle I just made in the code in place x section
I am going to start begin with a flow chart of everything from the instructions to the very first thing I need to do
1. Make a list of words
2. make an empty list
3. Prompt user to input their guess
4. Check whether the word is same as the word in the list/secret word
5. Print the congratulations
"""

list_of_words = ["candy", "lollipop", "sweet", "cucumber", "cookie", "biscuit", "milk", "chocolate"]
secret_word = random.choice(list_of_words)


user_guess = input("Enter your guess here: ")
if user_guess == secret_word:
    print("Fantastic! You got this right.")
    print(f"The answer was {user_guess}")
else:
    print("Try again next time")
