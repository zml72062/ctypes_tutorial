import ctypes

stringlib = ctypes.CDLL('./string.so')
# As is warned before, we must use b"Hello World!"
# to convert a Python string to a byte array
stringlib.display(b"Hello World!")

# An alternative way
content = ctypes.c_char_p(b"Hello World!") # "b" is still required
stringlib.display(content)
# Show the memory location of the char* pointer to the string
print(content)

# A test that shows Python strings are immutable
content.value = b"Goodbye World!"
stringlib.display(content)
print(content)

# Create mutable byte arrays
content = ctypes.create_string_buffer(1024) # create buffer of 1024 bytes
content.value = b"Hello World!"
stringlib.display(content)
print(content)

content.value = b"Goodbye World!"
stringlib.display(content)
print(content)