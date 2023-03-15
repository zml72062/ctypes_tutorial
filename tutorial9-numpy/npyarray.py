import ctypes
import numpy as np

arrgen = ctypes.CDLL("./npyarray.so")

arrgen.getArray.restype = ctypes.POINTER(ctypes.c_long)
arr = arrgen.getArray()
npy_arr = np.ctypeslib.as_array(arr, (4, 5))
print(npy_arr)
print(npy_arr.flags)
print(npy_arr.dtype)

arrgen.printArray(arr)
arrgen.freeArray(arr)
# This will dereference a dangling pointer!
# print(npy_arr)

new_npy_arr = np.concatenate([np.array([[3, 2], [5, 4]], dtype=np.int64)]*10, axis=1)
print(new_npy_arr.flags)
# note that "as_ctypes" will copy the array
new_2d = np.ctypeslib.as_ctypes(new_npy_arr)
# new_2d is of type int[2][20] in C
print(new_2d)
arrgen.printArray(new_2d[0])
arrgen.printArray(new_2d[1])
new_1d = np.ctypeslib.as_ctypes(new_npy_arr.reshape((40,)))
# new_1d is of type int[40] in C
print(new_1d)
arrgen.printArray(new_1d)

