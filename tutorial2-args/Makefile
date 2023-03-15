all: format.so

format.so: format.c
	gcc -fPIC -shared -o format.so format.c

clean:
	rm -f format.so