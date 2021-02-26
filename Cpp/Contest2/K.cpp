#include <bits/stdc++.h>
#include <cstdint>
#include <ios>
#include <iostream>

using namespace std;
#define endl '\n';

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int n[3], p[3];
    long long r, ans = 0;
    string str;

    cin >> str;
    cin >> n[0] >> n[1] >> n[2];   
    cin >> p[0] >> p[1] >> p[2];
    cin >> r;

    int arr[3];
    memset(arr, 0, sizeof arr);
    for (char c: str) {
        arr[(c == 'B') ? 0 : (c == 'S') ? 1 : 2]++; 
    }

    bool done = false;
    int minimo = INT32_MAX;
    int resto[3], answer[3];

    for(int i = 0; i < 3; i++) {
        if(arr[i]){
            answer[i] = n[i] / arr[i];
            minimo = min(minimo, answer[i]);
            resto[i] = n[i] % arr[i];
        } else {
            answer[i] = 0;
            resto[i] = 0;
        }
    }
    cout << minimo << endl;
    cout << resto[0] << resto[1] << resto[2] << endl;

    return 0;
}