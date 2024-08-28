#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int num_points;
    printf("Enter the number of Points: \n");
    scanf("%d", &num_points);
    int inside_circle = 0;
    srand(time(NULL));
    for (int i = 0; i < num_points; i++)
    {
        float x = (float)rand() / RAND_MAX;
        float y = (float)rand() / RAND_MAX;

        if ((x * x + y * y) <= 1.0)
        {
            inside_circle++;
        }
    }

    double pi_estimate = 4.0 * inside_circle / num_points;
    printf("Estimated value of PI: %.5f\n", pi_estimate);

    return 0;
}
