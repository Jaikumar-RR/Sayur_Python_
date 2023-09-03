######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

#      1  2  3  4  5
#   ********************
# 1 |  1  2  3  4  5
# 2 |  2  4  6  8 10
# 3 |  3  6  9 12 15
# 4 |  4  8 12 16 20
# 5 |  5 10 15 20 25

#get the start value and end value
start = int(input("Enter the start number : "))
end = int (input("enter the end Number : "))
if (end < start):
    print("!!Enter end value higher than start!!")
    exit()
size = end - start + 1 #set size is end - start + 1
print("  ",end = "") #print the whitespace abd continue the line
for col in range (start,end+1): # on this loop first it print #      1  2  3  4  5
                                                              #   ********************
    print(f"{col : 4}",end="")
print("\n","*"*(4*size + 1)) #just printing the star

for row in range(start,end + 1): # on this loop it set range the value of start and end + 1 value
    print(f"{row : 2} |",end = "") # row : 2 is used to print the value after 2 space
    for col in range (start,end + 1): #on this loop it set range the value of start and end + 1 value
        result = row * col #multiply row and col
        print(f"{result : 4}",end = "") #print the result after 4 space
    print()
