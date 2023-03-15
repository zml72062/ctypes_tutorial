import ctypes

hello = ctypes.CDLL('./hello.so') # "./" is necessary
hello.display()