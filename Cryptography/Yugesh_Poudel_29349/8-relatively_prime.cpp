#include <iostream>
using namespace std;

int main()
{
    do
    {
        int num1, num2;
        cout << "Enter two numbers: ";
        cin >> num1 >> num2;

        int hcf = 1;
        for (int i = 2; i <= num1 && i <= num2; ++i)
            num1 % i == 0 &&num2 % i == 0 ? hcf = i : hcf = hcf;

        if (hcf == 1)
            cout << num1 << " and " << num2 << " are relatively prime numbers." << endl;
        else
            cout << num1 << " and " << num2 << " are NOT relatively prime numbers." << endl;

        cout << "Do you want to continue? (y/n): ";
        char choice;
        cin >> choice;
        if (choice != 'y' && choice != 'Y')
        {
            break;
        }
        cin.ignore();
    } while (true);
    cout << "\nName: Yugesh Poudel\nRoll no: 22\n";
    return 0;
}