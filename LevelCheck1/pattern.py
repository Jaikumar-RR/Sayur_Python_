#Problem Statement
#Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form of the pattern. 
#Eg -  Message - "I Love India".
#      Pattern - "*** **** ** **********     *****"
#      Output  - "ILo veIn di aILoveIndi     aILov"


#To def an function with 1 parameters
def Pattern_Printing(Message) :
    #set the pattern what needed with message
    Pattern ="*** **** ** **********     *****"
    output = "" #set an empty output variable
    Message = Message.replace(" ","") #replace() is build-in function to replace thinks 
    index_position = 0 #set index position is 0

    for i in range(len(Pattern)): #Using for loop i to range is length of pattern
        if Pattern[i]=='*': #by tracing pattern it find star means if is executed
             output = output+Message[index_position] #adding the output with (message[index_postion])value
             index_position = index_position + 1 #and increament the index_position value

        elif Pattern[i]==' ':#by tracing pattern it found space means then elif is executed
            output = output + " " #also adding space with output
            
        if index_position == len(Message) : #when the index position and length of message is equals the this if is executed 
              index_position=0 #set the index_postion is 0 and executed again from top until length of pattern is finish
    print(output) #print the output message

#just print the title and set message 
print("Pattern Program")
print("---------------")
Message = "I Love You"
print("The given Message is :I Love You")
Pattern_Printing(Message) #calling the function with passing an argument

