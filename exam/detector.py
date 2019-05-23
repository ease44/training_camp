#!/usr/bin/env pypy3


def test(d, n, tmp):
    count = 0
    nr = ''
    if m - n == 0:
        for j in range(1, len(tmp) + 1):
            r = [0] * (len(d) + 1)
            for i in tmp:
                name, sentence = i.split(': ')
                if 'I am guilty.' in i:
                    r[d[name]] = (j == d[name])
                elif 'I am not guilty.' in i:
                    r[d[name]] = (j != d[name])
                elif ' is guilty.' in sentence:
                    name2 = sentence.replace(' is guilty.', '')
                    r[d[name]] = (j == d[name2])
                elif ' is not guilty.' in sentence:
                    name2 = sentence.replace(' is not guilty.', '')
                    r[d[name]] = (j != d[name2])

            if sum(r) == 1:
                for k, v in d.items():
                    if v == j:
                        return k
            elif sum(r) > 1:
                return 'Cannot Determine'
            else:
                pass

    for j in range(1, len(tmp) + 1):
        r = [0] * (len(d) + 1)
        for i in tmp:
            name, sentence = i.split(': ')
            if 'I am guilty.' in i:
                r[d[name]] = (j == d[name])
            elif 'I am not guilty.' in i:
                r[d[name]] = (j != d[name])
            elif ' is guilty.' in sentence:
                name2 = sentence.replace(' is guilty.', '')
                r[d[name]] = (j == d[name2])
            elif ' is not guilty.' in sentence:
                name2 = sentence.replace(' is not guilty.', '')
                r[d[name]] = (j != d[name2])

        if sum(r) == 1:
            for k, v in d.items():
                if v == j:
                    return k
        elif sum(r) > 1:
            return 'Cannot Determine'
        else:
            pass

        if sum(r) != (m - n):
            continue
        else:
            count += 1
            for k, v in d.items():
                if v == j:
                    nr = k
                    break

    if count > 1:
        return 'Cannot Determine'
    elif count == 0:
        return 'Impossible'
    elif count == 1:
        return nr


if __name__ == '__main__':
    m, n, p = map(int, input().split(' '))
    d = {}
    for i in range(1, m + 1):
        t = input()
        d[t] = i
    tmp = []
    for _ in range(p):
        t = input()
        if 'I am guilty.' in t or 'I am not guilty.' in t or \
                ' is guilty.' in t or ' is not guilty.' in t:
            tmp.append(t)

    print(test(d, n, tmp))
