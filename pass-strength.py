import string

def password_strength_checker(password):

    def is_strong(password):
        return (16 >= len(password) >= 12 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password))

    def is_medium(password):
        return (len(password) >= 8 and
                any(c.islower() for c in password) and 
                any(c.isupper() for c in password) and
                (any(c.isdigit() for c in password) or any(c in string.punctuation for c in password)))

    def is_weak(password):
        return len(password) < 8

        
    if len(password)>16:
        return "Password should be less than 16 characters"
    elif is_strong(password):
        return "Strong password"
    elif is_medium(password):
        return "Medium password"
    else:
        return "Weak password"

password = input("Enter your password: ")
print(password_strength_checker(password))
