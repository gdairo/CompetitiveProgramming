def main():
    t = int(input())
    while t:
        n, m = (map(int, input().split()))
        print((n // 3) * (m // 3))
        t -= 1


if __name__ == '__main__':
    main()
