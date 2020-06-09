def main():
    while True:
        duracion, inicial, monto, depresiacion = input().split()

        duracion = int(duracion)
        if duracion < 0:
            break

        inicial = float(inicial)
        monto = float(monto)
        depresiacion = int(depresiacion)

        meses = [0] * 101
        for i in range(depresiacion):
            mes, depre = list(map(float, input().split()))
            for j in range(int(mes), 101):
                meses[j] = depre

        valor_mes = monto / duracion

        ans = 0
        aux = (monto + inicial) * (1 - meses[ans])
        while aux < monto:
            ans += 1
            monto = monto - valor_mes
            aux = aux * (1 - meses[ans])

        print(ans, 'month' if ans == 1 else 'months')


if __name__ == "__main__":
    main()
