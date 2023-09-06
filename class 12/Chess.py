######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

#set the size of chess board
size = 8
for row in range(size):#this loop will executed with tha var row and he range of size
    for col in range(size): #on this inner loop to executed the chess board
        if(row + col )% 2 == 0: #if the row + col is even then , it will executed
            print('\u25A0',end=' ') #end isused to
        else : #otherwise it will executed
            print('B',end = ' ')
    print()