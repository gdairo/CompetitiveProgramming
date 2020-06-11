def ans(aux):
    a = False
    d = False
    temp = aux[0]
    for n in aux[1:]:
        if temp > n:
            a = True
        else:
            d = True
        temp = n
    return a and d


def main():
    n = int(input())
    print('Lumberjacks:')
    for _ in range(n):
        aux = list(map(int, input().split()))
        print('Unordered' if ans(aux) else 'Ordered')


if __name__ == "__main__":
    main()
