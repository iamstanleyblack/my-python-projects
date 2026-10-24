import random


def main():
    print("Stanley Black Academy")
    print(f"What is {randone} + {randtwo} + {randthree}")
    answer = int(input("Your answer: "))

    while answer != total:
        randone = random.randint(1, 99) #random.randint(1, 99)
        randtwo = random.randint(1, 99)
        randthree = random.randint(1, 99)

        total = f"{randone} + {randtwo} + {randthree}"

        if answer != total:
            print("Incorrect.")
            print(f"The expected answer is {total}")
        else:
            print("Correct!")
        

    print("Congratulations! You have found the correct answer")

if __name__ == '__main__':
    main()