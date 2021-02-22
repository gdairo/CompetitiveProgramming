#include <bits/stdc++.h>

using namespace std;

int N;
char x[110];

int main(){

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d\n", &N);
    while(N--){
        scanf("0.%[0-9]...\n", &x);
        printf("the digits are 0.%s\n", x);
    }
    return 0;
}