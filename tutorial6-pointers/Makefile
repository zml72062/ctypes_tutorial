all: allocate.so

allocate.so: allocate.c
	gcc -fPIC -shared -o allocate.so allocate.c

clean:
	rm -f allocate.so