def encrypt(text, shift):
    encrypted_text = ""
    
    # Traverse through each character in the text
    for char in text:
        # Encrypt only alphabetic characters
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            
            # Shift the character and wrap around if necessary
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # If it's not alphabetic, don't change it
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    # Decryption is just the reverse of encryption
    return encrypt(text, -shift)

# Take user inputs
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text
encrypted_text = encrypt(text, shift)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the text (for testing purposes)
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")
