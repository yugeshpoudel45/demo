#include <stdio.h>

int main()
{
    double lambda = 1.0 / 10.0; // Mean inter-arrival time = 10 minutes
    double mu = 1.0 / 5.0;      // Mean service time = 5 minutes

    double rho = lambda / mu; // Traffic intensity

    double P0 = 1.0 - rho;          // Probability that a customer will not have to wait
    double L = rho / (1.0 - rho);   // Expected number of customers in the bank
    double W = 1.0 / (mu - lambda); // Expected time a customer spends in the bank

    printf("Probability that a customer will not have to wait: %.2f\n", P0);
    printf("Expected number of customers in the bank: %.2f\n", L);
    printf("Expected time a customer spends in the bank: %.2f minutes\n", W);

    return 0;
}
