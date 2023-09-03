# Get input from the user
units_consumed = float(input("Enter the number of units consumed: "))


    # Fixed charges and tax percentage
tax_percentage = 0.1  # 10% tax
    
    # Calculate energy charges based on consumption
energy_charges = 0
    
if units_consumed>0 and units_consumed <= 100:
    
        fixed_charges = 0
        energy_charges = 0
        
elif units_consumed>100 and units_consumed <= 200:
    
        fixed_charges = 20
        energy_charges = 50 + (units_consumed - 100) * 2.25
        
elif units_consumed>200 and units_consumed <= 300:
    
        fixed_charges = 25
        energy_charges = 50  + (units_consumed - 200) * 4.50
        
elif units_consumed>300 and units_consumed <= 500:
    
        fixed_charges = 35
        energy_charges = 50  + (units_consumed - 300) * 6.50
        
else:
    
    fixed_charges = 50
    energy_charges = 50 + (units_consumed - 500) * 7.00
    
    # Calculate total bill amount
total_amount = fixed_charges + energy_charges
total_amount += (total_amount * tax_percentage) 
    
 

print("Your electricity bill amount is: Rs.",total_amount) 
