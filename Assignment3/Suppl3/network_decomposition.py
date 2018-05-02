import re
import math


class node:

    def __init__(self, name):
        self.name = name
        self.links = []

    def __eq__(self, other):
        return self.name == other.name

    def add(self, name):
        self.links.append(name)

    def remove(self, name):
        self.links.remove(name)

    def degree(self):
        return self.links.__len__()
# i = number of triangles
# j = min degree of both nodes
def c(i,j):
    if(j == 1):
        return math.inf
    else:
        return (i+1)/(j-1)

def numTri(A, B, net):
    n1 = net[A].links
    n2 = net[B].links
    return list(set(n1) & set(n2)).__len__()

file = open("GoT.txt", "r")
net = {}
links = []
for line in file:
    line = line.rstrip()
    temp = re.split(" ", line)
    if temp[0] not in net:
        n1 = node(temp[0])
    else:
        n1 = net[temp[0]]
    if temp[1] not in net:
        n2 = node(temp[1])
    else:
        n2 = net[temp[1]]
    n1.add(temp[1])
    n2.add(temp[0])
    net[n1.name] = n1
    net[n2.name] = n2
    links.append([temp[0], temp[1], 0])

while links.__len__() != 0:
    min_val = math.inf
    min_index = -1
    for i in range(0,links.__len__()):
        l = links[i]
        c1 = net[l[0]].degree()
        c2 = net[l[1]].degree()
        s = min(c1, c2)
        z = c(numTri(l[0], l[1], net), s)
        ltemp = [l[0], l[1], z]
        if z < min_val:
            min_val = z
            min_index = i
        links[i] = ltemp

    print(links[min_index])
    l = links[min_index]
    n1 = net[l[0]]
    n2 = net[l[1]]
    n1.remove(n2.name)
    n2.remove(n1.name)
    net[n1.name] = n1
    net[n2.name] = n2
    del links[min_index]

