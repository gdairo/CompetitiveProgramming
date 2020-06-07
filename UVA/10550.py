def main():
    while True:
        c, p, s, t = (map(int, input().split()))

        if not (c or p or s or t):
            break

        ans = 1080
        ans += ((c - p + 40) % 40 + (s - p + 40) % 40 + (s - t + 40) % 40) * 9
        print(ans)


if __name__ == "__main__":
    main()
