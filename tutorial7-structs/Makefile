all: point.so

point.so: point.c
	gcc -fPIC -shared -o point.so point.c

clean:
	rm -f point.so