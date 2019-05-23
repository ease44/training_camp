#!/usr/bin/env pypy3
import heapq


def test(n, l):
    """
    超时了
    :param n:
    :param l:
    :return:
    """
    for i in range((2 * n - 1) // 2 + 1):
        le = i * 2 + 1
        if le == 1:
            print(l[i])
            continue
        else:
            for j in range(1, le):
                key = l[j]
                k = j - 1
                while k >= 0 and l[k] > key:
                    l[k + 1] = l[k]
                    k -= 1
                l[k + 1] = key
            print(l[i])


def test2(n, l):
    """比test多过了两个测试用例，还是超时"""
    for i in range((2 * n - 1) // 2 + 1):
        le = i * 2 + 1
        if le == 1:
            print(l[i])
            continue
        else:
            l[:le] = sorted(l[:le])  # 试下
            print(l[i])


def test3(n, l):
    h = []
    index = [2 * i - 1 for i in range(1, n + 1)]
    c = 0
    for i, e in enumerate(l):
        heapq.heappush(h, e)
        if i == index[c] - 1:
            print(heapq.nlargest((index[c] // 2 + 1), h)[-1])
            c += 1


def test4(n, l):
    count = 1
    for j in range(1, len(l)+1):
        if j == 2*count-1:
            print(l[count-1])
            count += 1
            if j == len(l):
                return None
        i = binary_search(j, l[j], l)
        key = l[j]

        l.pop(j)
        l.insert(i, key)
        # 和上面两行一个意思
        # key = l[j]
        # while j > i:
        #     l[j] = l[j-1]
        #     j -= 1
        # l[j] = key

        # 插入排序
        # key = l[j]
        # k = j - 1
        # while k >= 0 and l[k] > key:
        #     l[k + 1] = l[k]
        #     k -= 1
        # l[k + 1] = key


def binary_search(high, t, l):
    low = 0
    while low < high:
        mid = (low + high) // 2
        if l[mid] == t:
            return mid
        elif l[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    if l[low] >= t:
        return low
    else:
        return low + 1


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split(' ')))
    # test(n, l)
    test4(n, l)
