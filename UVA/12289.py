def num(s) -> int:
    if len(s) > 4:
        return 3
    else:
        uno = 0
        for i in range(len(s)):
            if s[i] == "one"[i]:
                uno += 1

        if uno < 2:
            return 2

    return 1


def main():
    n = int(input())
    for _ in range(n):
        s = input()
        print(num(s))


if __name__ == "__main__":
    main()
