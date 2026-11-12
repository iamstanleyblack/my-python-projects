# How many points each letter's worth is, in my scrabble game

POINTS = {
    "a": 1, "e": 1, "i": 1, "l": 1, "n": 1, "o": 1,
    "r": 1, "s": 1, "t": 1, "u": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10,
}

def score(word):
    # Return the number of points that the given word is worth
    points = 0
    for letter in word:
       # print(letter)
        points += POINTS[letter]
    return points
def main():
    word = input("Enter a word: ").lower()
    while word != "":
        points = score(word)
        print(f"{word} is equal to {points} points")
        word = input("Enter a word: ")
if __name__ == '__main__':
    main() 
