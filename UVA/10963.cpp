#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, w, y1, y2;
    scanf("%d", &n);
    while (n--)
    {
        scanf("%d", &w);
        set<int> ans;
        for (int i = 0; i < w; i++)
        {
            scanf("%d %d", &y1, &y2);
            ans.insert(abs(y1 - y2));
        }

        if (ans.size() == 1)
        {
            cout << "yes" << endl;
        }
        else
        {
            cout << "no" << endl;
        }

        if (n)
        {
            cout << endl;
        }
    }

    return 0;
}