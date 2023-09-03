#Problem Statement 
#Having 3 types coins , value of 1 , 3 , 5 and find the minimum coin required for given amount
#To def an function with 1 parameters
def Counting_minimum_Coins(amount):
    #set coins values 
    coin_5 = 5 
    coin_3 = 3
    coin_1 = 1
    #define variables to count the coins (set value 0) 
    Count_of_coin5 = 0
    Count_of_coin3 = 0
    Count_of_coin1 = 0
    
    #Using while loop and make the condition 1 for continues loop until it break
    while 1 :
        # ex. amount = 9
        if(amount>=coin_5): # 9>=5 true then , execute if statement
            amount = amount - coin_5 # amount = 9 - 5 = 4
            Count_of_coin5 += 1 #Count_of_coin5 is incremented by 1
        elif(amount>=coin_3 and amount<5): #4>=3 and 4<5 true , then elif is executed
            amount = amount - coin_3 # amount = 4 - 3 = 1
            Count_of_coin3 += 1  #Count_of_coin3 is incremented by 1
        elif(amount>=coin_1 and amount<3):  #1>=1 and 1<3 true , then elif is executed
            amount = amount - coin_1  # amount = 1 - 1 = 0
            Count_of_coin1 += 1  #Count_of_coin1 is incremented by 1
        if(amount == 0): #amount == 0 so , if is executed
            break  # To break a loop

    #Print the counts of coins and total coins used .   
    print("Rs.5 Coins ("+str(Count_of_coin5)+")")
    print("Rs.3 Coins ("+str(Count_of_coin3)+")")
    print("Rs.1 Coins ("+str(Count_of_coin1)+")")
    print("Minimum Total Coins is : ",Count_of_coin5+Count_of_coin3+Count_of_coin1)

#just printing the title    
print("Counting the minimum coins for the amount ")
amount = int(input("Enter the amount to convert into coins : ")) #get an amount from user
Counting_minimum_Coins(amount) # calling the function 'Counting_minimum_Coins'with passing an arguments

