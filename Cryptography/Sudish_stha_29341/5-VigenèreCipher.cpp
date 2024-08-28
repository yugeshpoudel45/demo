#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string generateKey(string str, string key)
{
    int x = str.size();
    for (int i = 0;; i++)
    {
        if (x == i)
            i = 0;
        if (key.size() == str.size())
            break;
        key.push_back(key[i]);
    }
    return key;
}

string cipherText(string str, string key)
{
    string cipher_text;
    for (int i = 0; i < str.size(); i++)
    {
        char x = (str[i] + key[i]) % 26;
        x += 'A';
        cipher_text.push_back(x);
    }
    return cipher_text;
}

string originalText(string cipher_text, string key)
{
    string orig_text;
    for (int i = 0; i < cipher_text.size(); i++)
    {
        char x = (cipher_text[i] - key[i] + 26) % 26;
        x += 'A';
        orig_text.push_back(x);
    }
    return orig_text;
}

int main()
{
    int choice;
    string str, keyword, key, cipher_text, orig_text;

    while (true)
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
            cout << "Enter plain text:";
            cin >> str;
            cout << "Enter keyword:";
            cin >> keyword;
            transform(str.begin(), str.end(), str.begin(), ::toupper);
            transform(keyword.begin(), keyword.end(), keyword.begin(), ::toupper);

            key = generateKey(str, keyword);
            cipher_text = cipherText(str, key);
            cout << "Ciphertext: " << cipher_text << "\n";
            break;

        case 2:
            cout << "Enter the cipher text:";
            cin >> cipher_text;
            cout << "Enter the keyword:";
            cin >> keyword;
            transform(cipher_text.begin(), cipher_text.end(), cipher_text.begin(), ::toupper);
            transform(keyword.begin(), keyword.end(), keyword.begin(), ::toupper);

            key = generateKey(cipher_text, keyword);
            orig_text = originalText(cipher_text, key);
            cout << "Original/Decrypted Text: " << orig_text << "\n";
            break;

        case 3:
            cout << "Program Exited!!!!\n";
            cout << "\nName: Yugesh Poudel\nRoll no: 22\n";
            return 0;

        default:
            cout << "Invalid choice. Please enter 1, 2, or 3.\n";
            break;
        }
    }
}