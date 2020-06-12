# Dairo García
# https://vjudge.net/problem/UVA-12554

def main():
    cancion = [
        'Happy', 'birthday', 'to', 'you', 'Happy',
        'birthday', 'to', 'you', 'Happy', 'birthday',
        'to', 'Rujia', 'Happy', 'birthday', 'to', 'you'
    ]

    n = int(input())
    gente = []
    for i in range(n):
        gente.append(input())

    veces = 1
    if n > 16:
        veces = (n // 16) + 1

    x = 0
    for i in range(veces):
        for letra in cancion:
            print(f'{gente[x % n]}: {letra}')
            x += 1


if __name__ == "__main__":
    main()
