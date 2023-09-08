######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

#get input from user 
Subjects = int(input("Enter How many subject you have : "))
Students = int(input("Enter students count : "))
for student in range(Students):#by using for loop to get student name and mark
    student_name = input(f"Enter student name {student+1}: ")
    print("Enter marks for ",student_name)
    marks = [] #set an empty list variable
    for subject in range(Subjects): #on inner for loop to gets mark from user
        mark = int(input(f"enter Marks for Subject {subject+1} : "))
        marks.append(mark)    #append() is used to append the value on list
        
    print("Marks for ",student_name)
    for mark_lst in range(len(marks)):#in this loop to print the mark list 
        print(f"Mark {mark_lst + 1} for Subject {mark_lst +1}are :",marks[mark_lst])    

    

          