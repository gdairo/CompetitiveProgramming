def main():
    case = 1
    while True:
        s = input()
        if s == '*':
            break

        print(f'Case {case}:', end=' ')
        print('Hajj-e-Akbar' if s == 'Hajj' else 'Hajj-e-Asghar')
        case += 1


if __name__ == "__main__":
    main()
