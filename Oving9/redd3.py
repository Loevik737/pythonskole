#!/usr/bin/python3
from sys import stdin
class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
        self.place= 0
function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatoskInt = int(stdin.readline())
ratatosk_node = nodes[ratatoskInt]
ratatosk_node.ratatosk = True
ratatosk_node.place = ratatoskInt
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])
if function == 'dfs' or function == 'bfs' or function == 'velg':
    def findRatatosk(rn, depth):
        for i in nodes[:ratatosk_node.place]:
            print(i)
    print(findRatatosk(ratatosk_node,0))

