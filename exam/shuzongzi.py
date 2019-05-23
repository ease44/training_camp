#!/usr/bin/env pypy3


def test(t, l, r, d):
    print(len(set(t[l - 1:r])))


if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split(' ')))
    q = int(input())
    s = []
    for _ in range(q):
        l, r = map(int, input().split(' '))
        s.append((l, r))
    d = {}
    for l, r in s:
        test(t, l, r, d)
