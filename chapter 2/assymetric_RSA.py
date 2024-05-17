# Install pycryptodome if not already installed
# `pip install pycryptodome`

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

# Function to generate keys with default length 1024
def generate_key(KEY_LENGTH=1024):
    keyPair = RSA.generate(KEY_LENGTH)
    return keyPair

# Generate Key for ALICE and BOB
bobKey = generate_key()
aliceKey = generate_key()

# Print Public Key of Alice and Bob. This key could be shared
alicePK = aliceKey.publickey()
bobPK = bobKey.publickey()

print("Alice's Public Key:\n\r", alicePK.export_key().decode(), "\n\r")
print("Bob's Public Key:\n\r", bobPK.export_key().decode(), "\n\r")

# Alice wants to send a secret message to Bob. Let's create a dummy message for Alice
secret_message = "Alice's secret message to Bob"
print("Message:\n\r", secret_message)

# Function to generate a signature
def generate_signature(key, message):
    message_hash = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(message_hash)
    return signature

# Let's generate a signature for the secret message
alice_sign = generate_signature(aliceKey, secret_message.encode())

# Before sending the message in the network, encrypt the message using Bob's public key...
cipher_rsa = PKCS1_OAEP.new(bobPK)
encrypted_for_bob = cipher_rsa.encrypt(secret_message.encode())
print("Encrypted message:\n\r", encrypted_for_bob)

# Bob decrypts the secret message using his own private key...
cipher_rsa = PKCS1_OAEP.new(bobKey)
decrypted_message = cipher_rsa.decrypt(encrypted_for_bob)
print("Decrypted message:\n\r", decrypted_message.decode())

# Bob will use the following function to verify the signature from Alice using her public key
def verify_signature(message, PublicKey, signature):
    message_hash = SHA256.new(message)
    try:
        pkcs1_15.new(PublicKey).verify(message_hash, signature)
        return True
    except (ValueError, TypeError):
        return False

# Bob is verifying using decrypted message and Alice's public key
is_valid_signature = verify_signature(decrypted_message, alicePK, alice_sign)
print("Is Alice's signature for decrypted message valid?", is_valid_signature)
