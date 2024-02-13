import re

def password_strength(password):
    score=0
    
    #check if the password has at least 8 characters
    if len(password)<8:
        return "Weak: Password should be 8 characters long"
    elif len(password)>8:
        score=score+2
    
    #check if password contains at least one uppercase letter
    if re.search(r'[A-Z]', password):
        score=score+2
    else:
        return "Password should contain at least one uppercase letter"
    
    #check if password contains at least one lowercase letter
    if re.search(r'[a-z]', password):
        score=score+2
    else:
        return "Password should contain at least one lowercase letter"
    
    # Check if the password contains at least one digit
    if re.search(r'\d', password):
        score=score+1
    else:
        return "Password should contain numbers"
    
    # Check if the password contains at least one special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score=score+1
    else:
        return "Weak: Password should contain special characters"
    
    #strength checker
    if score<5:
        return "Moderate: Make your password stronger"
    elif score<7:
        return "Strong: Your password is strong"
    else:
        return "Very Strong: Your password is very strong"
    
user_password=input("Enter your password:")
print(password_strength(user_password))

