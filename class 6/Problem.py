
#Calculate the Grade for a student, using 3 marks.
#The student has 100 marks in any one subject, Grade is A.
#if the student has 90 or above in any one subject  Grade is B
#if the student has 60 or above in any one subject  Grade is C
#if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.
#Code


#getting an marks from user
mark1 = int(input("Enter the 1st subject mark"))
mark2 = int(input("Enter the 1st subject mark"))
mark3 = int(input("Enter the 1st subject mark"))

if(mark1<=100 and mark2<=100 and mark3<=100):
 if(mark1 == 100 or mark2 == 100 or mark3 == 100): #if all the marks is 100 , then it executed
    print ("Your Grade is A")
 elif(mark1 >= 90  or mark2 >= 90 or mark3 >= 90): #if any one mark is >= 90 ,then it executed 
    print ("Your Grade is B")
 elif (mark1 >= 60  or mark2 >= 60 or mark3 >= 60): #if any one mark is >= 60 ,then it executed
    print("Your Garde is C")
 elif (mark1 <= 50  and mark2 <= 50 and mark3 <= 50): #if all marks is <= 50 ,then it executed
    print ("Your Grade is F")
 else :
    print ("Your Grade is D")

else :
   print("!!enter valid marks!!")
   