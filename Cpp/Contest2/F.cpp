#include <algorithm>
#include <bits/stdc++.h>
#include <ios>

using namespace std;
#define endl '\n';

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    // freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);

    int n, t, i, j;
    cin >> n >> t;
    vector<int> a(n);
    for (i = 0; i < n; i++){
        cin >> a[i];
    }

    int ans, t_aux;
    int maximo = 0;
    for(i = 0; i < n; i++){
        ans = 0;
        t_aux = t;
        for(j = i; j < n; j++) {
            t_aux -= a[j];
            if(t >= 0) {
                ans++;
            } else {
                break;
            }
        }
        maximo = max(maximo, ans);
    }
    
    cout << maximo << endl;

    return 0;
}
