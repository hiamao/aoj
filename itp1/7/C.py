def main():
    r, c = map(int, input().split())
    cs = [0] * (c + 1)
    t = []
    for _ in range(r):
        s = list(map(int, input().split()))
        s.append(sum(s))
        t.append(s)
        for i in range(c):
            cs[i] += s[i]
    cs[-1] = sum(cs)
    t.append(cs)
    for a in t:
        print(' '.join(map(str, a)))


main()
