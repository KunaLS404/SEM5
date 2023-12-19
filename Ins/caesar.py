def encrypt_caesar(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

# Take input from the user
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

encrypted_text = encrypt_caesar(plaintext, shift)
decrypted_text = decrypt_caesar(encrypted_text, shift)

print("\nPlaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
