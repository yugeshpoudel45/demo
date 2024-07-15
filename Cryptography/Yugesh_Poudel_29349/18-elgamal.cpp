#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

long long mod_pow(long long a, long long b, long long c)
{
    long long result = 1;
    a = a % c;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            result = (result * a) % c;
        }
        a = (a * a) % c;
        b /= 2;
    }
    return result;
}

long long generate_random_prime()
{
    long long n = rand() % 1000 + 1000; // Generate a random number in a certain range
    for (long long i = n;; i++)
    {
        bool is_prime = true;
        for (long long j = 2; j <= sqrt(i); j++)
        {
            if (i % j == 0)
            {
                is_prime = false;
                break;
            }
        }
        if (is_prime)
        {
            return i;
        }
    }
}

int main()
{
    srand(static_cast<unsigned>(time(0)));
    long long p, g, x, y, k, m, a, b;
    long long decrypted_m; // Declare decrypted_m here
    char choice;
    do
    {
        cout << "ElGamal Cryptographic System Menu" << endl;
        cout << "1. Key Generation\n2. Encrypt\n3. Decrypt\n4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case '1':
            p = generate_random_prime();
            g = generate_random_prime();
            cout << "Enter your private key x: ";
            cin >> x;
            y = mod_pow(g, x, p);
            cout << "Keys generated: " << endl;
            cout << "Public Key (p, g, y): (" << p << ", " << g << ", " << y << ")" << endl;
            break;
        case '2':
            cout << "Enter the message to encrypt (an integer): ";
            cin >> m;
            k = rand() % (p - 2) + 1; // Random value in the range [1, p-1]
            a = mod_pow(g, k, p);
            b = (m * mod_pow(y, k, p)) % p;
            cout << "Ciphertext (a, b): (" << a << ", " << b << ")" << endl;
            break;
        case '3':
            decrypted_m = (b * mod_pow(a, p - 1 - x, p)) % p;
            cout << "Decrypted Message: " << decrypted_m << endl;
            break;
        case '4':
            cout << "Exiting the program. Goodbye!" << endl;
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != '4');
    cout << "\nName: Yugesh Poudel\nRoll no: 22\n";
    return 0;
}