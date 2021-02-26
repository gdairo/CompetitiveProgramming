#include <bits/stdc++.h>
#include <cstdio>
#include <iostream>

using namespace std;
#define endl '\n';

int factorial(int n) {
    if(n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    // freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);

    int n;
    cin >> n;

    cout << factorial(n) << endl;

    return 0;
}