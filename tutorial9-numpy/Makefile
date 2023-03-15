all: npyarray.so

npyarray.so: npyarray.c
	gcc -fPIC -shared -o npyarray.so npyarray.c

clean:
	rm -f npyarray.so