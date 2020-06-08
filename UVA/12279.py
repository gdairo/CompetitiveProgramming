
def main():
    case = 1
    while True:
        n = int(input())
        if not bool(n):
            break

        m = list(map(int, input().split()))
        ans = m.count(0)
        print(f'Case {case}: {n - ans * 2}')


if __name__ == "__main__":
    main()
