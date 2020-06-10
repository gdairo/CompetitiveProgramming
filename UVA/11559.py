
def main():
    while True:
        try:
            n, b, h, w = list(map(int, input().split()))
            ans = False
            aux = b
            for _ in range(h):
                p = int(input())
                a = list(map(int, input().split()))

                costo = n * p
                if costo <= b:
                    for i in a:
                        if n >= i:
                            ans = True
                            if aux > costo:
                                aux = costo
                            break

            print(aux if ans else 'stay home')
        except:
            break


if __name__ == "__main__":
    main()
