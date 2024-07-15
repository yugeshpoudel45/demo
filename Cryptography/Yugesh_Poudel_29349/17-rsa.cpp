#include <iostream>
#include <cmath>
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
long long encrypt(long long message, long long e, long long n)
{
    return mod_pow(message, e, n);
}
long long decrypt(long long encrypted, long long d, long long n)
{
    return mod_pow(encrypted, d, n);
}
int main()
{
    long long p, q, n, phi, e, d;
    long long message, encrypted, decrypted;
    char choice;
    cout << "RSA Encryption and Decryption Menu" << endl;
    do
    {
        cout << "1. Key Generation\n2. Encrypt\n3. Decrypt\n4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case '1':
            cout << "Enter two prime numbers (p and q): ";
            cin >> p >> q;
            n = p * q;
            phi = (p - 1) * (q - 1);
            cout << "Enter a public key (e): ";
            cin >> e;
            d = 1;
            while ((d * e) % phi != 1)
            {
                d++;
            }
            cout << "Keys generated: " << endl;
            cout << "Public key (e, n): (" << e << ", " << n << ")" << endl;
            cout << "Private key (d, n): (" << d << ", " << n << ")" << endl;
            break;
        case '2':
            cout << "Enter the message to encrypt: ";
            cin >> message;
            encrypted = encrypt(message, e, n);
            cout << "Encrypted message: " << encrypted << endl;
            break;
        case '3':
            cout << "Enter the message to decrypt: ";
            cin >> encrypted;
            decrypted = decrypt(encrypted, d, n);
            cout << "Decrypted message: " << decrypted << endl;
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