#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars

def sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


def flexradix(A):
    i = 0
    if len(A) <= 1:
        return A
    botter = [[] for x in range(len(chars))]
    for word in A:
        botter[ord(word[i]) - ord('a')].append(word)
    A = []
    for i in botter:
        if i != []:
            A.append(sort(i))
    return A



d = int(stdin.readline())
strings = []
for line in stdin:
    strings.append(line.rstrip())
A = flexradix(strings)
for string in A:
    for a in string:
        print(a)

