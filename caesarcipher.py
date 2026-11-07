THE_ALPHABET =  'abcdefghijklmnopqrstuvwxyz'

def encode(message, key):
    result = ""
    for i in message:
        if i in THE_ALPHABET:
            current_letter_position = THE_ALPHABET.find(i)
            final_letter_position = (current_letter_position + key) % len(THE_ALPHABET)
            
            result += THE_ALPHABET[final_letter_position]
        else:
            result += i
    
    return result

def decode(message, key):
    encoded_message = encode(message, key)
    empty_box = ""
    for i in encoded_message:
        if i in THE_ALPHABET:
            current_position = THE_ALPHABET.find(i)
            final_position = (current_position - key) % 26
            empty_box += THE_ALPHABET[final_position]
        else:
            empty_box += i
    
    return empty_box


def main():
    print("Welcome to the Caesar Castle")
    the_message = input("Enter your message: ")
    the_key = int(input("Enter your key: "))
    answer = encode(the_message, the_key)
    op_answer = decode(the_message, the_key)
    print(f"The encrypted message becomes: {answer}")
    print(f"The decrypted message becomes: {op_answer}")

if __name__ == '__main__':
    main()