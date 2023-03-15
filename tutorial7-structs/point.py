import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    
clib = ctypes.CDLL("./point.so")
p = Point(5, 6)
print(p)
print(p.x, p.y)
clib.printPoint(p)

ptr_to_p = ctypes.pointer(p)
clib.printPointRef(ptr_to_p)

clib.getPoint.restype = ctypes.POINTER(Point)
ptr = clib.getPoint(4, 2)

clib.printPointRef(ptr)
clib.printPoint(ptr.contents)
clib.freePoint(ptr)