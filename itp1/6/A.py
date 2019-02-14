def main():
    n = int(input())
    a = list(input().split())
    ans = []
    for _ in range(n):
        ans.append(a.pop(-1))
    print(' '.join(ans))


main()
