from sys import stdin
from itertools import repeat

alist = []
def merge(decks):
    if len(decks) > 1:
        mid = len(decks) // 2
        L = decks[:mid]
        R = decks[mid:]
        merge(L)
        merge(R)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                decks[k] = L[i]
                i += 1
            else:
                decks[k] = R[j]
                j += 1
            k +=1

        while i < len(L):
            decks[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            decks[k] = R[j]
            j += 1
            k += 1
    if len(decks)==len(alist):
        ret = ""
        for i in decks:
            ret = ret+i[1]
        return ret


def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        decks.append(list(zip(map(int, csv.split(',')), repeat(index))))
    for i in decks:
        for j in i:
            alist.append(j)
        decks = alist
    print(merge(decks))


if __name__ == "__main__":
    main()