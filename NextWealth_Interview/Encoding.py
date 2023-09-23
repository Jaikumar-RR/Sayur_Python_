# Problem 2
# Encoding 
# Encode the user input using the following alg, using the encode Key (a number)

# For each word in the odd position, move each letter in the word by the number of positions mentioned in the key.
# For words in the even position, reverse the word and then do the same as the odd position

# Eg - Key 2, input sentence "I am the King"
# Output K oc vjg ipkM

def encode_word(word, key):#to def a function with 2 parameters 
    encoded = "" #set an empty string variable
    for letter in word: #using for loop to seperate word into letter 
        if letter.isalpha(): #if the letter is alphabet means then this will executed
            shift = ord('a') if letter.islower() else ord('A') #on shift if the letter is lower case means it will executed ord('a') otherwise ord('A')
            encoded_letter = chr((ord(letter) -shift + key ) % 26 + shift)#chr() is used to change the ascii value into char.
            encoded += encoded_letter
        else:
            encoded += letter #if anything other than alpha means just add it
    return encoded  #return encoded string

def encode_sentence(sentence, key):#def a function with two parameters
    words = sentence.split() #split() sentence into words
    encoded_words = []#set an empty list

    for i, word in enumerate(words):
        if i % 2 == 0:#if word on odd pos means it will executed
            encoded_words.append(encode_word(word, key))#calling the function encode_word and the return value is appened to the encoded_word
        else:
            encoded_words.append(encode_word(word[::-1], key))#calling the function encode_word ,also reversing the word and the return value is appened to the encoded_word

    return ' '.join(encoded_words) #covert list into string


# Get the user input for the key and the sentence
key = int(input("Enter the key: "))
sentence = input("Enter the sentence: ")

# Encode the sentence using the key and print the result
result = encode_sentence(sentence, key)
print("The encoded sentence is:", result)

#________________________________________________________________________________


#   OUTPUT  :

# Enter the key: 2
# Enter the sentence: I am the King
# The encoded sentence is: K oc vjg ipkM

#__________________________________
