#!/usr/bin/python3

from sys import stdin

#this version is not 100% tested
def sort_list(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x) // 2
    y = sort_list(x[:mid])
    z = sort_list(x[mid:])
    i, j = 0, 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


def find(A, lower):
    mid = len(A)//2

    if lower in A[:mid]:
        find(A[:mid])
    elif lower == A[mid]:
        return A[mid]
    elif lower == A[mid+1]:
        return A[mid+1]
    else:
        find(A[mid:])



input_list = []
for x in stdin.readline().split():
    input_list.append(int(x))
sorted_list = sort_list(input_list)
for line in stdin:
    word = line.split()
    minimum = int(word[0])
    maximum = int(word[1])
    result = find(sorted_list, minimum)
    print(str(result[0]) + " " + str(result[1]))
