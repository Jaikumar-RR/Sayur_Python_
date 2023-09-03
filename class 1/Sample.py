std1 = 1000
std2 = 800
std3 = 1200
total_rupee = std1 + std2 + std3
print("Total Rupees :",total_rupee)
spend = 2000
print("Spending amt :",spend)
bal = total_rupee - spend
print("Balance :",bal)
print("Amount to pay for Student 1 :",bal*(std1/total_rupee))
print("Amount to pay for Student 2 :",bal*(std2/total_rupee))
print("Amount to pay for Student 3 :",bal*(std3/total_rupee))
print("-------------------")


