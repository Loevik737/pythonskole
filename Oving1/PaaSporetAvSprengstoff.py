from sys import stdin

class Kubbe:
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    storst = kubbe.vekt
    while kubbe.neste != None:
        if kubbe.neste.vekt > storst:
            storst = kubbe.neste.vekt
        kubbe = kubbe.neste
    return storst


# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print(spor(forste))