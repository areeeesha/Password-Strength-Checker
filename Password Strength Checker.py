import string 

def password_strength_checker(password):

    # LENGTH VERIFICATION:
    if len(password) < 8:
        return "IMMEDIATE FAIL: Password must be at least 8 characters long."
    
    # PATTERN RECOGNITION:
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    symbols = set(string.punctuation)
    has_symbol = any(char in symbols for char in password)

    # SUGGESTIONS FOR IMPROVEMENT:
    suggestions = []

    if not has_uppercase:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not has_digit:
        suggestions.append("Add at least one digit (0-9).")
    if not has_symbol:
        suggestions.append("Add at least one symbol (!@#$%^&*()-+).")
    
    # PASSWORD STRENGTH EVALUATION:
    criteria = sum([has_uppercase, has_digit, has_symbol])

    if criteria == 3:
        return "STRONG: Password is secure."
    elif criteria == 2:
        return "MEDIUM: Password is moderately secure.\n""SUGGESTIONS:\n" + "\n".join(suggestions)
    else:
        return "WEAK: Password is not secure.\n""SUGGESTIONS:\n" + "\n".join(suggestions)

if __name__ == "__main__":
    print("----------------------------------")
    print("    PASSWORD STRENGTH CHECKER    ")
    print("----------------------------------")
    print("\nWelcome to Areesha's Password Strength Checker!")
    print("To exit the program, type 'exit'.")

    while True:
        sample = input("\nEnter your password: ")

        if sample.lower() == "exit":
            print("Exiting the password strength checker. \nThank you for using Areesha's Password Strength Checker!")
            break       
        
        result = password_strength_checker(sample)
        print(result)