#!/usr/bin/python3
from sys import stdin
class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])
if function == 'velg' or function == 'bfs':
    queue = [(start_node, 0)]
    while queue:
        node, depth = queue.pop(0)
        if node.ratatosk:
            print(depth)
            break
        for child in node.child:
            queue.append((child, depth + 1))
else:
    stak = [start_node]
    while stak:
        node = stak[-1]
        if node.ratatosk:
            print(len(stak) - 1)
            break
        if len(node.child) == node.next_child:
            stak.pop()
        else:
            stak.append(node.child[node.next_child])
            node.next_child += 1
