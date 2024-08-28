#include <stdio.h>

int main()
{
    float transitionMatrix[2][2] = {
        {0.9, 0.1},
        {0.5, 0.5}};

    float initialWeather[2] = {1.0, 0.0};

    float nextDayWeather[2] = {0.0, 0.0};

    nextDayWeather[0] = initialWeather[0] * transitionMatrix[0][0] + initialWeather[1] * transitionMatrix[1][0];
    nextDayWeather[1] = initialWeather[0] * transitionMatrix[0][1] + initialWeather[1] * transitionMatrix[1][1];

    printf("Weather probabilities for the next day:\n");
    printf("Sunny: %.2f\n", nextDayWeather[0]);
    printf("Rainy: %.2f\n", nextDayWeather[1]);

    return 0;
}
