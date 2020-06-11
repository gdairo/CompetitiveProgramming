def ans(bancos) -> bool:
    for i in bancos:
        if i < 0:
            return False
    return True


def main():
    while True:
        b, n = list(map(int, input().split()))

        if not (b and n):
            break

        bancos = list(map(int, input().split()))

        for i in range(n):
            d, c, v = list(map(int, input().split()))
            bancos[d - 1] -= v
            bancos[c - 1] += v

        print('S' if ans(bancos) else 'N')


if __name__ == "__main__":
    main()
