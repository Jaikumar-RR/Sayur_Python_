#Calculation of Wedding Expenses
#Cost for lunch per person is Rs200. Cost for Breakfast per person is half of lunch cost. Cost of the hall is Rs 200 per person.Decoration is 50% of Hall cost. Parking is 10% of the Hall cost.Decide what should be the input and calculate the cost. 
#Spliting the total cost for Bride and Groom equally and Bride has saved Rs50000. Determine if the bride has to take a loan or not. If loan, how much?
#Calculating the given expenses cost with no of person attendence and also bride loan calculation .

#This program based on my Assumption

#To def a function 'Wedding_Calculation' with parameter
def Wedding_Calculation(no_of_persons,):
    LunchCost = 200*no_of_persons #Assigning the Cost of Lunch 
    Breakfast = LunchCost/2    #Assigning the Cost of Breakfast
    HallCost = 200*no_of_persons #Assigning the Cost of Hall 
    decoration = HallCost*0.5    #Assigning the Cost of Decoration
    Parking = HallCost*0.10    #Assigning the Cost of Parking

    #Calculating the Total Cost 
    TotalCost = LunchCost+Breakfast+HallCost+decoration+Parking 
    #Printing the Cost Statements  
    print("Lunch Cost :",LunchCost)
    print("BreakFast Cost :",Breakfast)
    print("Hall Cost :",HallCost)
    print("Decoration Cost :",decoration)
    print("Parking Cost :",Parking)
    print("Total wedding expenses is :",TotalCost)
    print("---------------------------")
    
    #Spliting Total cost for Bride and Groom
    Bride = TotalCost/2
    

    #identifying the bride has to take loan or not
    if(Bride<=50000):  # 25000<50000 then, if statement is execute and also show balance amount
        bal = 50000 - Bride
        print("Bride saves Rs.50000 and the TotalCost for Bride is :",Bride)
        print ("You don't need to take loan\nand also has balance amount :",bal)
    else : #otherwise execute else statement and show the loan amount to take by Bride
        print("Bride need to take Loan, Because you have only 50000 the Totalcost for you is :",Bride)
        loan = Bride - 50000
        print("Loan Amount You need to take is :",loan)



#Just printing Title
print("!!Wedding Expenses Calculation!!")
print("________________________________")
#Getting the input from user for No of person Attendence and printing it 
No_of_PersonAttendence = int(input("Enter How many people should attend this function :"))
print("There is ",No_of_PersonAttendence,"should attend this function")
Wedding_Calculation(No_of_PersonAttendence) #Calling the Wedding_Calculation function with passing an arguments
