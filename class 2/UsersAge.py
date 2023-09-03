#import date class from datetime module
from datetime import date


def ageCalculator(name,birthyear,currentyear):
    print("Hello",name)
    if currentyear>birthyear :  
        age = currentyear-birthyear
        print("Your age is :",age)
    else :
        print("!!Please Enter correct Birthyear!!")

todays_date = date.today()
currentyear = todays_date.year
print("!!!!Age Calculator!!!!")
print("----------------------")
name = input("Enter Your Name : ")
#currentyear = int(input("Enter current year : "))
birthyear = int(input("Enter your Birth Year : "))
ageCalculator(name,birthyear,currentyear)
    