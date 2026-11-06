ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encode(message, n):
    empty = ""
    for i in message:
        if i in ALPHABET:
            cur_pos = ALPHABET.find(i)
            final_pos = (cur_pos + n) % 26
            empty += ALPHABET[final_pos]

        else:
            empty += i
    return empty

def decode(message, n):
    the_message = encode(message, n)
    decoder = ""
    for i in the_message:
        if i in ALPHABET:
            cur_pos = ALPHABET.find(i)
            final_pos = (cur_pos - n) % 26
            decoder += ALPHABET[final_pos]
        else:
            decoder += i

    return decoder

# def crack(message):
#     for i in range(1, 26):
#         decracked_cracked = decode(message, i)
#         print(f"Shift {i}: {decracked_cracked}")
            
def letter_to_shift(key):
    shift = ALPHABET.find(key)
    return shift


def main():
    print("Welcome to the Code Cracker")
    the_message = input("Enter the message: ")
    the_shift = input("Enter the key: ")

    print(f"Encoded: {encode(the_message, letter_to_shift(the_shift))}")
    print(f"Decoded: {decode(the_message, letter_to_shift(the_shift))}")
    # print(f"{crack(the_message)}")

if __name__ == '__main__':
    main()