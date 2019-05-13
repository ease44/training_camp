"""
跳台阶
"""


def test(n):
    """
    两种跳法，一次跳一级和一次跳两级
    :param n: 台阶数
    :return:
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b


def test2(n):
    """
    三种跳法，一次跳一级、一次跳两级和一次跳三级
    :param n: 台阶数
    :return:
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a, b, c = 1, 2, 4
        for _ in range(3, n):
            a, b, c = b, c, a + b + c
        return c


def test3(n):
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2 级，……，也可以跳上n 级，
    此时该青蛙跳上一个n级的台阶总共有多少种跳法？
    :param n: 台阶数
    :return:
    """
    if n == 1:
        return 1
    else:
        s = 1
        for _ in range(1, n):
            s *= 2
        return s


if __name__ == '__main__':
    n = 4
    print(test(n))
    print(test2(n))
    print(test3(n))
