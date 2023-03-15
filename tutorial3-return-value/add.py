import ctypes

add = ctypes.CDLL("./add.so")
res = add.add(5, 6)
print(res)
print(type(res))

# An alternative approach
add_func = add.add
add_func.argtypes = [ctypes.c_int, ctypes.c_int]
add_func.restype = ctypes.c_int

#######################################
# It doesn't work if we write
# add_func.argtypes = [int, int]
# add_func.restype = int
#######################################

res = add.add(5, 6)
print(res)
print(type(res))