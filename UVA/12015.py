def main():
    t = int(input())
    v = {}

    for i in range(t):
        aux = 0
        for j in range(10):
            n = input().split()
            n[1] = int(n[1])
            v[n[0]] = n[1]
            if n[1] > aux:
                aux = n[1]

        print(f'Case #{i + 1}:')
        for ans, valor in v.items():
            if valor == aux:
                print(ans)


if __name__ == "__main__":
    main()
