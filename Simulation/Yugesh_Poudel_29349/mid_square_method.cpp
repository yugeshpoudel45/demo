#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
int getNumberLength(int num)
{
    if (num == 0)
        return 1; // Special case for 0
    return (int)log10(num) + 1;
}

int extractMiddleDigits(int num, int totalDigits)
{
    char str[20];                               // String to hold the number as text
    sprintf(str, "%0*d", totalDigits * 2, num); // Pad the number with leading zeros

    int numDigitsSquared = strlen(str); // Get length of the padded number

    // Calculate the start index for extracting middle digits
    int start = (numDigitsSquared - totalDigits) / 2;

    char middleStr[20]; // String to hold the middle digits
    strncpy(middleStr, str + start, totalDigits);
    middleStr[totalDigits] = '\0'; // Null-terminate the string

    // Convert the middle string back to integer
    return atoi(middleStr);
}

int main()
{
    int X0, n, totalDigits;

    do
    {
        printf("Enter the value of the seed (even digits): ");
        scanf("%d", &X0);
        totalDigits = getNumberLength(X0);
    } while (totalDigits % 2 != 0);

    printf("Number of digits in %d is %d\n", X0, totalDigits);
    printf("How many random numbers do you want to generate? : ");
    scanf("%d", &n);

    int denominator = pow(10, totalDigits);

    for (int i = 0; i < n; i++)
    {
        int X1 = X0 * X0;
        int middleDigits = extractMiddleDigits(X1, totalDigits);

        float random_no = (float)middleDigits / denominator;
        printf("R%d = %.2f\n", i + 1, random_no);

        X0 = middleDigits;
    }

    return 0;
}
