#!/usr/bin/python3

from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0


def dfs(root):
    # SKRIV DIN KODE HER
    print(root.next_child)
    print(len(root.child))
    stack = [root]
    while stack: #så lenge stack ikke er tom
        node = stack[len(stack) - 1]#node blir stackens siste node
        if node.ratatosk:#om dette er noden vi leter etter
            return len(stack) - 1 #returnerer vi lengden på stacken- 1
        if node.next_child == len(node.child): # om nodens neste barn er lengden på nodens barn
            stack.pop() #pop det siste elementet i stacken
        else:
            stack.append(node.child[node.next_child]) # om ikke legg nodens barn sit neste barn til stacken
            node.next_child += 1 # noden si neste barn blir en større


def bfs(root):
    # SKRIV DIN KODE HER
    print("hade")

function = stdin.readline().strip() # function = velg/dfs/bfs
number_of_nodes = int(stdin.readline()) #antall noder i treet
nodes = []  #en tom liste for nodene
for i in range(number_of_nodes):    #for antall noder sett in en node i nodes
    nodes.append(Node())    #sett in en "tom"node  i nodes
start_node = nodes[int(stdin.readline())]   #sett startnoden til den neste linjen som i eksempelet blir 0,altså den første noden i nodes
ratatosk_node = nodes[int(stdin.readline())]    #noden han befinner seg i er noden på neste linje, i eksempelet er dette node 7
ratatosk_node.ratatosk = True   #dette er altså ratatosks node og vi setter den til true
for line in stdin:  #for resten av linjene
    number = line.split()#splitt linjen så hvert tal blir et eget element i number
    print(number)#
    temp_node = nodes[int(number.pop(0))]   #temp_node = noden i posisjonen til det første elementet i number,(7,1,3,0)
    print(temp_node)
    print(number)
    for child_number in number: #for elementene som er igjen i number
        temp_node.child.append(nodes[int(child_number)]) #de elementene som var igjen er indeksen for hvilke noder i nodes som skal bli barna til temp_node

for i in nodes:
    print(i.ratatosk)
if function == 'dfs':
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    # SKRIV DIN KODE HER
    print(dfs(start_node)) #velger bare midlertidig dybde først søk