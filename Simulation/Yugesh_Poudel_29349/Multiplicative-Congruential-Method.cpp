#include <stdio.h>

int main()
{
    int X0, a, m;

    printf("Enter the seed value : ");
    scanf("%d", &X0);

    printf("Enter the multiplier: ");
    scanf("%d", &a);

    printf("Enter the modulus : ");
    scanf("%d", &m);

    int RandomInt[100];
    float RandomNum[100];

    RandomInt[0] = X0;

    for (int i = 1; i < 100; i++)
    {
        RandomInt[i] = (a * RandomInt[i - 1]) % m;
    }

    for (int i = 0; i < 100; i++)
    {
        RandomNum[i] = (float)RandomInt[i] / m;
    }

    printf("Generated random values:\n");

    for (int i = 0; i < 100; i++)
    {
        printf("X%d=%d\tR%d=%.3f", i, RandomInt[i], i, RandomNum[i]);

        if ((i + 1) % 3 == 0)
        {
            printf("\n");
        }
        else
        {
            printf("\t");
        }
    }

    return 0;
}
