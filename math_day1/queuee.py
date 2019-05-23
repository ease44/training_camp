#!/usr/bin/env pypy3


def test(n, m):
    b = [0] * 1001
    b[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            b[j] = b[j] * j + b[j - 1]
        b[0] = 0
    print(b[m] % (10 ** 9 + 7))


def test2(n, m):
    """第一类斯特林数"""
    su = [[0] * (n+1) for _ in range(n+1)]
    su[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            su[i][j] = su[i - 1][j - 1] + su[i - 1][j] * (i - 1)
    print(su[n][m] % (10 ** 9 + 7))


if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    test2(n, m)
