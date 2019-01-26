import math


def main():
    while True:
        a, op, b = input().split()
        if op == '?':
            break
        print(math.floor(eval(a + op + b)))


main()
