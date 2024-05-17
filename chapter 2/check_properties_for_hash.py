# Check properties for hash
import hashlib

input_text = "Sample Input Text"
for i in range(20):  # Используем range вместо xrange
    # Add the iterator to the end of the text
    input_with_iterator = input_text + str(i)
    # Show the input and hash result
    print(input_with_iterator, ':', hashlib.sha256(input_with_iterator.encode()).hexdigest())
