#Problem Statement 
#7.Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget.  
#Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city. 
# Same as above, but add 3% of the budget for petrol expenses.

#This program is based on my assumption


#To def a function with 3 parameters
def Budget_Price(Onion,Tomato,budget):
    
    petrol_exp = budget*0.03 #set the petrol expences
    
    if(petrol_exp>=1): # 50 > = 1 then the if statement is executed
        print("Your Petrol Expences is :",petrol_exp)
        budget = budget - petrol_exp
        print("Your Budget after reducing Petrol expences :",budget)
    
    #printing the option & get input from user
    print("1.If you want onion, based on your budget Press 1\n2.If you want Tomato, based on your budget Press 2\n3.If you wants equal Kg of both Onion and Tomato, based on your budget Press 3")
    option = int(input("Enter your Option :"))

    if(option==1):  # if the user press 1 then,if is executed
        #calculating and printing the user buy onion in kg
        Kg_buy_onion = budget/Onion
        print("You can get :",int(Kg_buy_onion),"kg")
        #calculating the balance amount and print it
        balance = budget%Onion
        print("Your balance amount :Rs.",balance)
    elif(option==2):   # if the user press 1 then,if is executed
        #calculating and printing the user buy tomato in kg
        Kg_buy_tomato = budget/Tomato
        print("You can get :",int(Kg_buy_tomato),"kg")
        #calculating the balance amount and print it
        balance = budget%Tomato
        print("Your balance amount :Rs.",balance)
    elif(option==3):  # if the user press 1 then,if is executed
        #calculating and printing the user buy both equal amount in kg
        kg_buy_both = budget/(Onion+Tomato)
        print("You can get Onion :",int(kg_buy_both),"kg")
        print("You can get Tomato :",int(kg_buy_both),"kg")
        #calculating the balance amount and print it
        balance = budget%(Onion+Tomato)
        print("Your balance amount :Rs.",balance)
    else :
        print("Invalid Option!!!")
    
#Just printing the Title
print("Budget Calculation - Onion & Tomato ")
print("------------------------------------")

#print and ask the user for cites selection
print("1.Local Area\n2.Other Cites")
option = int(input("Enter 1 or 2 :"))

if(option==1):  # if user press 1 then , it show the rates and ask to input budget
    print("Onion Price for 1kg is : 20")
    print("Tomato Price for 1kg is : 10.5")
    budget = float(input("Enter your Budget :"))
    Budget_Price(20,10.5,budget)

elif (option ==2): # if user press 2 then , it show the Cites name and ask to select cities
    print("Cities :\n1.Chennai\n2.Madurai\n3.Trichy")
    City = int(input("Enter number to select cities:"))
    if(City == 1):  # if user press 1 then , it show the rates and ask to input budget
        print("Onion Price for 1kg is : 30")
        print("Tomato Price for 1kg is : 10.5")
        budget = float(input("Enter your Budget :"))
        Budget_Price(30,10.5,budget)
    elif(City == 2):  # if user press 2 then , it show the rates and ask to input budget
        print("Onion Price for 1kg is : 34")
        print("Tomato Price for 1kg is : 10.5")
        budget = float(input("Enter your Budget :"))
        Budget_Price(34,10.5,budget)
    elif(City == 3):  # if user press 1 then , it show the rates and ask to input budget
        print("Onion Price for 1kg is : 27")
        print("Tomato Price for 1kg is : 10.5")
        budget = float(input("Enter your Budget :"))
        Budget_Price(27,10.5,budget)
    else :  #otherwise it executed the else
        print("Please enter valid option")
else :
        print("Please enter valid option")






    

        