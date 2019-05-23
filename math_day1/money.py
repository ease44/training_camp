#!/usr/bin/env pypy3


def test(total, index):
    global count
    if index == len(l):
        return None
    if total == 0:
        count += 1
        return None

    for i in range(index, len(l)):
        t = total - l[i]
        if t < 0:
            break
        else:
            test(t, i + 1)


def test2(total, l):
    d = {}
    for i in l:
        r = {}
        if not d:
            for j in (0, i):
                d[j] = 1
        else:
            # for j in (0, i):
            #     for k in list(d.keys()):
            #         d[k + j] = d.get(k + j, 0) + d[k]
            r.update(d)
            for k in d.keys():
                if d.get(k + i, None) is None:
                    r[k + i] = d[k]
                else:
                    r[k + i] += d[k]
            d.update(r)
            r = {}
    return d.get(total, 0)


if __name__ == '__main__':
    n, total = map(int, input().strip().split(' '))
    l = sorted(map(int, input().strip().split(' ')))
    count = 0
    # test(total, 0)
    # print(count)
    print(test2(total, l))
