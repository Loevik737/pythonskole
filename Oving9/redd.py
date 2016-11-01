#!/usr/bin/python3

from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0



def dfs(root):
    stak = [root]
    while stak:
        node = stak[-1]
        if node.ratatosk:
            return len(stak) -1
        if len(node.child) == node.next_child:
            stak.pop()
        else:
            stak.append(node.child[node.next_child])
            node.next_child +=1




def bfs(root):
    # SKRIV DIN KODE HER
    queue = [(root, 0)]
    while len(queue) > 0:
        node, depth = queue.pop(0)
        if node.ratatosk:
            return depth
        for child in node.child:
            queue.append((child, depth + 1))


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

#for node in nodes:
 #   print(node.ratatosk)
  #  for node2 in node.child:
   #     if node2 != None:
    #        print("child:", node2.ratatosk)
visitedNodes = []
if function == 'dfs':
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    # SKRIV DIN KODE HER
    print(dfs(start_node))