all: array.so

array.so: array.c
	gcc -fPIC -shared -o array.so array.c

clean:
	rm -f array.so