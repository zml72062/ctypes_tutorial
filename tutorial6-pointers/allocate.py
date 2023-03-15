import ctypes

clib = ctypes.CDLL("./allocate.so")

# Pointer return types are treated as integers
cstr_ptr = clib.alloc_memory()
print(cstr_ptr)
print(type(cstr_ptr))

# To interpret the return value of "alloc_memory"
# as pointers, we have to designate "restype"
clib.alloc_memory.restype = ctypes.POINTER(ctypes.c_char)
cstr_ptr = clib.alloc_memory()
print(cstr_ptr)
print(type(cstr_ptr))

# We can do pointer arithmetics like in C using
# operator []
for i in range(15):
    print(cstr_ptr[i], end=" ")
print()

##########################################
# Notice: Don't do this!
#
# for c in cstr_ptr:
#     print(c, end=" ")
#
# The C pointer doesn't know the length
# of the string, and this will lead to
# a Segmentation Fault.
##########################################

# The "zero_memory" and "free_memory" functions takes
# pointer types as input
clib.zero_memory(cstr_ptr)
for i in range(15):
    print(cstr_ptr[i], end=" ")
print()

clib.free_memory(cstr_ptr)
