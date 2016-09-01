from sys import stdin


forste = None
siste = None


class Kubbe:
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None


def spor(kubbe):
    if kubbe != None:
        storst = kubbe.vekt
        while kubbe.neste is not None:
            if kubbe.neste.vekt > storst:
                storst = kubbe.neste.vekt
            kubbe = kubbe.neste
        return storst
    return None


for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste is None:
        forste = siste
    else:
        forrige_siste.neste = siste


print(spor(forste))

