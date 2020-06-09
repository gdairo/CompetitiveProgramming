def main():
    n = int(input())
    for _ in range(n):
        f = int(input())
        ans = 0
        for i in range(f):
            famers = list(map(int, input().split()))
            ans = ans + famers[0] * famers[2]

        print(ans)


if __name__ == "__main__":
    main()
