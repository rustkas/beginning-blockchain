import ecdsa

# SECP256k1 is the Bitcoin elliptic curve
signingKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Get the verifying key
verifyingKey = signingKey.get_verifying_key()

# Generate the signature of a message
message = b"signed message"
signature = signingKey.sign(message)

# Verify the signature is valid for a message
print("Is the signature valid for the message?", verifyingKey.verify(signature, message))  # True. Signature is valid

# Try to verify the signature for a different message
try:
    assert verifyingKey.verify(signature, b"message")  # Throws an error. Signature is invalid for this message
except ecdsa.keys.BadSignatureError:
    print("The signature is invalid for the message.")
