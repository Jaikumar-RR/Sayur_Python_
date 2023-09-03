#Problem Statement....
#Calculate and print which Standard te Student is studying
#Program to ask the user for his/her name and print Hello,user name & get user born year
#Calculate if the user is going to elementary school , middle school , highschool or collage based on users age

#This program based on my assumption....

#Program
#importing date from datetime Modules
from datetime import date

#To define a function 'StudentStandard' with 2 parameters 
def StudentStandard(name,age):
    print("Hello!!,",name)#print Hello,username
    if(age<5): #eg. 3<5 
        #print age and eligibility
        print("Your age is :",age)
        print("You are not eligible to join school,\nThe eligible age to join school is : 5")
    elif(age>=5 and age<11): # age is above/eguals to 5 and below 11 
         #print age and eligibility
        print("Your age is :",age)
        print("You are in elementary school standards")
    elif(age>=11 and age<=14): # age is above/equals to 11 and below/equals to 14
         #print age and eligibility
        print("Your age is :",age)
        print("You are in middle school standards")
    elif(age>=15 and age<18): # age is above/eguals to 15 and below 18
         #print age and eligibility
        print("Your age is :",age)
        print("You are in High school standards")
    elif(age>=18 and age<25): # age is above/eguals to 18 and below 25
          #print age and eligibility
         print("Your age is :",age)
         print("You are in Collage standards")
    else : #age ig above/equals to 25
        print("May be your are finished your collage life")


Student_name = input("Enter your name :") #geting user name 
  
Student_bornYear = int(input("What year were you born :")) #geting user year they born

todays_date = date.today()
#CurrentYear = todays_date.year 
CurrentYear = 2023
if(Student_bornYear>CurrentYear):
    print(Student_name,"Please enter correct Year!!!,\n Current Year is :",CurrentYear)
else :
    Student_age = CurrentYear-Student_bornYear
    StudentStandard(Student_name,Student_age)


    
    

    




