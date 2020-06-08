def operacion(s) -> str:
    if s in ['1', '4', '78']:
        return '+'
    elif s[-2:] == '35':
        return '-'
    elif s[0] == '9' and s[-1] == '4':
        return '*'
    elif s[:3] == '190':
        return '?'


def main():
    n = int(input())
    for _ in range(n):
        s = input()
        print(operacion(s))


if __name__ == "__main__":
    main()
