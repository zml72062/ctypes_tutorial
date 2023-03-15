import ctypes

# Types corresponding to "int[10]" in C
array_of_10_ints = ctypes.c_int * 10
array = array_of_10_ints()
# Default all-zero for "array"
for val in array:
    print(val, end=" ")
print()

for i in range(10):
    array[i] = i
for val in array:
    print(val, end=" ")
print()

add = ctypes.CDLL("./array.so").sum
print(add(array, 10))
