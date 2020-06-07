def main():
    t = int(input())
    for _ in range(t):
        n = input()
        x = list(map(int, input().split()))
        print((max(x) - min(x)) * 2)


if __name__ == '__main__':
    main()
