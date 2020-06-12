# Dairo García
# https://vjudge.net/problem/UVA-12468

def main():
    while True:
        a, b = list(map(int, input().split()))
        if a < 0 and b < 0:
            break

        print(min((100 - max(a, b) + min(a, b)), abs(b - a)))


if __name__ == "__main__":
    main()
