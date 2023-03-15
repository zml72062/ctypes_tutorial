all: test.so

test.so: test.cpp
	g++ -fPIC -shared -o test.so test.cpp

clean:
	rm -f test.so