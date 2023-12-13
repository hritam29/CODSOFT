import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    all_characters = lower_case + upper_case + digits + special_characters

    # Ensure the password length is at least 8 characters
    length = max(8, length)

    # Generate a random password using the selected character sets
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Get user input for the desired length of the password
        password_length = int(input("Enter the desired length of the password: "))

        # Generate and display the password
        password = generate_password(password_length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
