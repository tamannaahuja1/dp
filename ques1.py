def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else : 
            result += chr((ord(char) + s - 97) % 26 + 97)  
    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else :
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

def menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            s = int(input("Enter shift value: "))
            print("Encrypted text:", encrypt(text, s))
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            s = int(input("Enter shift value: "))
            print("Decrypted text:", decrypt(text, s))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
