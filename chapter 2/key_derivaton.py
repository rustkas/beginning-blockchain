import hashlib, binascii

# Key derivation algorithm:
# Native hashing algorithms are not resistant against brute force attacks.
# Key derivation algorithms are used for securing password hashing.

algorithm = 'sha256'
password = 'HomeWifi'.encode()  # Convert the string to bytes
salt = 'salt'.encode()  # Convert the string to bytes
nu_rounds = 1000
key_length = 64  # dklen is the length of the derived key

# Generate the key using PBKDF2-HMAC
dk = hashlib.pbkdf2_hmac(algorithm, password, salt, nu_rounds, dklen=key_length)

# Output the results
print('derived key:', dk)
print('derived key in hexadecimal:', binascii.hexlify(dk))
