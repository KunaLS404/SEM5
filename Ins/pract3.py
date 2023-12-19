import hashlib
import hmac
import os

def generate_key():
    """Generate a random key for HMAC."""
    return os.urandom(16)  # Use a 16-byte (128-bit) key for HMAC

def generate_mac(message, key):
    """Generate a Message Authentication Code (MAC) using HMAC."""
    mac = hmac.new(key, message, hashlib.sha256)
    return mac.digest()

def verify_mac(message, key, mac_to_verify):
    """Verify the Message Authentication Code (MAC) using HMAC."""
    generated_mac = generate_mac(message, key)
    return hmac.compare_digest(generated_mac, mac_to_verify)

# Example usage:
key = generate_key()
message = b"Hello, MAC!"

# Generate MAC
mac = generate_mac(message, key)
print("Generated MAC:", mac.hex())

# Verify MAC
is_valid = verify_mac(message, key, mac)
if is_valid:
    print("MAC is valid. The message has not been tampered with.")
else:
    print("MAC is not valid. The message may have been tampered with.")
