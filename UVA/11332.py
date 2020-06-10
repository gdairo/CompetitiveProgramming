def g(n):
    if len(n) == 1:
        return int(n)
    else:
        return g(str(sum(map(int, n))))


def main():
    while True:
        n = input()
        if n == '0':
            break

        print(g(n))


if __name__ == "__main__":
    main()
