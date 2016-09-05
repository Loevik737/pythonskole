from sys import stdin

ord = stdin.readline().split()
ordliste= []
resultat = {}
sokeord = []
pos = 0

for o in ord:
    ordliste.append((o, pos))
    pos += len(o) + 1

for sord in stdin:
    sokeord.append( sord.strip())

for j in sokeord:
    for k in range(0,len(ordliste)-1):
        if j in ordliste[k]:
            if j in resultat.keys():
                resultat[j].append(ordliste[k][1])
            else:
                resultat[j] = []
                resultat[j].append(ordliste[k][1])

for z in sokeord:
    if "?" in z:
        print("true")


print(resultat)