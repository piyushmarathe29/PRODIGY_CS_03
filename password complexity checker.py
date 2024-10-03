import re

def assess_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase and lowercase letter check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
        
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Number check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Assess overall strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback
    feedback_message = "Password strength: " + strength
    if feedback:
        feedback_message += "\nSuggestions for improvement:\n- " + "\n- ".join(feedback)
    
    return feedback_message

# Example usage:
password = input("Enter a password to assess: ")
print(assess_password_strength(password))
