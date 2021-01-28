/**
* @Author Dairo Garcia
* 
* https://codeforces.com/contest/1157/problem/A
*
*/

tailrec fun quitarZeros(x: Int): Int = if (x % 10 == 0) quitarZeros(x / 10) else x

fun f(x: Int) = quitarZeros(x + 1)  

fun main() {
    var n = readLine()!!.toInt()

    var alcanzado = HashSet<Int>()
    while(alcanzado.add(n)) n = f(n)
    
    println(alcanzado.size)
}