from sys import stdin

A = []
for tall in stdin:
    A.append(int(tall))


def sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            print("swap",j)
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


sort(A)
print(A)
