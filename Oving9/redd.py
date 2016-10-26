#!/usr/bin/python3

from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0


def dfs(root):
    # SKRIV DIN KODE HER


def bfs(root):
    # SKRIV DIN KODE HER

function = stdin.readline().strip() # function = velg/dfs/bfs
number_of_nodes = int(stdin.readline()) #antall noder i treet
nodes = []  #en tom liste for nodene
for i in range(number_of_nodes):    #for antall noder sett in en node i nodes
    nodes.append(Node())    #sett in en "tom"node  i nodes
start_node = nodes[int(stdin.readline())]   #sett startnoden til den neste linjen som i eksempelet blir 0,altså den første noden i nodes
ratatosk_node = nodes[int(stdin.readline())]    #noden han befinner seg i er noden på neste linje, i eksempelet er dette node 7
ratatosk_node.ratatosk = True   #dette er altså ratatosks node og vi setter den til true
for line in stdin:  #for resten av linjene
    number = line.split()
    print(number)
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    # SKRIV DIN KODE HER
    print(dfs(start_node)) #velger bare midlertidig dybde først søk