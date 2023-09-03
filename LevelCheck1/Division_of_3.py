#Problem Statement
#Getting an dividend and divisor input from thr user and keep dividing the number until the dividend is less than divisor , and print the number of times the number is divided

# To def a function with 2 parameters 
def Division_Of_3(number,divisor):
      count = 0  #set count is 0

      #print the divisor and dividend 
      print("The Number for Divisor :",divisor)
      print("The Number for Dividend :",number)

      #using while loop for looping the statement and set condition is 1 , because its loop will not end until is break
      while 1:
         if(number>divisor):  # On if condition , eg : 50 > 3 the if is executed
            number = number/divisor
            count += 1
         else : # Otherwise the else is executed and break the loop
            break 
      #print the count , number of times the number is divided
      print("The Number is :",count,"times divided by ",divisor)
    
#Just printing the title
print("Counting Divided times")
#get input from user for dividend and divisor
number = int(input("Enter a number to divided : "))
divisor = int(input("Enter a divisor number to divided number "+str(number)+":"))
#calling the function 'Division_Of_3' with passing 2 arguments
Division_Of_3(number,divisor)

    