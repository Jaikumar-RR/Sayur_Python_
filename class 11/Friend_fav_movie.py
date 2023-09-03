############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

# To set variables for friend 1 and 2 to get their favourite movies
friend1_movies = input("First friend, enter the movies you like (comma-separated): ").lower().split(',')
friend2_movies = input("Second friend, enter the movies you like (comma-separated): ").lower().split(',')

common_movies = [] #set an empty list variable to store common movies


for movie in friend1_movies: #by using for loop to assign friend1 movie list on movie variable to check on friend 2 list
    
    if movie in friend2_movies:  #if the movie has in friend2 means it stored to common movie
        
        common_movies.append(movie)
        
        if len(common_movies) >= 3: #if the len of common movie is greater than or equal to 3 means it will executed
            break

# Print common movies
if common_movies: #if common_movie contains any value means it will executed
    print("You both like these movies:")
    for movie in common_movies: #by using for loop to print common Movie name
        print(movie)
else: #otherwise it will exected
    print("You don't have common favorite movies.")
