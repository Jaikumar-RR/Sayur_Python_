#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold


# Initialize the quantities and prices of bags
red_bags = 100
white_bags = 200
red_bag_price = 1000
white_bag_price = 1500

# Initialize variables to keep track of sales and bags sold
total_sales = 0
total_bags_sold = 0

#by using while to check the sales is <10000 and sold bag is <10
while total_sales < 10000 and total_bags_sold < 10:
    print("Available Bags:")
    print(f"Red Bags: {red_bags} (Rs {red_bag_price} each)")
    print(f"White Bags: {white_bags} (Rs {white_bag_price} each)")
    
    bag_type = input("Enter the bag type (Red/White) you want to buy (or 'q' to quit): ").lower()
    
    if bag_type == 'q':#if the user give q it will executed
        break
    
    if bag_type == 'red' and red_bags > 0: #if the user give red and red bag > 0 means, it will executed
        quantity = int(input(f"How many Red Bags do you want to buy? Available: {red_bags} bags: "))
        if quantity <= red_bags:
            red_bags -= quantity
            total_bags_sold += quantity
            total_sales += quantity * red_bag_price
        else:
            print("Not enough Red Bags in stock.")
            
    elif bag_type == 'white' and white_bags > 0:
        quantity = int(input(f"How many White Bags do you want to buy? Available: {white_bags} bags: "))
        if quantity <= white_bags:
            white_bags -= quantity
            total_bags_sold += quantity
            total_sales += quantity * white_bag_price
        else:
            print("Not enough White Bags in stock.")
    else:
        print("Invalid choice or bag not in stock.")

print(f"Total Sales: Rs {total_sales}")
print(f"Total Bags Sold: {total_bags_sold}")
