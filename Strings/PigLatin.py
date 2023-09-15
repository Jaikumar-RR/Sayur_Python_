#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

#get an input from user
inputSentence = input("Enter your sentence : ")
pigLatinKey = 'ay'#set piglatinkey
outputSentence = []#set an empty list

for word in inputSentence.split():#using split() to spilit the sentences into word
    if len(word) > 1:  # Check if the word has more than one character
        firstChar = word[0] #set first char
        word = word[1:] + firstChar + pigLatinKey 
    else: #otherwise it will executed 
        word = word + pigLatinKey  # If the word has only one character, just add 'ay'

    outputSentence.append(word) #append the word into the list

result = ' '.join(outputSentence)#using join() we merge the list words
print(result)
