######## Problem  1.1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
#same problem as above, but output should have the student name and all the marks in the same line.

#get input from user 
Subjects = int(input("Enter How many subject you have : "))
Students = int(input("Enter students count : "))
for student in range(Students): #by using for loop to get student name
    student_name = input(f"Enter student name {student+1}: ")
    print("Enter marks for ",student_name)
    marks = [] #set an empty list
    for subject in range(Subjects):#on this loop we gets marks
        mark = int(input(f"enter Marks for Subject {subject+1} : "))
        marks.append(mark)        #append() is used to append the value on list
    print(f"{student_name}'s,Marks for Subject are :",marks)    #print the marks
