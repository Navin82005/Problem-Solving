#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        if (n == 2)
        {
            cout << "NO\n";
            continue;
        }

        cout << "YES\n";
        if (n % 2 == 1)
        {
            int val = n / 2;
            for (int i = 1; i <= val; i++)
                cout << i << ' ';
            for (int i = n; i > val; i--)
                cout << i << ' ';
            cout << '\n';
        }
        else
        {
            int val = (n / 2);

            for (int i = 2; i <= val; i++)
                cout << i << ' ';
            cout << 1 << ' ';
            for (int i = n; i > val; i--)
                cout << i << ' ';
            cout << '\n';
        }
    }

    return 0;
}