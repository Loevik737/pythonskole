from sys import stdin
from time import clock


def merge4(x):
    result = []
    if len(x) < 2:
        print(x)
        return x
    mid = len(x) // 2
    y = merge4(x[:mid])
    z = merge4(x[mid:])
    i,j = 0,0
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


def merge3(decks):
    if len(decks) > 1:
        mid = len(decks) // 2
        L = decks[:mid]
        R = decks[mid:]
        merge3(L)
        merge3(R)
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
            k += 1

        while i < len(L):
            decks[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            decks[k] = R[j]
            j += 1
            k += 1


def main():
    ints = []
    for line in stdin:
        ints.append(int(line))
    a = clock()
    merge4(ints)
    #merge3(ints)
    b = clock()
    print("used: "+str(b-a) +"sec")
if __name__ == "__main__":
    main()
