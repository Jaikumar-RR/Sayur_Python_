#problem statement
#find the tax slap for income tax for india . write a program to calculate the income tax.
#Old Tax Regime :
#< 60 years of age :  | 60 - 80 years :    | > 80 Years : 
# 0 - 250000 -> NIL   | 0 - 3L -> NIL      | 0 - 5L -> NIL
#2.5L - 5L -> 5%      | 3L - 5L -> 5%      | 5L - 10L -> 20%
#5L - 10L -> 20%      | 5L - 10L -> 20%    | 10L <  -> 30%
#10L < -> 30%         | 10L <  -> 30%      |
#--------------------------------------------------------------------------------------
#New Tax Regime :
# 0 - 3L -> NIL
# 3L - 6L -> 5%
# 6L - 9L -> 10%
# 9L - 12L -> 15%
# 12L - 15L -> 20%
# 15L <   -> 30%
#-----------------------------------------------------------------------------------------


#To def a function "Old_tax_regime" with 2 parameters
def Old_tax_regime(age , taxable_income):
    
    
    health_education_cess = 0.04    # Health and Education cess : 4%
    
    if age <= 60 : # if the age is below or equal to 60 then it will be executed
        
        #To define a variables (slabs) with their values
        slab1 = 250000
        slab2 = 500000
        slab3 = 1000000
        
        if(taxable_income <= slab1): # if the taxable income is <= slab1 then it will executed
            tax = 0  #set tax = 0
            print("NIL")
        elif(slab1 < taxable_income <= slab2 ):# if the taxable income is above slab1 <= slab2 then it will be executed
            tax = 0.05 * (taxable_income - slab1) # to set tax = 5% 
        elif(slab2 < taxable_income <= slab3): # if the taxable income is above slab2 <= slab3 then it will be executed
            tax = 12500 +(0.2 * (taxable_income - slab2)) # to set tax = 20%
        else : #if the taxable income is above slab3 then else will executed
            tax = 112500 +(0.3 *(taxable_income - slab3)) # to set tax = 30%
        
        # adding the health and education cess amount with tax    
        tax = tax + (tax * health_education_cess)
        print("Your Tax amount is : ",tax)
        
    elif 60 < age <= 80 : # if the age is 60 - 80 then it will be executed
        
        #To define a variables (slabs) with their values
        slab1 = 300000
        slab2 = 500000
        slab3 = 1000000        
        
        if(taxable_income <= slab1):# if the taxable income is <= slab1 then it will executed
            tax = 0  #set tax = 0
            print("NIL")
        elif(slab1 < taxable_income <= slab2 ): # if the taxable income is above slab1 <= slab2 then it will be executed
            tax = 0.05 * (taxable_income - slab1) # to set tax = 5%
        elif(slab2 < taxable_income <= slab3):  # if the taxable income is above slab2 <= slab3 then it will be executed
            tax = 10000 +(0.2 * (taxable_income - slab2)) # to set tax = 20%
        else :  #if the taxable income is above slab3 then else will executed
            tax = 110000 +(0.3 *(taxable_income - slab3)) # to set tax = 30%
       
        # adding the health and education cess amount with tax      
        tax = tax + (tax * health_education_cess) 
        print("Your Tax amount is : ",tax)
        
    else :  #if the age is >80 then it will executed 
        
        #To define a variables (slabs) with their values
        slab1 = 500000
        slab2 = 1000000
        
        if(taxable_income <= slab1): # if the taxable income is <= slab1 then it will executed
            tax = 0 # set tax = 0
            print("NIL")
        elif(slab1 < taxable_income <= slab2 ): # if the taxable income is above slab1 <= slab2 then it will be executed
            tax = 0.2 * (taxable_income - slab1) # to set tax = 20%
        else : #if the taxable income is above slab2 then else will executed
            tax = 100000 +(0.3 *(taxable_income - slab2)) # to set tax = 30%
        
        # adding the health and education cess amount with tax   
        tax = tax + (tax * health_education_cess)
        print("Your Tax amount is : ",tax)

#To def a function "New_tax_regime" with parameter       
def New_tax_regime(taxable_amount):
    
    #To define a variables (slabs) with their values
    slab1 = 300000
    slab2 = 600000
    slab3 = 900000
    slab4 = 1200000
    slab5 = 1500000
    #To set health and education cess is : 4%
    health_education_cess = 0.04
    
    if (slab1 >= taxable_amount):# if the taxable income is <= slab1 then it will executed
        tax = 0 #to set tax = 0
        print("NIL")
    elif(slab1 < taxable_amount <= slab2): # if the taxable income is above slab1 <= slab2 then it will be executed
        tax = 0.05 * (taxable_amount - slab1) # set tax = 5%
    elif(slab2 < taxable_amount <= slab3): # if the taxable income is above slab2 <= slab3 then it will be executed
        tax = 15000 + (0.10 * (taxable_amount - slab2)) #set tax = 10%
    elif(slab3 < taxable_amount <= slab4): # if the taxable income is above slab3 <= slab4 then it will be executed
        tax = 45000 + (0.15 * (taxable_amount - slab3)) #set tax = 15%
    elif(slab4 < taxable_amount <= slab5): # if the taxable income is above slab4 <= slab5 then it will be executed
        tax = 90000 + (0.20 * (taxable_amount - slab4)) #set tax = 20 %
    else :  #if the taxable income is above slab2 then else will executed
        tax = 150000 + (0.30 * (taxable_amount - slab5)) #set tax = 30%
    
    # adding the health and education cess amount with tax   
    tax = tax + (tax * health_education_cess)
    print("Your Tax amount is : ",tax)
        
#just printing title       
print("!!Income Tax Calculator!!")
print("-------------------------")
option = int(input("1.Old Tax Regime\n2.New Tax Regime\nEnter your Choice : "))#ask choice for old and new tax regime if old press 1 and new press 2
if(option == 1): #if the option is 1 then it will executed
    #ask user to enter annual income and age
    Annual_Income = float(input("Enter your Annual Income Salary : "))
    while Annual_Income < 0 : #using while loop to check number is not in negative
        print("Please Dont enter negative number!!")
        Annual_Income = float(input("Enter your Annual Income Salary : "))
    age = int(input("Enter Your Age : "))
    while age < 0 : #using while loop to check number is not in negative
        print("Please enter correct age because your age is not in Negative")
        age = int(input("Enter Your Age : ")) 
    Standard_deduction = 50000
    Section_80C_80CCC_80CCD_deduction =float(input("Enter your amount under Section 80C,80CCC,80CCD(NPS,PPF,LIC,SchoolFee,FD etc...,) (Max_Limit : 2 lakhs): "))
    while Section_80C_80CCC_80CCD_deduction > 200000 or Section_80C_80CCC_80CCD_deduction < 0 : #using while loop to check number is not in negative and less than maxlimit
        if(0 > Section_80C_80CCC_80CCD_deduction):# if the number negative then it will executed
            print("Please Dont enter negative Number")
            Section_80C_80CCC_80CCD_deduction = float(input("Enter your amount under Section 80C,80CCC,80CCD(NPS,PPF,LIC,SchoolFee,FD etc...,) (Max_Limit : 2 lakhs): "))
        elif(0 < Section_80C_80CCC_80CCD_deduction and 200000 < Section_80C_80CCC_80CCD_deduction): # if the number >Max limit then it will executed
            print("Enter amount upto 2 laks  ")
            Section_80C_80CCC_80CCD_deduction =float(input("Enter your amount under Section 80C,80CCC,80CCD(NPS,PPF,LIC,SchoolFee,FD etc...,) (Max_Limit : 2 lakhs): "))
    HRA = float(input("Enter your HRA Exectention : "))
    while HRA > (Annual_Income * 0.5) or HRA < 0 : #using while loop to check number is not in negative and less than maxlimit
        if(HRA < 0): # if the number negative then it will executed
            print("Please Dont enter Negative Number")
            HRA = float(input("Enter your HRA Exectention : "))
        elif(0 < HRA and HRA > (Annual_Income * 0.5)): # if the number >Maxlimit then it will executed
            print("Please calculate correct HRA because your HRA is >= '50%' of Annual Salary")
            HRA = float(input("Enter your HRA Exectention : "))
    Medical_Insurance = float(input("Enter your Medical Insurance amount under Section 80D (MaxLimit : 25000) : "))
    while Medical_Insurance < 0 or Medical_Insurance > 25000 : #using while loop to check number is not in negative and less than maxlimit
        if Medical_Insurance < 0 : # if the number negative then it will executed
            print("!!Please Dont enter Negative Number!!")
            Medical_Insurance = float(input("Enter your Medical Insurance amount under Section 80D (MaxLimit : 25000) : "))
        elif(0 < Medical_Insurance and 25000 < Medical_Insurance) : # if the number >Maxlimit then it will executed
            print("Please Enter amount upto 25K")
            Medical_Insurance = float(input("Enter your Medical Insurance amount under Section 80D (MaxLimit : 25000) : "))
    #deducting the given deduction amount in Annual Income and set to taxable income 
    taxable_amount = Annual_Income - Standard_deduction - Section_80C_80CCC_80CCD_deduction - HRA - Medical_Insurance
    if (taxable_amount <= 0): #if the taxable_amount <= 0 then it will executed
        print("Your Deduction is Higher than your Annual Income")
        print("Your Tax Amount is : 0")
    else : #otherwise it will executed
        print("Your Taxable Amount is : ",taxable_amount)
        print("Your age is : ",age)
        Old_tax_regime(age , taxable_amount) #calling the function "Old_tax_regime" with passing 2 arguments
        
elif(option == 2): #if the user press 2 then it will executed
    
    #ask annual income from user
    Annual_Income = float(input("Enter your Annual Income Salary : "))
    Standard_deduction = 50000 #set standard deduction
    taxable_amount = Annual_Income - Standard_deduction #deducting the given deduction amount in Annual Income and set to taxable income 
    if (taxable_amount <= 0): #if the taxable_amount <= 0 then it will executed
        print("Your Deduction is Higher than your Annual Income")
        print("Your Tax Amount is : 0")
    else : #otherwise it will executed
        print("Your Taxable Amount is : ",taxable_amount)
        New_tax_regime(Annual_Income) #calling the function "New_tax_regime" with passing arguments
        
else : #if the user enter any other number then it will executed
    
    print("!!Please enter Valid Option!!")
    
        
            
                       
        
    
    
            
        
        
        
            
            
            
        
            
        
        
            
        
    
        
    