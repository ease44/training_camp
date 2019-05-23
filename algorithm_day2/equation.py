#!/usr/bin/env pypy3


class QuickFind(object):
    # count = 0

    def __init__(self, n):
        self.id = []
        self.count = n
        i = 0
        while i < n:
            self.id.append(i)
            i += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        idp = self.find(p)
        if not self.connected(p, q):
            for i in range(len(self.id)):
                if self.id[i] == idp:  # 将 p所在组  的所有节点的id都设为q的当前id
                    self.id[i] = self.id[q]
            self.count -= 1


if __name__ == '__main__':
    res = []
    t = []
    c = int(input())
    x = []
    y = []
    for _ in range(c):
        n, m = map(int, input().split(' '))
        x.append(n)
        y.append(m)
        s = []
        for _ in range(m):
            p, q, e = map(int, input().split(' '))
            s.append((p, q, e))
            s.sort(key=lambda l: l[2] > 0, reverse=True)
        t.append(s)

    for i in range(c):
        a = False
        qf = QuickFind(x[i]+1)
        for p, q, e in t[i]:
            if e == 1:
                qf.union(p, q)
            else:
                if e != qf.connected(p, q):
                    print('No')
                    a = True
                    break
        if not a:
            print('Yes')
