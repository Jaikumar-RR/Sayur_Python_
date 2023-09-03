# 1. Print the following using for loop
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5

#set variable for multificand and table_range
multiplicand = 1 
table_range = 6

print("Tables") #just printing title
for multiplier in range(1,table_range): #By using for loop , to run statement from range 1 - table_range
    print(multiplicand,' * ',multiplier,' = ',multiplicand*multiplier) #Eg : 1 * 1 = 1