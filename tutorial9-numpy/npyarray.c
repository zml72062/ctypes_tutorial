#include <stdlib.h>
#include <stdio.h>

long* getArray()
{
    long* array = (long*)malloc(sizeof(long) * 20);
    for (long i = 0; i < 20; i++)
    {
        array[i] = i;
    }
    return array;
}

void printArray(long* array)
{
    for (int i = 0; i < 20; i++)
    {
        printf("%ld ", array[i]);
    }
    printf("\n");
}

void freeArray(long* array)
{
    printf("Freed!\n");
    free(array);
}