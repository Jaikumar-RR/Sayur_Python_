#Problem Statement
#Get a n number input from user for calculate table for given numbers 

#to def an function with a parameter
def User_table_Calculation(Wanted_tables):
    #ask easy, advance or both option
    print("1.EasyNumbers\n2.AdvanceNumbers\n3.Both Easy and Advance")
    option = int(input("Enter Your Option (1 \ 2 \ 3): "))

    if(option == 1):#if user enter 1 then it will executed
        for multiplicand in Wanted_tables: # on first loop set range as Wanted_table list and store value on multiplicand
            print("Tables ",multiplicand) 
            print("EasyNumbers")#it inside on first loop
            for multiplier in range(1,11):#On second loop set range to 1 - 11 value
                print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
            print(f"{'-'*20}")
        print("End of tables")#it is on out side the loop
    elif(option == 2):#if user enter 2 then it will executed
        # on first loop set range as Wanted_table list and store value on multiplicand
        for multiplicand in Wanted_tables:
            print("Tables ",multiplicand)
            print("Advanceumber")#it inside on first loop
            for multiplier in range(11,21):#On second loop set range to 11 - 21 value
                print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
            print(f"{'-'*20}")
        print("End of tables")
    elif(option == 3):#if user enter 3 then it will executed
        # on first loop set range as Wanted_table list and store value on multiplicand
        for multiplicand in Wanted_tables:
            print("Tables ",multiplicand)
            print("Easy Numbers")#it inside on first loop
            for multiplier in range(1,11):#On second loop set range to 1 - 11 value
                print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
            print("Advance Numbers")  
            for multiplier in range(11,21):#On third loop set range to 11 - 21 value
                print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
            print(f"{'-'*20}")
        print("End of tables")
    else : #otherwise it will exected the else statement
        print("!!Please enter valid number!!")
        
print("!!!!Tables Calculator!!!!")
print(f"{'-'*20}")
Wanted_tables = [] #set an empty list variable
count = 1
while 1 :#By using infinite while loop for get n number from user until they break
    
    table = input(f"Enter {count}. table (press any other key to exit): ")
    count +=1
    if table == '0' : #if they enter 0 then it will executed
        print("Don't enter zero")
        
    else:#otherwize it will executed
    
        if table.isdigit():#isdigit() function is used to check the enter value is number or not
         
            Wanted_tables.append(int(table)) #convert into int table and append() is used to store it on list

        else : #if the value is negative or any other value means it will executed
            break #break the loop
User_table_Calculation(Wanted_tables) #calling the 'User_table_Calculation' with passing an argument