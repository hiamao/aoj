def main():
    n = int(input())
    ans = ['']
    for i in range(1, n + 1):
        x = i
        if x % 3 == 0:
            if i not in ans:
                ans.append(i)
        else:
            while x > 0:
                if x % 10 == 3:
                    if i not in ans:
                        ans.append(i)
                x //= 10
    print(' '.join(map(str, ans)))


main()
