"""
跳马，象棋中的马从某个棋盘的左下角，如何走到右上角，有多少种走法
"""
from collections import namedtuple


res = []
direction = ((1, -2), (2, -1), (2, 1), (1, 2))


def test(pos, step):
    """
    没写完
    :param pos:
    :param step:
    :return:
    """

if __name__ == '__main__':
    start = namedtuple('postion', ['x', 'y'])
    start.x = 0
    start.y = 0
    print(test(start, 0))
