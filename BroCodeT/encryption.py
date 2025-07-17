def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Q to quit): ").upper()

        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ('E', 'D'):
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter shift (number): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 'E':
                encrypted = encrypt(message, shift)
                print(f"Encrypted message: {encrypted}")
            else:
                decrypted = decrypt(message, shift)
                print(f"Decrypted message: {decrypted}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
