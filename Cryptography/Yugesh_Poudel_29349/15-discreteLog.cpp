#include <iostream>
#include <cmath>
#include <unordered_map>
using namespace std;
int discreteLog(int, int, int);
int modularInverse(int, int);
int main()
{
    int g, y, n;
    do
    {
        cout << "Enter base (g): ";
        cin >> g;
        cout << "Enter value (y): ";
        cin >> y;
        cout << "Enter modulus (n): ";
        cin >> n;
        int result = discreteLog(g, y, n);
        if (result != -1)
            cout << "Discrete logarithm x such that " << g << "^x === " << y << " (mod " << n << ") is: " << result << endl;
        else
            cout << "No discrete logarithm found for the given inputs." << endl;
        char choice;
        cout << "Do you want to continue (y/n): ";
        cin >> choice;
        if (choice == 'n')
            break;
    } while (true);
//    cout << "\nName: Yugesh Poudel\nRoll no: 22\n";
    return 0;
}

int discreteLog(int g, int y, int n)
{
    unordered_map<int, int> giantStep;
    int m = static_cast<int>(sqrt(n)) + 1;
    int value = 1;
    for (int j = 0; j < m; ++j)
    {
        giantStep[value] = j;
        value = (value * g) % n;
    }
    int invM = 1;
    for (int j = 0; j < m; ++j)
    {
        invM = (invM * g) % n;
    }
    invM = modularInverse(invM, n);
    value = y;
    for (int i = 0; i < m; ++i)
    {
        if (giantStep.find(value) != giantStep.end())
        {
            return i * m + giantStep[value];
        }
        value = (value * invM) % n;
    }
    return -1;
}

int modularInverse(int a, int n)
{
    int t = 0, newT = 1;
    int r = n, newR = a;
    while (newR != 0)
    {
        int quotient = r / newR;
        int tempT = newT;
        newT = t - quotient * newT;
        t = tempT;
        int tempR = newR;
        newR = r - quotient * newR;
        r = tempR;
    }
    if (r > 1)
    {
        return -1;
    }
    if (t < 0)
    {
        t += n;
    }
    return t;
}
