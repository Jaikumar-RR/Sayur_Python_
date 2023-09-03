
def Budget_Price(Onion,Tomato,budget):
    
    petrol_exp = budget*0.03
    
    if(petrol_exp>=1):
        print("Your Petrol Expences is :",petrol_exp)
        budget = budget - petrol_exp
        print("Your Budget after reducing Petrol expences :",budget)
    
    print("1.If you want onion, based on your budget Press 1\n2.If you want Tomato, based on your budget Press 2\n3.If you wants equal Kg of both Onion and Tomato, based on your budget Press 3")
    option = int(input("Enter your Option :"))

    if(option==1):
        Kg_buy_onion = budget/Onion
        print("You can get :",int(Kg_buy_onion),"kg")
        balance = budget%Onion
        print("Your balance amount :Rs.",balance)
    elif(option==2):
        Kg_buy_tomato = budget/Tomato
        print("You can get :",int(Kg_buy_tomato),"kg")
        balance = budget%Tomato
        print("Your balance amount :Rs.",balance)
    elif(option==3):
        kg_buy_both = budget/(Onion+Tomato)
        print("You can get Onion :",int(kg_buy_both),"kg")
        print("You can get Tomato :",int(kg_buy_both),"kg")
        balance = budget%(Onion+Tomato)
        print("Your balance amount :Rs.",balance)
    else :
        print("Invalid Option!!!")
    

print("Budget Calculation - Onion & Tomato ")
print("------------------------------------")

print("1.Local Area\n2.Other Cites")
option = int(input("Enter 1 or 2 :"))

if(option==1):
    print("Onion Price for 1kg is : 20")
    print("Tomato Price for 1kg is : 10.5")
    budget = float(input("Enter your Budget :"))
    Budget_Price(20,10.5,budget)

elif (option ==2):
    print("Cities :\n1.Chennai\n2.Madurai\n3.Trichy")
    City = int(input("Enter number to select cities:"))
    if(City == 1):
        print("Onion Price for 1kg is : 30")
        print("Tomato Price for 1kg is : 10.5")
        budget = float(input("Enter your Budget :"))
        Budget_Price(30,10.5,budget)
    elif(City == 2):
        print("Onion Price for 1kg is : 34")
        print("Tomato Price for 1kg is : 10.5")
        budget = float(input("Enter your Budget :"))
        Budget_Price(34,10.5,budget)
    elif(City == 3):
        print("Onion Price for 1kg is : 27")
        print("Tomato Price for 1kg is : 10.5")
        budget = float(input("Enter your Budget :"))
        Budget_Price(27,10.5,budget)
    else :
        print("Please enter valid option")
else :
        print("Please enter valid option")






    

        