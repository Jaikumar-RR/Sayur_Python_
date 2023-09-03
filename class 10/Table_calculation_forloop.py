#Problem Statement
#Get a n number input from user for calculate table for given numbers using for loop

#To def a function with an parameter
def EasyNumber(multiplicand):
    print("Tables ",multiplicand) 
    print("EasyNumbers")#it inside on first loop
    for multiplier in range(1,11):#On second loop set range to 1 - 11 value
        print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
    print(f"{'-'*10}")

#To def a function with an parameter
def AdvanceNumber(multiplicand):
    
    print("Tables ",multiplicand)
    print("Advancenumber")#it inside on first loop
    for multiplier in range(11,21):#On second loop set range to 11 - 21 value
        print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
    print(f"{'-' *10}")
    

#just print title
print("!!!!Tables Calculator!!!!")
print(f"{'-'*15}")
Wanted_tables = [] #set an empty list variable

NumberOfTables = int(input("Enter number of tables needed : "))

for count in range (NumberOfTables): #By using for loop to set range of number of table insert value
    table = int(input(f"Enter {count+1}. table : "))
    if table > 0 :#if the number is > 0 means it will executed
        Wanted_tables.append(table) #append() is used to store table value on wanted table list
    else :#otherwise it will executed
        print("Don't enter zero or negative number")

#ask easy, advance or both option
print("1.EasyNumbers\n2.AdvanceNumbers\n3.Both Easy and Advance")
option = int(input("Enter Your Option (1 \ 2 \ 3): "))

if (option == 1): #if user enter 1 it will executed
    for multiplicand in Wanted_tables:
        EasyNumber(multiplicand)#calling a function 'EasyNumber' with passing an arguments
    print("End of Tables")
elif(option == 2):#if user enter 1 it will executed
    for multiplicand in Wanted_tables:
        AdvanceNumber(multiplicand)#calling a function 'AdvanceNumber' with passing an arguments
    print("End of Tables")
elif(option == 3):#if user enter 1 it will executed
    for multiplicand in Wanted_tables:
        EasyNumber(multiplicand)#calling a function 'EasyNumber' with passing an arguments
        AdvanceNumber(multiplicand)#calling a function 'AdvanceNumber' with passing an arguments
    print("End of Tables")
else :
    print("!!Enter Valid Number!!")
