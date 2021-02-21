#include <bits/stdc++.h>

using namespace std;

// Atajos para tipos de datos "comunes" en concursos
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 10000000000


int main(){
    ios_base::sync_with_stdio(0);   // Lineas para la optimizacion de cin AND cout
    cin.tie(0);                     // Cuando se usan estos metodos no se recomienda el uso scanf AND prinf

    freopen("in.txt", "r", stdin);      // Probar el codigo con un archivo de entrada
    freopen("out.txt", "w", stdout);    // Archivo donde se guarda la salida estandar de la ejecucion

    int i = 0, index, ans, b, c, val, n, d, new_computation;
    bool a;
    int memo[n], arr[n];
    
    // Atajos para simplificar el codigo en C++ o Java
    i++;                        // Para simplificar i = i + 1;
    ans = a ? b : c;            // Para simplificar if(a) ans = b; else ans = c;
    ans += val;                 // Para simplificar ans = ans + val; y demas    
    index = (index + 1) % n;    // index++; if(index >= n) index = 0;
    index = (index + n - 1) % n;// index--; if(index < 0) index = n - 1;
    ans = (int) ((double) d + 0.5); // redondeo al entero mas cercano
    ans = min(ans, new_computation);// Atajo para minimo/maximo
    // Forma alternativa: ans <?= new_computation;
    // Operadores de bits: AND && OR ||

    // Opciones de memset habituales
    memset(memo, -1, sizeof memo);  // Inicializa table de memorizacion de DP con -1
    memset(arr, 0, sizeof arr);     // Vaciado de un array de enteros

    return 0;
}