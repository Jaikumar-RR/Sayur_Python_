# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high

#import the random 
import random
print(" Welcome, To Number Guessing Game ")
print(f"{'-'*15}")
computer_number = random.randint(1,500)#on random we use randint() for get random value from Computer
max_attempts = 5 #set max attempt
user_attempt = 0
while user_attempt < max_attempts:# Bysusing while , to chech the user_attempt is < max attempt 
    user_guess = int(input(f"Enter your Guessing Number upto [ 1 - 500 ](Your Remaining attempts {max_attempts-user_attempt}) : "))
    user_attempt += 1
        
    if user_guess<computer_number:#if 25<250 means it will executed
        print("Low")
    elif user_guess>computer_number:#if 400<250 means it will executed
        print("High")
    else :#otherwise it will executed
        print(f"Congratulations! You guessed the number {computer_number} in '{user_attempt}' attempts ")
        exit()
print("Sorry, Try again!! You have no attempts remaining!!")
print("The Computer Number was : ",computer_number)
