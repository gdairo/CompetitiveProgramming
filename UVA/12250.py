def lenguaje(s) -> str:
    if s == 'HELLO':
        return 'ENGLISH'
    elif s == 'HOLA':
        return 'SPANISH'
    elif s == 'HALLO':
        return 'GERMAN'
    elif s == 'BONJOUR':
        return 'FRENCH'
    elif s == 'CIAO':
        return 'ITALIAN'
    elif s == 'ZDRAVSTVUJTE':
        return 'RUSSIAN'
    else:
        return 'UNKNOWN'


def main():
    case = 1
    while True:
        s = input()
        if s == '#':
            break

        print(f'Case {case}: {lenguaje(s)}')
        case += 1


if __name__ == "__main__":
    main()
