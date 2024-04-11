import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_characters.search(password) is not None

def assess_password_strength(password):
    criteria = {
        "length": check_length(password),
        "uppercase": check_uppercase(password),
        "lowercase": check_lowercase(password),
        "digit": check_digit(password),
        "special character": check_special_char(password)
    }

    strength_score = sum(criteria.values())
    strength_feedback = ""

    if strength_score == 5:
        strength_feedback = "Strong"
    elif strength_score >= 3:
        strength_feedback = "Moderate"
    else:
        strength_feedback = "Weak"

    return strength_feedback

def main():
    password = input("Enter your password: ")

    strength = assess_password_strength(password)
    print(f"The strength of your password is: {strength}")

if __name__ == "__main__":
    main()
