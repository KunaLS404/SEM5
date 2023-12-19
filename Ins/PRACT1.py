'''text=input("Enter your text:")
s=int(input("Enter your Key:"))
def encrypt(text,s):              #function for Encryption
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)    
    return result
def decrypt(text,s):            #function for Decryption
    result = ""
 
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)  
        else:
            result += chr((ord(char) - s-97) % 26 + 97)
    return result
Etext=encrypt(text,s)
Dtext=decrypt(Etext,s)

print('Encrypted text: ',Etext)
print('Decrypted text: ',Dtext)'''

def multiplicative_cipher(text, key):
    return "".join(chr((ord(c) - 65) * key % 26 + 65) if c.isalpha() else c for c in text.upper())

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def multiplicative_decipher(text, key):
    inverse_key = mod_inverse(key, 26)
    if inverse_key is None:
        return "Error: Invalid key. The modular inverse does not exist."

    return "".join(chr((ord(c) - 65) * inverse_key % 26 + 65) if c.isalpha() else c for c in text)

# Example usage
plaintext = input("enter your plain text")
key = int(input("enter your key value "))

encrypted_text = multiplicative_cipher(plaintext, key)
decrypted_text = multiplicative_decipher(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

