all: string.so

string.so: string.c
	gcc -fPIC -shared -o string.so string.c

clean:
	rm -f string.so