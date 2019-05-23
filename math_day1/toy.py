#!/usr/bin/env python3
"""
搭积木
小球相同，格子不同
"""


def combination(n, m):
    r = 1
    for i in range(1, m + 1):
        t = (r * (n - i + 1) // i) % (10 ** 9 + 7)
        t *= r
    return r


if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    print(combination(m * m + n - 1, n) % (10 ** 9 + 7))
