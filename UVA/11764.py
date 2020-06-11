def main():
    t = int(input())
    for caso in range(t):
        n = int(input())
        paredes = list(map(int, input().split()))

        temp = paredes[0]
        saltoA = 0
        saltoB = 0

        for pared in paredes[1:]:
            if temp > pared:
                saltoA = saltoA + 1
            elif temp < pared:
                saltoB = saltoB + 1
            temp = pared

        print(f'Case {caso + 1}: {saltoB} {saltoA}')


if __name__ == "__main__":
    main()
