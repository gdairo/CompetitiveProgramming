#include <bits/stdc++.h>
#include <ios>
#include <iostream>

using namespace std;
#define endl '\n';

char crossword[10][10];
string words;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            cin >> crossword[i][j];
    
    cin >> words;

    cout << words << endl;

    return 0;
}
