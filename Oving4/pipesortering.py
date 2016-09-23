#!/usr/bin/python3

from sys import stdin


def sort_list(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


def find(A, lower, upper):
    if lower in A and upper in A:
        return [lower,upper]
    if lower in A and upper not in A:
        return [lower,findClosest(A,upper,"up")]
    if upper in A and lower not in A:
        return [findClosest(A,lower,"low"),upper]
    if upper not in A and lower not in A:
        return [findClosest(A,lower,"low"),findClosest(A,upper,"up")]


def findClosest(A,x,arg):
    #finding interval
    if arg =="up":
        for i in range(0,len(A)-1):
            if x < A[i]:
                return A[i]
        return A[len(A)-1]
    if arg =="low":
        for j in range(1,len(A)-1):
            if x> A[j]:
                return A[j]
        return A[0]


input_list = []
for x in stdin.readline().split():
    input_list.append(int(x))
sorted_list = sort_list(input_list)
for line in stdin:
    word = line.split()
    minimum = int(word[0])
    maximum = int(word[1])
    result = find(sorted_list, minimum, maximum)
    print(str(result[0]) + " " + str(result[1]))
