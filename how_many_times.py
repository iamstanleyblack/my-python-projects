
def main():

   ###############################################################
   #      Making a program that inputs sentences from user then  #
   #        computes how many times each word in the             #
   #           sentence appears				         #
   ###############################################################
    # start by prompting user to enter a sentence
    sentence = input("Enter a sentence: ")
    
    #then split the sentence into words and store in a variable
    separated_sentence = sentence.split()
    
   #define an empty dictionary where i will be storing the keys and values
    empty_dictionary = {}
   # then loop over the words(separated sentence
    for word in separated_sentence:
        #find out if teh word is already inside the dictionary
        if word in empty_dictionary:
	    #increment the value plus one if the word is in the dictionary already
            empty_dictionary[word] = empty_dictionary[word] + 1

        else:
		#the value for a word that appears only once will be just 1
            empty_dictionary[word] = 1
        
    #write a second for loop that prints each of the keys and their values
    for key, value in empty_dictionary.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()
