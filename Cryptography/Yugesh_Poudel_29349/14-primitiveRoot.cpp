#include <iostream>
#include <vector>
using namespace std;

int power(int a, int b, int m)
{
    int result = 1;
    a = a % m;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            result = (result * a) % m;
        }
        a = (a * a) % m;
        b = b / 2;
    }
    return result;
}

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

vector<int> findPrimitiveRoots(int n)
{
    vector<int> primitiveRoots;
    for (int r = 2; r < n; r++)
    {
        if (gcd(r, n) == 1)
        {
            bool isPrimitiveRoot = true;
            for (int i = 1; i <= n - 2; i++)
            {
                if (power(r, i, n) == 1)
                {
                    isPrimitiveRoot = false;
                    break;
                }
            }
            if (isPrimitiveRoot)
            {
                primitiveRoots.push_back(r);
            }
        }
    }
    return primitiveRoots;
}

int main()
{
    int n;
    do
    {
        cout << "Enter a positive integer: ";
        cin >> n;
        vector<int> primitiveRoots = findPrimitiveRoots(n);
        if (primitiveRoots.empty())
        {
            cout << "No primitive roots found for " << n << endl;
        }
        else
        {
            cout << "Primitive roots of " << n << " are: ";
//            for (int root : primitiveRoots)
//            {
//                cout << root << " ";
//            }
			for (size_t i = 0; i < primitiveRoots.size(); ++i)
		{
   			 int root = primitiveRoots[i];
    		cout << root << " ";
		}

            cout << endl;
        }
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
