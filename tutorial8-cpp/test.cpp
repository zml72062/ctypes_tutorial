#include <iostream>

void func(int a)
{
    std::cout << a << std::endl;
}

extern "C" {
    void c_func(int a)
    {
        func(a);
    }
}