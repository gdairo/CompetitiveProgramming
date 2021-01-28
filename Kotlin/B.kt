/**
* @author Dairo Garcia
* 
* https://codeforces.com/contest/1157/problem/B
*
*/

private fun readLn() = readLine()!!
private fun readInt() = readLn().toInt()

fun main() {
    val n = readInt()
    val s = readLn()
    val fl = readLn().split(" ").map { it.toInt() }

    fun f(c: Char) = '0' + fl[c - '1']

    val i = s.indexOfFirst { c -> f(c) > c }.takeIf { it >= 0 } ?: s.length

    val j = s.withIndex().indexOfFirst { (j, c) -> j > i && f(c) < c }.takeIf { it >= 0 } ?: s.length

    val ans = s.substring(0, i) + s.substring(i, j).map { c -> f(c) }.joinToString("") + s.substring(j)

    println(ans)
}