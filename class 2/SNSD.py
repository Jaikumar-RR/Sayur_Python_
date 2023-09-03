def swap2numbers(Firstnumber,Secondnumber):
    temp = Firstnumber
    Firstnumber = Secondnumber
    Secondnumber = temp
    
    print("After Swapping :")
    print("FirstNumber = ",Firstnumber)
    print("SecondNumber = ",Secondnumber)

def swap2digit(getdigit):
    firstdigit = getdigit // 10
    seconddigit = getdigit % 10
    print("After Swapping Digits :",(seconddigit*10)+firstdigit)


print("Swaping Two Numbers & Digits")
print("____________________________")
print("1.To swap two numbers ")
print("2.To swap two digits")
select = int(input("Enter 1 or 2 only : "))

if select == 1 :
    Firstnumber = int(input("Enter First Number :"))
    Secondnumber = int(input("Enter Second Number"))
    print("Before Swaping :")
    print("FirstNumber = ",Firstnumber)
    print("SecondNumber = ",Secondnumber)
    swap2numbers(Firstnumber,Secondnumber)

elif select == 2 :
    getdigit = int(input("Enter 2 digit number :"))
    if 9<getdigit and 100>getdigit :
        print("Before Swaping Digits : ",getdigit)
        swap2digit(getdigit)
    else :
        print("Please enter 2 digit number only !!!!!")

else :
    print("!! Invalid Selection !! ")


