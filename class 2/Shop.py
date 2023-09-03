print("Welcome To Tea Stall")
print("____________________")
Vadai = 30
Sandwich = 100
Soda = 20
Vadaicost = 0
Sodacost = 0
Sandwichcost = 0

while 1 :
       print("Menu")
       print("----")
       print("1.Vadai - Rs.30")
       print("2.Soda - Rs.20")
       print("3.Sandwich - Rs.100")
       print("Press any other Number to get bill")
       order = int(input("Please enter food Number : "))
       
       if order == 1 :
           print("Vadai")
           quantity = int(input("Please enter quantity : "))
           Vadaicost = 30*quantity
       elif order == 2 :
             print("Soda")
             quantity = int(input("Please enter quantity : "))
             Sodacost = 20*quantity 
       elif order == 3 :
             print("Sandwich")
             quantity = int(input("Please enter quantity : "))
             Sandwichcost = 100*quantity
       else :
             print("!!Thank You!!")
             break

totalcost = Vadaicost+Sodacost+Sandwichcost
print("Your Total Bill Cost is :",totalcost)
Cust_amt = float(input("Please enter Your Amount : "))
if Cust_amt>totalcost :
      print("Please take your balance ", Cust_amt-totalcost)
      print("!!Thank You For Ordering!!,Have a Nice day")
elif Cust_amt<totalcost :
      print("Please pay your balance amount :",totalcost-Cust_amt)
      bal_amt = float(input("Enter amount :"))
      Cust_amt += bal_amt 
      if Cust_amt>totalcost :
            print("Please take your balance ", Cust_amt-totalcost)
            print("!!Thank You For Ordering!!,Have a Nice day")
      else :
           print("!!Thank You For Ordering!!,Have a Nice day")
else :
      print("!!Thank You For Ordering!!,Have a Nice day")
      
            

       






