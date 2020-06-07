inicio = True
while True:
    try:
        s = input()
        for c in s:
            if c == '"':
                if inicio:
                    print("``", end='')
                else:
                    print("''", end='')
                inicio = not inicio
            else:
                print(c, end='')
        print()
    except:
        break
