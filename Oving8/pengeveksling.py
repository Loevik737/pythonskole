from sys import stdin

Inf = float('inf')

def minCoinsGreedy(coins, value):
    i = 0 #mynt nr i blir iterert
    num = 0#antall mynter
    while value > 0:#så lenge verdien vi vil ha er større en 0
        if coins[i] <= value:#om mynten vi velger har samme verdi som value vil vi kunne ittetere bare en gang og returnere 1, om ikke må vi fortsette til value blir 0
            value = value - coins[i]#trekk verdien til mynten fra value
            num +=1#nå har vi brukt en mynt mer
        else:
            i +=1#om vi ikke kan bruke mynt nr i lenger går vi til neste
    return num #returner antall mynter brukt


def minCoinsDynamic(coins, value):
    results = [Inf] * (value + 1)#lag et uendelig element for hvert tall i value (3 = [inf,inf,inf])
    usefulCoins = [] #myntel som er mindre eller lik verdien vi skal ha
    for c in coins:#for alle myntene vi kan bruke
        if c <= value:#om mynten er mindre eller lik verdien
            results[c] = 1 #skriv 1 til indeksen til mynten i results
            usefulCoins.append(c)#legg den til mynter vi kan bruke
    for curVal in range(1, value + 1):
        if results[curVal] != Inf:
            continue
        best = Inf
        for c in usefulCoins:
            if c <= curVal:
                current = 1 + results[curVal - c]
                if current < best:
                    best = current
        results[curVal] = best
    return results[value]


def canUseGreedy(coins):

    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER

    return False



coins = []#tomm array for coins
for c in stdin.readline().split():
    coins.append(int(c))#legger til myntene i arrayen
coins.sort()#sorterer myntene
coins.reverse()#den største mynten er først
method = stdin.readline().strip()#method får verdien til linje 2 i input(input2
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):#om vi har valgt grådig algoritme eller canUseGreedy returnerer true
    for line in stdin:
        print(minCoinsGreedy(coins, int(line)))#skriver ut det minimale antallet mynter som kan brukes for å oppnå det beløpet
else:#hvis ikke bruk DP
    for line in stdin:
        print(minCoinsDynamic(coins, int(line)))#skriver ut det minimale antallet mynter som kan brukes for å oppnå det beløpet