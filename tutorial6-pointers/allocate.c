#include <stdlib.h>
#include <stdio.h>

char* alloc_memory()
{
    char* str = (char*)calloc(15, sizeof(char));
    printf("Memory allocated!\n");
    for (int i = 0; i < 15; i++)
    {
        str[i] = "Hello, World!\n"[i];
    }
    return str;
}

void zero_memory(char* ptr)
{
    printf("Memory zeroed!\n");
    for (int i = 0; i < 15; i++)
    {
        ptr[i] = 0;
    }
}

void free_memory(char* ptr)
{
    printf("Memory freed!\n");
    free(ptr);
}


