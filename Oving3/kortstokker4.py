from sys import stdin
from itertools import repeat, chain
from time import clock
a = clock()


def merge(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x) // 2
    y = merge(x[:mid])
    z = merge(x[mid:])
    i,j = 0,0
    while i < len(y) and j < len(z):
            if y[i][0] > z[j][0]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result


def main():
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        decks.append(list(zip(map(int, csv.split(',')), repeat(index))))
    decks = list(chain.from_iterable(decks))
    print(''.join(v for (k, v) in merge(decks)))
    b = clock()
    print(b-a)


if __name__ == "__main__":
    main()
