from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

#
def bygg(ordliste):
    toppnode = Node()
    for (ord, posisjon) in ordliste:
        node = toppnode
        for bokstav in ord:
            if bokstav not in node.barn.keys():
                node.barn[bokstav] = Node()
            node = node.barn[bokstav]
        node.posi.append(posisjon)
    return toppnode



def posisjoner(ord, indeks, node):
    if indeks >= len(ord):
        posi = node.posi
    elif ord[indeks] == "?":
        posi = []
        for barn in node.barn.values():
            posi += posisjoner(ord,indeks+1,barn)
    elif ord[indeks] in node.barn.keys():
        posi = posisjoner(ord,indeks+1,node.barn[ord[indeks]])
    else:
        posi = []
    return posi



def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
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