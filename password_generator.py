import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    # Build character set based on user preferences
    characters = ""
    
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure at least one character set is selected
    if not characters:
        raise ValueError("No character sets selected. Enable at least one option.")
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Customizable Secure Password Generator")
    
    while True:
        try:
            # Step 1: Take password length as input
            length = int(input("Enter desired password length: "))
            
            # Step 2: Ask user for customization options
            use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            
            # Step 3: Generate password
            password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
            
            # Step 4: Display password
            print("Generated Password:", password)
            
            # Step 5: Allow multiple generations
            again = input("Generate another password? (y/n): ").lower()
            if again != 'y':
                print("Goodbye! Stay secure. 🔒")
                break
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
