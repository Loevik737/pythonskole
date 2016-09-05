from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    tre = []
    for i in ordliste:
        for j in range(0,len(i[0])-1):
            node = Node()
            node2 = Node()
            node2.barn[i[0][j+1]] = {}
            node.barn[i[0][j]] = node2

            if len(i[0][j+1]) == len(i)-1:
                node.posi.append(i[1])
            tre.append(node)


    for i in tre:
        print(i.barn,i.posi)


def posisjoner(ord, indeks, node):
    print("fd")


def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        print(ordliste)
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()