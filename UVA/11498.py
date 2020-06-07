def residence(px: int, py: int, x: int, y: int) -> str:
    if x == px or y == py:
        return 'divisa'
    elif x < px and y > py:
        return 'NO'
    elif x > px and y > py:
        return 'NE'
    elif x > px and y < py:
        return 'SE'
    elif x < px and y < py:
        return 'SO'


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        px, py = (map(int, input().split()))

        for _ in range(n):
            x, y = (map(int, input().split()))
            print(residence(px, py, x, y))


if __name__ == "__main__":
    main()
