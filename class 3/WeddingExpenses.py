#Problem Statement
#Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per person is half of lunch cost. Cost of the hall is Rs 200 per person.  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. Decide what should be the input and calculate the cost.

#To def a function 'Wedding_Calculation' with parameter
def Wedding_Calculation(no_of_persons):

    LunchCost = 200*no_of_persons  #Assigning the Cost of Lunch for one person is 200
    Breakfast = LunchCost/2        #Assigning the Cost of Breakfast for one person is 50% of lunchcost
    HallCost = 200*no_of_persons   #Assigning the Cost of HallCost for one person is 200
    decoration = HallCost*0.5      #Assigning the Cost of decoration is 50% from hall cost
    Parking = HallCost*0.10        #Assigning the Cost of Parking is 10% from hallcost
    #Calculating the Total Cost 
    TotalCost = LunchCost+Breakfast+HallCost+decoration+Parking
    #Printing the Cost Statements  
    print("Lunch Cost :",LunchCost)
    print("BreakFast Cost :",Breakfast)
    print("Hall Cost :",HallCost)
    print("Decoration Cost :",decoration)
    print("Parking Cost :",Parking)
    print("Total wedding expenses is :",TotalCost)

#Just printing Title
print("!!Wedding Expenses Calculation!!")
#Getting the input from user for No of person Attendence and printing it 
No_of_PersonAttendence = int(input("Enter How many people should attend this function :"))
print("There is ",No_of_PersonAttendence,"should attend this function")
Wedding_Calculation(No_of_PersonAttendence) #Calling the Wedding_Calculation function with passing an arguments