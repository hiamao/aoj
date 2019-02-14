def main():
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        for _ in range(H):
            col = ''
            for _ in range(W):
                col += '#'
            print(col)
        print()


main()
