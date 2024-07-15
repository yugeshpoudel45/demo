#include <iostream>
#include <string>

using namespace std;

int getKey()
{
    int key;
    cin >> key;
    if (key < 0 || key > 25)
    {
        cout << "Invalid key. Enter again: ";
        return getKey();
    }
    return key;
}

string encrypt(string text, int key)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isalpha(text[i]))
        {
            char base = islower(text[i]) ? 'a' : 'A';
            char encrypted = ((text[i] - base + key) % 26) + base;
            result += encrypted;
        }
        else
        {
            result += text[i];
        }
    }
    return result;
}

string decrypt(string cipher, int key)
{
    return encrypt(cipher, 26 - key);
}

int main()
{
    int choice;
    int key;
    string plaintext, ciphertext;

    do
    {
        cout << "Choose an option:\n";
        cout << "1 for Encryption.\n";
        cout << "2 for Decryption\n";
        cout << "3 for Exit\n";
        cout << "Enter your choice (1/2/3): ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter plaintext: ";
            cin.ignore();
            getline(cin, plaintext);
            cout << "Enter key (0 to 25): ";
            key = getKey();
            ciphertext = encrypt(plaintext, key);
            cout << "Encrypted Text: " << ciphertext << endl
                 << endl;
            break;

        case 2:
            cout << "Enter ciphertext: ";
            cin.ignore();
            getline(cin, ciphertext);
            cout << "Enter key (0 to 25): ";
            key = getKey();
            plaintext = decrypt(ciphertext, key);
            cout << "Decrypted Text: " << plaintext << endl
                 << endl;
            break;

        case 3:
            cout << "Program Exited!!!!\n";
            break;
        default:
            cout << "Invalid choice. Please enter 1, 2, or 3.\n";
            break;
        }
    } while (choice != 3);

    cin.get();
    cout << "\nLab report by: Yugesh Poudel\nRoll no: 22\n";
    return 0;
}
