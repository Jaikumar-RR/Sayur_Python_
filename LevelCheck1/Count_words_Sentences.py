#Problem Statement 
#Input is a Sentence . Find the Number of times each word appears .

#To def a function with 1 parameters
def Count_Words(Sentence):

    words = Sentence.split() #By using split() method it will split up the given sentences  and split() is an build in method
    
    for index in range(len(words)): #By using for loop, the range is length of the words
        words[index] = words[index].lower() #lower()is also a bulid-in function to change the word into lowercase
        count = 1 #set count value is 1
        
        for index1 in range(index + 1,len(words)): #By using inner for loop j and set the range into i+1 , length of words
            if words[index] == words[index1] : #On if check the two words is equal
                count = count+1
                words[index1]=""
            
            
        if words[index]!="": #if the words is not equal to empty string means then it will executed
            print(words[index] ,":"+ str(count))

#asking the user to input sentences 
sentences = input("Enter a sentences :")
Count_Words(sentences) #calling the 'Count_Words'function with passing arguments