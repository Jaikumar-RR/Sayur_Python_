#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay 


#get an input from user
inputSentence = input("Enter the string : ")
inputSentence=inputSentence # using lower() we change the sentence into lowercase 
pigLatinKey = 'ay' #set piglatinkey
vowels = ['a','e','i','o','u','A','E','I','O','U']#set vowels on list
words=inputSentence.split(" ") #spliting the sentences into words 
sentence=""#set empty string 
for word in words: #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
        if char in vowels: 
            first_vowel_index = index
            break
    # here using string slicing to add words in sentence

    sentence = sentence + word[first_vowel_index+1:] +word[:first_vowel_index + 1] + pigLatinKey    # finally adding the ay at end
    sentence+=" "   # adding space at end of each word
print(f"Final sentence is : {sentence}")