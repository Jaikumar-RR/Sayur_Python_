#importing the Counter from collection package
from collections import Counter

#To def a function with parameters
def Count_Words(Sentence):
    words = Sentence.lower().split()#Using the lower() is used to change the sentence into lowercase 
                                    #Using the split() is used to split the sentences into words
    word_count = Counter(words)   #Counter is used to count the words and stored as dictionary 

    for word , count in word_count.items(): #items() is used to get the items in dictonary and By using for loop to store the value on it.
        #print the words and count
        print(word + ":" + str(count))

# Asking the user to input sentences
sentence = input("Enter a sentence: ")
Count_Words(sentence)#calling the function 'Count_Words' with passing an arguments
