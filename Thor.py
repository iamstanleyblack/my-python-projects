import random

NUM_DIGITS = 7
MAX_GUESSES = 10

def main():
    print (f'''Mukzard is a deductive logic game by SB, with instructions from AI Sweigart
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:

    When I say:             ->         That means:
            -Odin           ->         One digit is correct but in the wrong position

            -Thor           ->         One digit is correct and in the right position

            -Loki           ->         No digit is correct
For example, if the secret number was 248 and your guess was 843, the clues would be Thor Odin.''')


    # The next code block is the main game loop
    while True: 
        #To store the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it right.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ') # We store the number of guesses the user has made so far
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct, so break out of this loop

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNum}')

        #Ask player if they wanna play again
        print('Do you want to play again?(yes or no)')
        if not input('> ').lower().startswith('y'):
            print('Thanks for playing!')
            break


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') #Creating a list of digits from 0 to 9
    random.shuffle(numbers) # Shuffle them into random order

    #ggetting the first NUM_DIGITS digits in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the odin, loki and thor clues for a guess and a seret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit is in the correct plac
            clues.append('Thor')
        elif guess[i] in secretNum:
            # a correct digit is in the incorrect place.
            clues.append('Odin')


    if len(clues) == 0:
        return 'Mukzard' #Meaning there are no correct digits at all

    else:

        # Sort the clues into alphabetical order so their original order
        #doesn't give information away
        clues.sort()
        #Make a single string from the list of string clues.

        return ''.join(clues)


if __name__ == '__main__':
    main()
