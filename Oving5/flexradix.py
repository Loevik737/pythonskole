#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars


def flexradix(A, i):
    if len(A) <= 1:
        return A
    ferdig = []
    botter = [[] for x in range(len(chars))]
    for word in A:
        if i >= len(word):
            ferdig.append(word)
        else:
            botter[ord(word[i]) - ord('a')].append(word)
    botter = [flexradix(b, i + 1) for b in botter]
    return ferdig + [b for blist in botter for b in blist]


d = int(stdin.readline())
strings = []
for line in stdin:
    strings.append(line.rstrip())
A = flexradix(strings, 0)
for string in A:
    print(string)

