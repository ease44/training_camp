#!/usr/bin/env pypy3


def test(l):
    s = set()
    for i, j in l:
        if i == 1:
            if j in s:
                print('Failed')
            else:
                s.add(j)
                print('Succeeded')
        else:
            if j in s:
                s.remove(j)
                print('Succeeded')
            else:
                print('Failed')


if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().strip().split(' '))))
    test(l)
