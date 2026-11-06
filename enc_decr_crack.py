ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encode(message, n):
    empty = ""
    for i in message:
        if i in ALPHABET:
            curr_pos = ALPHABET.find(i)
            final_pos = (curr_pos + n) % 26
            empty += ALPHABET[final_pos]
        else:
            empty += i
        
    return empty

def decode(message, n):
    # encoded_message = encode(message, n)
    decoder = ""
    for i in message:
        if i in ALPHABET:
            curr_pos = ALPHABET.find(i)
            final_pos = (curr_pos - n) % 26
            decoder += ALPHABET[final_pos]
        else:
            decoder += i
    return decoder

def crack(message):
    for i in range(1, 26):
        decracked_one = decode(message, i)

        print(f"Shift {i}: {decracked_one}")

def main():
    print("Welcome to the Code Machine!")
    the_message = input("Enter a message: ")
    # the_shift = int(input("Enter a shift: "))
    # print(f"Encoded: {encode(the_message, the_shift)}")
    # print(f"Decoded: {decode(the_message, the_shift)}")
    crack(the_message)
if __name__ == "__main__":
    main()
