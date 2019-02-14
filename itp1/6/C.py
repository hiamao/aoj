def main():
    n = int(input())
    ans = [[0] * 10 for _ in range(15)]
    for i in range(3, 14, 4):
        ans[i] = '#' * 20
    for _ in range(n):
        b, f, r, v = map(int, input().split())
        ans[(b - 1) * 4 + f - 1][r - 1] += v
    for col in ans:
        if col.count('#') > 0:
            print(col)
        else:
            print(' ' + ' '.join(map(str, col)))


main()
