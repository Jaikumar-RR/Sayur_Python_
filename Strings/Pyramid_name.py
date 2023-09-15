#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

#get the input from user
name = input("enter your name : ")

for i in range(1, len(name) + 1):#by using the for we loop with size of the name given
    spaces = " " * (len(name) - i)  # Add spaces before the name
    name_part = " ".join(name[:i])  # Add spaces between characters
    print(spaces + name_part) 
    

# substring = ""
# for letter in name:
#     substring += letter
#     print(substring)
    