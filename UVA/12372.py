def ans(s) -> str:
    s.sort()
    if s.pop() > 20:
        return 'bad'

    return 'good'


def main():
    t = int(input())

    for case in range(t):
        s = list(map(int, input().split()))
        print(f'Case {case + 1}: {ans(s)}')


if __name__ == "__main__":
    main()
