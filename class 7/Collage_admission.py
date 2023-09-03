#Problem Statement

#We have 3 colleges - each college has a different cut off mark for engineering college admission.
#Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
#For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
#for admission in College 1 and College 2

#To def a function with 5 Parameters
def Collage_admission(mark1,mark2,mark3,mark4,mark5):
    
    #Checking the all the given mark is <= 100
    if(mark1<=100 and mark2<=100 and mark3<=100 and mark4<=100 and mark5<=100):
        
        #printing Collage cutoff details 
        print("!!Collage Cutoff Details!!")
        print("-------------------")
        print("Collage 1 : 89%")
        print("Collage 2 : 93%")
        print("Collage 3 : 97%")
        print("---------------")
        
        #Calculating total and avg marks
        Total_Mark = mark1+mark2+mark3+mark4+mark5
        
        Average = Total_Mark/5
        
        print("Total Mark : ",Total_Mark)
        print("Average : ",Average,"%")
        
        
        
        if(Average>=97): # if 98>=97 then , it executed
            print("you are eligible for all three collages \nCollage 1 , Collage 2 and Collage 3")
            
        elif(Average<97 and Average>=93): #elif mark is <97 and >=93 Ex:Average = 95 then , it executed
            print("You are eligible for Collage 1 and Collage 2")
            
        elif(Average<93 and Average>=89): #elif mark is <93 and >=89 Ex:Average = 90 then , it executed
            print("You are eligible for Collage 1")
            
        else : #Otherwise else will executed
            print("You are not eligible for above given collages \nPlease!! Try other Collages")
            
    else : #they enter like >100 means else will executed
        print("!!Please Enter Valid Marks!!")
            
#Just printing titles          
print("Admission Eligibility Checking For Engineering Collages")
print("-------------------------------------------------------")
    
#getting 5 Subject marks
Subject_1_Mark = int(input("Enter Your 1st Subject Mark :"))
Subject_2_Mark = int(input("Enter Your 2nd Subject Mark :"))
Subject_3_Mark = int(input("Enter Your 3rd Subject Mark :"))
Subject_4_Mark = int(input("Enter Your 4th Subject Mark :"))
Subject_5_Mark = int(input("Enter Your 5th Subject Mark :"))
#calling the function with passing aruguments 
Collage_admission(Subject_1_Mark,Subject_2_Mark,Subject_3_Mark,Subject_4_Mark,Subject_5_Mark)
