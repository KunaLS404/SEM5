import random

def is_prime(n, k=5):
    """Check if a number is prime using the Miller-Rabin primality test."""
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2:
        return True

    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Apply Miller-Rabin test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_prime(bits=1024):
    """Generate a random prime number with the specified number of bits."""
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def egcd(a, b):
    """Extended Euclidean Algorithm (Iterative)."""
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0

def modinv(a, m):
    """Modular multiplicative inverse."""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_keypair(bits=1024):
    """Generate RSA key pair."""
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(1, phi)
    while egcd(e, phi)[0] != 1:
        e = random.randint(1, phi)

    # Calculate d, the modular multiplicative inverse of e (mod phi)
    d = modinv(e, phi)

    # Public key: (n, e), Private key: (n, d)
    return ((n, e), (n, d))

def encrypt(message, public_key):
    """Encrypt a message using RSA."""
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt(ciphertext, private_key):
    """Decrypt a message using RSA."""
    n, d = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_text

# Take input from the user
message = input("Enter the message to be encrypted: ")
print("Original Message:", message)

# Generate key pair
public_key, private_key = generate_keypair()

# Encrypt the message using the public key
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

# Decrypt the message using the private key
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
