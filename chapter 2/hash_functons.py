"""
Code Examples of Hash Functions
"""

import hashlib
# hashlib module is a popular module to do hashing in python

# Constructors of md5(), sha1(), sha224(), sha256(), sha384(), and sha512() present in hashlib

md = hashlib.md5()
md.update("The quick brown fox jumps over the lazy dog".encode())  # Encoding the string to bytes
print(md.digest())
print("Digest Size:", md.digest_size, "\n\rBlock Size: ", md.block_size)

# Comparing digest of SHA224, SHA256,SHA384, SHA512
print ("Digest SHA224", hashlib.sha224("The quick brown fox jumps over the lazy dog".encode()).hexdigest())
print ("Digest SHA256", hashlib.sha256("The quick brown fox jumps over the lazy dog".encode()).hexdigest())
print ("Digest SHA384", hashlib.sha384("The quick brown fox jumps over the lazy dog".encode()).hexdigest())
print ("Digest SHA512", hashlib.sha512("The quick brown fox jumps over the lazy dog".encode()).hexdigest())

# RIPEMD160 160 bit hashing example
h = hashlib.new('ripemd160')
h.update("The quick brown fox jumps over the lazy dog".encode())
print ("Digest RIPEMD160", h.hexdigest())