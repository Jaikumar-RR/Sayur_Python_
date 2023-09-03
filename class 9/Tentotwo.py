# 4.Print the following
# My Tables
# Table  10
# 10 * 1 = 10
# 10 * 2 = 20
# 10 * 3 = 30
# 10 * 4 = 40
# 10 * 5 = 50
# **********
# Table  8
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# **********
# Table  6
# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# **********
# Table  4
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20
# **********
# Table  2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# **********
# End of tables

print("My Tables")#just print title
#By using nested for loop ,
for multiplicand in range(10,0,-2):#On first loop set an range startvalue = 10 and endvalue = 0 and stepvalue = -2 because it starts with 10 and jump up to -2 
    print("Table ",multiplicand) #Eg : Table 10
    for multiplier in range(1,6):#On second loop set range to 1 - table_range value
        print(multiplicand,' * ',multiplier,' = ',multiplicand*multiplier)#printing the statement as 10*1=10
    print("************")
print("end of table")    