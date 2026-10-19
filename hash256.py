# I am going to make a program that hashes a password using sha256
# This hashing is irreversible and cannot be decrypted to find teh original password
# To find teh original function, you will have to hash every other password in the wordlist and then check which hash functions are similar

#First, I will have to imprt the module for secure hashes and message digests
import hashlib

#The string method we can use to convert a regular string like "password123" into bytes is called .encode('utf-8)

# once we have our word in bytes we can feed it into the SHA-256 algorithm to create a hash object
# for example my_hash = hashlib.sha256(word_bytes)

#This will create the hash object in the background which we will convert to a readable string of letters and numbers like ef34b9u4..etc


#word_bytes = "pass@123".encode('utf-8')
# my_hash = hashlib.sha256(word_bytes)

# readable_hash = my_hash.hexdigest()
password_found = False
with open('passwords.txt', 'r') as file:
    for line in file:
        #word = "pass@123"
        word = line.strip()
        word_bytes = word.encode('utf-8')
        
        my_hash = hashlib.sha256(word_bytes)
        readable_hash = my_hash.hexdigest()
        #"835a60e0a4f5ef4545598687ba1b6e4e0406d3381a1a2e3796d8b67104b90159"
        print(f"Trying: {word!r} -> {readable_hash}")
        if readable_hash == "91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203":
            print(f"Password found: {word}")
            password_found = True
            break
        
if password_found == False:
    print("Password not found in wordlist.")