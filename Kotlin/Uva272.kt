/*
*   @author Dairo García Naranjo
*   https://vjudge.net/problem/UVA-00272  
*/

fun main() {
    var str: String
    var bool: Boolean = true
    while(true) {
        str = readLine()!!
        if(str.length == 0) break
        var arr = str.toCharArray()
        for(char in arr) {
            if(char.compareTo('\"') == 0) {
                if(bool) print("``") else print("''")
                bool = !bool
            } else {
                print(char)
            }
        }
    }
}