# 2. Check if the username and password is correct.  
#       Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end. 
#       passward is the first, third, and last 3 letters of the username followed by the first three letters of the  
#       name of the company mentioned in the username, followed by any 3 numbers. 
#       eg username : myname@sayur.com. password - mnamesay123


import random
#def a function for valid user
def is_valid_username(username):
    if "@" in username: # if the user name contains @ means it will executed
        domain_endings = [".com", ".edu", ".tech", ".org"] #set domain ending
        for ending in domain_endings: # set the end on ending using loop
            if username.endswith(ending):#endswith() is used to check the value is on ending or not
                return True
    return False

#def a function to generate password
def generate_password(username):
    if is_valid_username(username):#if it is valid user name means it will executed
        username_parts = username.split("@") #it split the name and .com
        if len(username_parts) == 2: #len of username_part == 2
            username_prefix = username_parts[0] #set the name into variable 
            domain = username_parts[1].split(".")[0]
            
            if len(username_prefix) >= 2 and len(domain) >= 3:
                random_number = random.randint(0, 999)
                password = username_prefix[:5] + domain[:3] + str(f'{random_number:03d}')
                return password
    return None

# Test with a username
username = input("Enter Your Mail_Id : ")
password = generate_password(username)

if password:
    print(f"Username: {username}")
    print(f"Generated Password: {password}")
else:
    print("Invalid username.")