def main():
    n = int(input())

    while n > 0:
        str = input()
        ans = []

        flag = True

        for c in str:
            if c == '(' or c == '[':
                ans.append(c)
            else:
                if len(ans) == 0:
                    flag = False
                    continue
                ans.pop()

        if len(ans) == 0 and flag:
            print("Yes")
        else:
            print("No")

        n -= 1


if __name__ == '__main__':
    main()