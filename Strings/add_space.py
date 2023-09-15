########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g

#___________________________________________________________________________________________________________
# inputString = input("enter a word to add space after 2 char : ")
# i = 0 #counter to track the chars
# newString = ""
# j = 0
# while i < len(inputString):

#     if j < 2 :
#         newString += inputString[i]
#         j+=1
#     else :
#         newString += " " #add space
#         j = 0
#         i = i - 1
#     i+=1
# #check to add the chars at the end
# #FillinMissingCode

# print (newString)

#--------------------------------------------------------------------------------------------
inputString = input("Enter a string: ")  # Get input from the user
i = 0  # Counter to track the characters
newString = ""

while i < len(inputString):
    newString += inputString[i:i+2]  # Append characters from i to i+1 of inputString
    if i + 2 < len(inputString):  # Check if there are more characters to add
        newString += " "  # Add a space
    i += 2

print(newString)
