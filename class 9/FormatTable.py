# 3. Print the following. Learn how to use print with formatting
# Learn how to print ********* using formatted print
# My Tables
# Table  1
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# **********
# Table  2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# **********
# Table  3
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# **********
# End of tables

print("My Table")#just print title
table_range = 6 # set the title range
#By using nested for loop,
for multiplicand in range(1,4): # By using for loop set range to 1 - 4 
    print("Table ",multiplicand) #printing statement with multiplicand value Eg : Table 1
    for multiplier in range(1,table_range):#On second loop set range to 1 - table_range value
        print(multiplicand,' * ',multiplier,' = ',multiplicand*multiplier)#printing the statement as 1*1=1
    print("**************")
print("End of tables")    