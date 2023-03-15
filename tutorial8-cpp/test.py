import ctypes

cpplib = ctypes.CDLL("./test.so")
# This won't work, since C++ uses name mangling
# cpplib.func(12)
cpplib.c_func(12)

# Generally, you should use C++ for implementation
# and C for interface (within extern "C")