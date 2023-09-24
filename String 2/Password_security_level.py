# 1. Print the level of the password security and if the password is acceptable 
#      Weak - only alphabets or only numbers or only special chars 
#      Ok - at least one alphabet, one number and one special char 
#      strong - at least three alphabets, two numbers and one special char 
#      Very strong - same as strong, but at least 16 count 
  
#      All passwords must be at least 8 chars long. You can use RegEx if you want.


import re

def check_password_security(password):
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."

    if re.match(r'^[a-zA-Z]*$', password) or re.match(r'^[0-9]*$', password) or re.match(r'^[!@#$%^&*()_+{}:<>?]*$', password):
        return "Weak - Only alphabets, numbers, or special characters."

    if re.match(r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}:<>?])', password):
        alpha_count = len(re.findall(r'[a-zA-Z]', password))
        digit_count = len(re.findall(r'[0-9]', password))

        if alpha_count >= 3 and digit_count >= 2:
            if len(password) >= 16:
                return "Very strong"
            else:
                return "Strong"
        else:
            return "OK"

    return "Weak - Only alphabets, numbers, or special characters."

# Test with a password
password = input("Enter Your Password : ")
security_level = check_password_security(password)
print(f"Password Security Level: {security_level}")