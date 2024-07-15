#include <iostream>
using namespace std;
void computeTotient(int);
int main()
{
    int n;
    do
    {
        cout << "Enter a positive integer: ";
        cin >> n;
        computeTotient(n);
        cout << "Do you want to continue? (y/n): ";
        char ch;
        cin >> ch;
        if (ch == 'n' || ch == 'N')
        {
            cout << "\nName: Yugesh Poudel\nRoll no: 22\n";
            break;
        }
    } while (true);
    return 0;
}

void computeTotient(int n)
{
    long long phi[n + 1];
    for (int i = 1; i <= n; i++)
        phi[i] = i;
    for (int p = 2; p <= n; p++)
    {
        if (phi[p] == p)
        {
            phi[p] = p - 1;
            for (int i = 2 * p; i <= n; i += p)
            {
                phi[i] = (phi[i] / p) * (p - 1);
            }
        }
    }
    cout << "Totient value of " << n << ": " << phi[n] << endl;
}