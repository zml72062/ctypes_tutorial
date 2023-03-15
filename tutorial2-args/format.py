import ctypes

clib = ctypes.CDLL('./format.so')

# Here it's necessary to pass b"John" instead of "John"
# in order to convert a Python string to a byte-array
clib.format(b"John", 18)


# An alternative approach
func = clib.format
func.argtypes = [ctypes.c_char_p, ctypes.c_int]
func.restype = None

func(b"John", 18)