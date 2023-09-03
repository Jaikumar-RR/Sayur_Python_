def EasyNumber(multiplicand):#to def a function with parameters
    print("Tables", multiplicand) 
    print("EasyNumbers")  
    for multiplier in range(1, 11):#set an range 1 - 11
        print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
    print(f"{'-' * 10}")

def AdvanceNumber(multiplicand):#to def a function with parameters
    print("Tables", multiplicand)
    print("Advancenumber")  
    for multiplier in range(11, 21):#set an range 11 - 21
        print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
    print(f"{'-' * 10}")

def both_functions(multiplicand):#to def a function with parameters
    #calling the function easy and advance 
    EasyNumber(multiplicand) 
    AdvanceNumber(multiplicand)

operations = [EasyNumber, AdvanceNumber, both_functions ]#on list we can assign the 3 functions name on operations

print("!!!! Tables Calculator !!!!")
print(f"{'-' * 15}")

input_tables = input("Enter table numbers separated by commas: ")
input_tables = input_tables . split(',') #split(',') is used to split the value on the ist after commas
wanted_tables = [int(table) for table in input_tables]#on empty list we assign value as int()

print("1. EasyNumbers\n2. AdvanceNumbers\n3. Both Easy and Advance")
option = int(input("Enter Your Option (1 / 2 / 3): ")) -1  # Subtracting 1 to match list index

selected_operation = operations[option] # option = 1 -1 =0 then opreations[0] = easynumber

print("Tables:")
for multiplicand in wanted_tables: #wanted list values are stored in multiplicands 
    selected_operation(multiplicand) #calling the function with passing arguments

print("End of Tables")
