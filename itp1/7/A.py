def main():
    ans = []
    while True:
        m, f, r = map(int, input().split())
        if m == -1 and f == -1 and r == -1:
            break
        s = 0
        if m >= 0:
            s += m
        if f >= 0:
            s += f
        if m == -1 or f == -1:
            ans.append('F')
        elif s >= 80:
            ans.append('A')
        elif 80 > s >= 65:
            ans.append('B')
        elif 65 > s >= 50 or r >= 50:
            ans.append('C')
        elif 50 > s >= 30:
            ans.append('D')
        elif 30 > s:
            ans.append('F')
    for a in ans:
        print(a)


main()
