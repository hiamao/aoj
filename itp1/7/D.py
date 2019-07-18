def main():
    n, m, l = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(m)]
    ans = [[0] * l for _ in range(n)]
    for i in range(n):
        for k in range(l):
            v = 0
            for j in range(m):
                v += A[i][j] * B[j][k]
            ans[i][k] = str(v)
    for a in ans:
        print(' '.join(a))


main()
