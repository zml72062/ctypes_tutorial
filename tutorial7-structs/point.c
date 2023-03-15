#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x;
    int y;
};

void printPoint(struct Point p)
{
    printf("x: %d, y: %d\n", p.x, p.y);
}

void printPointRef(struct Point* p)
{
    printf("x: %d, y: %d\n", p->x, p->y);
}

struct Point* getPoint(int x, int y)
{
    struct Point* p = (struct Point*)malloc(sizeof(struct Point));
    p->x = x;
    p->y = y;
    return p;
}

void freePoint(struct Point* p)
{
    free(p);
}