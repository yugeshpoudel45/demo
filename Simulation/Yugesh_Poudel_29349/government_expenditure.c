#include <stdio.h>

int main()
{
    double I, Y, T, C, G;
    double Y_minus_1 = 80;                     // Initial value of Y-1
    double G_values[5] = {20, 25, 30, 35, 40}; // Governmental expenditure for 5 years
    int year;
    for (year = 1; year <= 5; year++)
    {
        G = G_values[year - 1];
        I = 2 + 0.1 * Y_minus_1;
        Y = 45.45 + 2.27 * (I + G);
        T = 0.2 * Y;
        C = 20 + 0.7 * (Y - T);

        printf("Year %d:\n", year);
        printf("Government Expenditure (G): %.2f\n", G);
        printf("Investment (I): %.2f\n", I);
        printf("National Income (Y): %.2f\n", Y);
        printf("Tax (T): %.2f\n", T);
        printf("Consumption (C): %.2f\n\n", C);

        Y_minus_1 = Y; // Update Y-1 for the next year
    }

    return 0;
}
