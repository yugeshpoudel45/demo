#include <iostream>

// Function to calculate factorial iteratively
unsigned long long factorial(int n)
{
    // Initialize result to 1
    unsigned long long result = 1;
    // Multiply result by each integer from 1 to n
    for (int i = 1; i <= n; ++i)
    {
        result *= i;
    }
    return result;
}

int main()
{
    int number;
    std::cout << "Enter a non-negative integer: ";
    std::cin >> number;
    // Check if the number is non-negative
    if (number < 0)
    {
        std::cout << "Factorial is not defined for negative numbers." << std::endl;
    }
    else
    {
        // Calculate and print factorial
        std::cout << "Factorial of " << number << " is " << factorial(number) << std::endl;
    }
    return 0;
}
