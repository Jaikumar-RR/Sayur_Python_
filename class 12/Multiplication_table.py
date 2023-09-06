######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.

#set an list variable to store the range of which table given
Multiplicands_range = [7,16]
table_range = 12 #set the range of the table
for multiplicand in range(Multiplicands_range[0],Multiplicands_range[1]+1): #By using for loop to executed the tables
    print(f"Table {multiplicand}")
    for multiplier in range(1,table_range+1): #By using inner loop to calculate the multiplicand * multiplier
        print(f"{multiplicand} * {multiplier} : {multiplicand*multiplier}")
    print(f"{'-'*15}") #lastly just print line