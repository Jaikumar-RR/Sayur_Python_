# Problem 1:
# Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

#this is based on my assumption....

def count_the_the_pairs(passage):# To def a function count_the_the_pairs with an parameter 
    
    words = passage.lower().split() #make the passage as lower case and split it into words
    # Initialize count to 0.
    count = 0
    # set a flag to False to check if the previous word was 'the'.
    previous_was_the = False

    for word in words:#by using store word and check the condition
        if word == "the": #if word = the means it will executed
            if previous_was_the: # if true means it will executed
                count += 1#count increment
            previous_was_the = True 
        elif word == "a":#if word = a means it will executed
            previous_was_the = False#set previous_was_the = False

    return count #return Count

#set a passage 
passage = "The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day."

count = count_the_the_pairs(passage)#calling the function and set the return value on count

# Print the count.
print("'the' followed by another 'the' without 'a' in between :",count)

#_______________________________________________________________________________

#   OUTPUT :

#'the' followed by another 'the' without 'a' in between : 4

