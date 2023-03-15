all: hello.so

hello.so: hello.c
	gcc -fPIC -shared -o hello.so hello.c

clean:
	rm -f hello.so