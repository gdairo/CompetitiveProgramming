# Dairo García
# https://vjudge.net/problem/UVA-12503

def ejecutar(instrucciones, i):
    if len(instrucciones[i]) == 1:
        if instrucciones[i][0] == 'LEFT':
            return -1
        elif instrucciones[i][0] == 'RIGHT':
            return 1
    else:
        return ejecutar(instrucciones, int(instrucciones[i][2]) - 1)


def main():
    t = int(input())
    while t:
        n = int(input())
        instrucciones = []
        ans = 0
        for i in range(n):
            instrucciones.append(input().split())
            ans += ejecutar(instrucciones, i)

        print(ans)
        t -= 1


if __name__ == "__main__":
    main()
