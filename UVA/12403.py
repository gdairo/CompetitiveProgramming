def main():
    t = int(input())
    k = []
    for _ in range(t):
        s = input().split()
        if len(s) > 1:
            k.append(int(s.pop()))
        else:
            print(sum(k))


if __name__ == "__main__":
    main()
