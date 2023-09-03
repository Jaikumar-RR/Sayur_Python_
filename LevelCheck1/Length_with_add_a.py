#Problem Statement 
#Get two names. If the length of the two names is not equal, add 'a' at the end of the short name until the length is equal. 
  #  Eg - input - cat, arrow. (legnth is not equal) 
   # Output - cataa, arrow (length is equal by adding a)
#To def an function with 2 parameters
def Length_equal(firstword,secondword):
    # ex . the firstword = virat secondword = abd
    if len(firstword)==len(secondword): # 5 == 3 its false so , it cannot be executed
        print(firstword)
        print(secondword)
    else : # Now, else is executed because if is false
        #Using while 1 for continues looping
        while 1 :
            if len(firstword) > len(secondword): # 5 > 3 so , again looping 5>4 so ,
               secondword = secondword + 'a' #secondword = abda  # secondword = abdaa
            elif len(secondword) > len(firstword) : # if the given secondword is larger then firstword means elif is executed
                firstword = firstword + 'a' # and add a to the firstword
            else : # if the if and elif false like virat == abdaa then ,print it and break the loop
                print(firstword) 
                print(secondword)
                break

#just print title and get two words from user
print("!!Adding a if the word is small!!")
print("Enter any 2 words")
firstword = input("Enter a Firstword :")
secondword = input("Enter a Secondword :")
Length_equal(firstword,secondword) #calling the function 'Length_equal' with passing 2 arguments 