#include <cstdio>

int sum(int x, int y)
{
    return x + y;
}

int main()
{
    int first_num = 30;
    int second_num = 40;
    printf("The sum  of %d and %d is %d.\n", first_num, second_num, sum(first_num, second_num));
}