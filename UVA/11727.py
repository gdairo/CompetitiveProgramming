def main():
    t = int(input())

    for i in range(t):
        n = list(map(int, input().split()))
        print(f'Case {i + 1}: {n[1]}')


if __name__ == "__main__":
    main()
