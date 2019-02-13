def main():
    cards = {
        'S': [0] * 13,
        'H': [0] * 13,
        'C': [0] * 13,
        'D': [0] * 13
    }

    n = int(input())
    for _ in range(n):
        a, b = input().split()
        cards[a][int(b) - 1] = 1

    for a, b in cards.items():
        for i in range(13):
            if b[i] == 0:
                print(a, i + 1)


main()
