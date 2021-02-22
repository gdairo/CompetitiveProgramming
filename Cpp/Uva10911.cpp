#include <bits/stdc++.h>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <ios>
#include <iostream>

using namespace std;

int N, target;
double dist[20][20], memo[1 << 16];

double matching(int bitmask){
    // Iniciamos memo con -1 en la fun main
    if(memo[bitmask] > -0.5){       // Este estado ya esta calculado
        return memo[bitmask];
    }
    if (bitmask == target){         // Todos los estudiantes estan emparejados
        return memo[bitmask] = 0;   // El coste es 0
    }
    double ans = 20000000000.0;      // Inicializamos con un valor grande
    int p1, p2;
    for(p1 = 0; p1 < 2 * N; p1++){
        if(!(bitmask & (1 << p1))){
            break;                  // Encontrar el primer bit apagado
        }
    }
    for (p2 = p1 + 1; p2 < 2 * N; p2++){        // Despues intentar emparejar P1
        if(!(bitmask & (1 << p2))){
            // Elegir el minimo
            ans = min(ans, dist[p1][p2] + matching(bitmask | (1 << p1) | (1 << p2)));
        }
    }
    return memo[bitmask] = ans;     // Guardar el resultado en la tabla y volver
}


int main(){
    int i, j, caseNo = 1, x[20], y[20];
    
    // freopen("in.txt", "r", stdin);  // Archivo de entrada a stdin
    // freopen("out.txt", "w", stdout);// Archivo de salida a stdout

    while(scanf("%d", &N), N){
        for(i = 0; i < 2 * N; i++){
            scanf("%*s %d %d", &x[i], &y[i]);
        }
        for(i = 0; i < 2 * N - 1; i++){
            for(j = i + 1; j < 2 * N; j++){
                dist[i][j] = dist[j][i] = hypot(x[i] - x[j], y[i] - y[j]);
            }
        }

        memset(memo, -1.0, sizeof memo);
        target = (1 << (2 * N)) - 1;
        printf("Case %d: %.2lf\n", caseNo++, matching(0));
   }
    return 0;
}