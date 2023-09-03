
phone_sold = input(f"how many phone sold in this year, Enter sales list for each month (comma basis ,) ").split(',')

monthlySalesList = [int(Each_month_list) for Each_month_list in phone_sold ]
print(monthlySalesList)

    
base_pay = 10000
bonus_for_5_phones = 5000
bonus_per_phone = 1100
additional_bonus = 5000
cumulative_bonus = 0

previousMonthSalary = base_pay

for month, phoneCount in enumerate(monthlySalesList,1):
    
    # Calculate the Salary using if statements
    if phoneCount >= 5:
        total_bonus = bonus_for_5_phones + (phoneCount - 5) * bonus_per_phone
    else:
        total_bonus = 0
    
    currentMonthSalary = base_pay + total_bonus
    
    cumulative_bonus += total_bonus
    
    if currentMonthSalary == 10000 :
         print(f"This year month's {month} ,salary is : {currentMonthSalary}")
         print(f"{'-' * 20 }")
    else :
        print(f"This year month's {month} ,salary with additional bonus : {currentMonthSalary}")
        print(f"{'-' * 20 }")
        
    
    # Check for condition: If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones
    # this month also, then he gets additional Rs5000.
    if previousMonthSalary > 20000 and phoneCount >= 20:
        currentMonthSalary += additional_bonus
        print(f"This year month's {month} , salary with extra additional bonus: {currentMonthSalary}")
        print(f"{'-' * 20 }")
    previousMonthSalary = currentMonthSalary  
    
      
    
    if cumulative_bonus >= 100000 :
         base_pay += base_pay * 0.05
        # cumulative_bonus = 0
        
print(f"{'*' * 25 }")
   