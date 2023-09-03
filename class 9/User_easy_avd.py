# Ask the user if they want only the basic or only the advanced or both.
# Print what the user is asking. 
# Also ask the user what number table they want to print


#To def a function with passing 4 parameters
def Easy_Advance_number(table,another_table,start_range,end_range):
    #set start level for easy and advance
    EasyLevel_start = 1
    AdvanceLevel_start = 11
    
    if table <= another_table:#if the table value is <= another table value Eg : 4 < 8
       for multiplicand in range(table,another_table+1):# on first loop Eg : set range 1 - 4 and store value on multiplicand
        
            print("Table ",multiplicand) #Eg : Table 10
            for multiplier in range(start_range,end_range):#On second loop Eg : set range to 1 - 11 value
               if(multiplier == EasyLevel_start): #if the multipler = easylevel means it will executed 
                   print("Easy Number")
               if(multiplier == AdvanceLevel_start):#if the multipler = Advancelevel means it will executed
                   print("Advance Number")
               print(multiplicand,' * ',multiplier,' = ',multiplicand*multiplier)#printing the statement as 10*1=10
           
            print("**************")#it will inside the first for loop
       print("End of Table")# it is outside the loop
    
    else :#otherwise , else will executed 8 > 4
        
        step = -1 #set an step value as -1 to reverse no.
        for multiplicand in range(table,another_table-1,step): #On first loop set an range startvalue = 10 and endvalue = 0 and stepvalue = -2 because it starts with 10 and jump up to -2 
        
            print("Table ",multiplicand) #Eg : Table 10
            for multiplier in range(start_range,end_range):#On second loop Eg : set range to 1 - 11 value
                if(multiplier == EasyLevel_start):#if the multipler = easylevel means it will executed
                    print("Easy Number")
                if(multiplier == AdvanceLevel_start):#if the multipler = Advancelevel means it will executed
                    print("Advance Number")
                print(multiplicand,' * ',multiplier,' = ',multiplicand*multiplier)#printing the statement as 10*1=10
           
            print("**************")#it will inside the first for loop
        print("End of Table")# it is outside the loop

print("My Tables") #just print title
print("Enter 2 two numbers for tables") #get two number from user 
table = int(input("Starting table : "))
another_table = int(input("Ending table : "))
if table > 0 and another_table > 0 : # if table and another tavle value is higher than 0 means it will executed
    #set an option variable for easy , advance and both 
    option = int(input("1.Easy Number\n2.Advance Number\n3.Both Easy and Advance\nPress no (1 \ 2 \ 3) : "))
    if option == 1: # if the user press 1 means it will executed
        #set an start and end range
        start_range = 1
        end_range = 11
        Easy_Advance_number(table,another_table,start_range,end_range)#calling the function with passing 4 arguments
    elif option == 2 : # if the user press 2 means it will executed
        #set an start and end range
        start_range = 11
        end_range = 21
        Easy_Advance_number(table,another_table,start_range,end_range)#calling the function with passing 4 arguments
    elif option == 3 : # if the user press 3 means it will executed
        #set an start and end range
        start_range = 1
        end_range = 21
        Easy_Advance_number(table,another_table,start_range,end_range)#calling the function with passing 4 arguments
    else : #otherwise it will executed
        print("Please enter valid Number!!!")
else : #otherwise it will executed
    print("Please Don't enter zero or negative number")
    
    
