def countWordInFile(file_path, target_word):
    count = 0
    # make the target word to be lowercase so as to avoid case-sensitive bugs
    target_word = target_word.lower()
    
    # open the file in read mode "r"
    with open('dummy.txt', 'r') as file:
        # i want to read line by line
        for line in file:
            # to convert the line to lowercase and clean up punctuation
            line = line.lower()
            for punctuation in [".", ",", "!", "?", ";", ":"]:
                line = line.replace(punctuation, "")
            
            # split the line into individual words
            words = line.split()
            for word in words:
                if word == target_word:
                    count += 1
                    
    return count

# Call the function at the bottom to test it:
result = countWordInFile('dummy.txt', 'the')
print(f"The word appears {result} times.")