#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.

#set an variable for total money and ask count
Total_money = 0
#ask_count = 0

for ask_count in range(5): #By suing for loop and set it range 5 
    money_given_by_parents = int(input("Enter the money given by your parents: Rs "))#entering parent given money
    
    #ask_count += 1 #set count increament
    
    if money_given_by_parents <= 10:#if the given money is less than or equal to 10 means it will executed
        print("Thank you, but this amount won't help much.") 
        continue #continue is used to continue the loop by skipping current iteration
    
    Total_money += money_given_by_parents
    
    print(f"Thank you. You now have Rs {Total_money}.")
    
    if Total_money >= 1000: #if the money is >= 1000 means it will executed
        print("You have enough money for the movie!")
        break

if Total_money < 1000: #after the loop the money is less than 1000 means it will executed
    print("You couldn't gather enough money for the movie.")

    
print(f"You asked your parents {ask_count+1} times.")#just printing ask count
