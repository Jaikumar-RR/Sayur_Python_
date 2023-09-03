# 2. Print the following using two for loops

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15

#set a variable to store table range
table_range = 6
#By using nested for loop to ren the below statement
for multiplicand in range(1,4): # on first loop set range 1 - 4 and store value on multiplicand
    for multiplier in range(1,table_range): # on second loop set range 1 - 11 and store value on multiplier
        print(multiplicand,' * ',multiplier,' = ',multiplicand*multiplier) #printing the statement as 1*1=1