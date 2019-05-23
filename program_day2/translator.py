#!/usr/bin/env python3
import re


def test(x, y, q):
    re_d = {
        'A': [
            'Today\sis\s(.*).',
            'I\swant\sto\s(.*).',
            '(\d+)\s(.*),\splease.',
        ],
        'B': [
            "Var\sday=(.*);",
            'Var\splan="(.*)";',
            'Var\sitem="(.*)";\sVar\snum=(\d+);',
        ],
        'C': [
            ".*I\sjust\sfound\sthat\stoday\sis\s(.*)!",
            ".*Let\sus\sgo\sto\s(.*).",
            "I\swant\sone\s([\w\s]*)[,.]+(,\sand\sone\smore)*",
        ]
    }

    for i, e in enumerate(re_d[x]):
        r = re.match(e, q)
        if r:
            key = r.groups()
            trans(i, key, x, y, q)
            break


def trans(index, key, x, y, q):
    tmp_d = {
        'A': [
            'Today is {}.',
            'I want to {}.',
            "{n} {xxx}, please.",
        ],
        'B': [
            "Var day={};",
            'Var plan="{}";',
            'Var item="{xxx}"; Var num={n};',
        ],
        'C': [
            "Oh, my god. that's incredible. You know what? I just found that today is {}!",
            "My god! What should I do today? Let me see. Well, I have an excellent idea! Let us go to {}.",
            "I want one {xxx}{n}.",
        ]
    }
    if index == 0:
        t = {
            'A': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'B': ['1', '2', '3', '4', '5', '6', '7'],
            'C': ['MMMonday', 'TTTuesday', 'WWWednesday', 'TTThursday', 'FFFriday', 'SSSaturday', 'SSSunday'],
        }
        s = []
        for j in key[0].split('/'):
            i = t[x].index(j)
            s.append(t[y][i])
        print(tmp_d[y][index].format('/'.join(s)))
    elif index == 1:
        print(tmp_d[y][index].format(key[0]))
    else:
        if x == 'A':
            print(tmp_d[y][index].format(n=key[0], xxx=key[1]))
        elif x == 'B':
            n = ', and one more' * (int(key[1])-1)
            print(tmp_d[y][index].format(xxx=key[0], n=n))
        else:
            n = q.count(', and one more') + 1
            print(tmp_d[y][index].format(xxx=key[0], n=n))


if __name__ == '__main__':
    n = int(input())
    t = []
    for _ in range(n):
        l = input().split(' ')
        t.append((l[0], l[1], ' '.join(l[2:])))
    for x, y, q in t:
        if x == y:
            print(q)
        else:
            test(x, y, q)
