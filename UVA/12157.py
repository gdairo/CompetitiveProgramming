def main():
    t = int(input())
    for caso in range(t):
        n = int(input())
        llamadas = list(map(int, input().split()))
        mile = 0
        juice = 0
        for segundos in llamadas:
            mile += (segundos // 30) * 10 + 10
            juice += (segundos // 60) * 15 + 15

        if mile == juice:
            print(f'Case {caso + 1}: Mile Juice {mile}')
        elif mile < juice:
            print(f'Case {caso + 1}: Mile {mile}')
        else:
            print(f'Case {caso + 1}: Juice {juice}')


if __name__ == "__main__":
    main()
