/**
*
* @author Dairo Garcia
*
* https://kotlinlang.org/docs/tutorials/competitive-programming.html
*
*/

private fun readLn() = readLine()!!                         // Cadena de caracteres en una linea
private fun readInt() = readLn().toInt()                    // Un solo entero
private fun readStrings() = readLn().split(" ")             // List de cadenas
private fun readInts() = readStrings().map { it.toInt() }   // List de Enteros

fun main() {
    // Como compilar y ejecutar:    kotlinc TipsAndTricks.kt -include-runtime -d a.jar
    //                              kotlin a.jar

    val (n, k) = readInts()             // Leer dos enteros n y k

    val a = readStrings()
    println(a.joinToString("\n"))       // Imprimir en cada elemento un salto de linea
}