from sys import stdin
import time
start = time.clock()
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

forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste
end = time.clock()
print(spor(forste), "time(s): "+str(end-start))