import random

secret_number = random.randint(1, 99)
# print(f"The secret number is: {secret_number}")
# print("I a thinking of a number between 1 and 99...")

# guessed_yet = 0
# while guessed_yet:
#     answer = int(input("Enter a guess: "))
#     if answer > RANDOM_NUMBER:
#         print("Your guess is too high")
#         print(answer)
#     elif answer < RANDOM_NUMBER:
#         print("Your guess is too low")
#         print(answer)
#     else:
#         print(f"Congrats! The number was: {answer}")
#         guessed_yet = 1


guess = int(input("Enter a guess: "))
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low.")
    guess = int(input("Enter another guess: "))

print(f"Congrats! The secret number was {guess}")