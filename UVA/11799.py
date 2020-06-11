def main():
    t = int(input())
    for i in range(t):
        c = list(map(int, input().split()))
        print(f'Case {i + 1}: {max(c[1:])}')


if __name__ == "__main__":
    main()
