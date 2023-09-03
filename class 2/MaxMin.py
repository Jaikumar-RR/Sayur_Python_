def MaxMin(num1,num2,num3) :
   print("Enter (min) /1.to find minimum among 3 number ")
   print("Enter (max) /2.to find maximum among 3 number ")
   option = input()

   if option=="min" or option=='1' :
      print("Finding Minimum Number")
      if num1<num2 and num1<num3 :
         print("The Minimum Number is :",num1)
      elif num2<num1 and num2<num3 :
         print("The Minimum Number is :",num2)
      else :
         print("The Minimum Number is :",num3)

   
   elif option =="max" or option=='2':
      print("Finding Maximum Number")
      if num1>num2 and num1>num3 :
         print("The Maximum Number is :",num1)
      elif num2>num1 and num2>num3 :
         print("The Maximum Number is :",num2)
      else :
         print("The Maximum Number is :",num3)
      
   else :
      print("Invalid Option !!!")

print("Minimum & Maximum Number Finder")
print("_______________________________")
print("Enter 3 Numbers ")
num1 = int(input("1st Number :"))
num2 = int(input("2nd Number :"))
num3 = int(input("3rd Number :"))
MaxMin(num1,num2,num3)