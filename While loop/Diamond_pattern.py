######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

#get the input from user number of lines wants to print
number_of_dollar = int(input("Enter the row's value for diamond: "))
lines = 0
continue_printing = True

#By using while loop 
while lines < number_of_dollar * 2 - 1 and continue_printing: # 0 < 5 = True and True = True , if continue change into false or line =5 means it does not executed the loop
    space = abs(number_of_dollar - 1 - lines)#abs () is used to get positive value on it
    symbol = 2 * abs(number_of_dollar - space) - 1

    print(" " * space + "$ " * symbol)

    lines += 1
    #get the input from user 
    user_input = input("Press space to continue or any other key to stop: ")

    if user_input != " ":#if used enter otherthan space means it will executed
        continue_printing = False
