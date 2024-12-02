import random
import string

def generate_password(num_letters):
    try:
        with open('dictionary.txt', 'r') as file:
            words = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("Dictionary file not found!")
        return None

    password = ''
    
    while len(password) < num_letters:
        word = random.choice(words)
        if len(password) + len(word) <= num_letters:
            password += word
    
    password = password[:num_letters]
    
    return password

def main():
    while True:
        try:
            num_letters = int(input("Enter the number of letters for your password (max 15): "))
            if num_letters <= 15:
                break
            else:
                print("Password length must not exceed 15 characters. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(num_letters)
    if password:
        print(f"Generated password: {password}")

if __name__ == '__main__':
    main()
