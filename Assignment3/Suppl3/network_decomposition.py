import re
import math


class node:

    def __init__(self, name):
        self.name = name
        self.degree = 0

    def __eq__(self, other):
        return self.name == other.name

    def add(self):
        self.degree += 1

    def remove(self):
        if self.degree < 0:
            self.degree -= 1

def c(i):
    if(i == 1):
        return math.inf
    else:
        return (i+1)/(i-1)

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
    n1.add()
    n2.add()
    net[n1.name] = n1
    net[n2.name] = n2
    links.append([temp[0], temp[1], 0])

while links.__len__() != 0:
    min_val = math.inf
    min_index = -1
    for i in range(0,links.__len__()):
        l = links[i]
        c1 = net[l[0]].degree
        c2 = net[l[1]].degree
        s = min(c1, c2)
        z = c(s)
        l = [l[0], l[1], z]
        if z < min_val:
            min_val = z
            min_index = i
        links[i] = l

    print(links[min_index])
    l = links[min_index]
    n1 = net[l[0]]
    n2 = net[l[1]]
    n1.remove()
    n2.remove()
    net[n1.name] = n1
    net[n2.name] = n2
    del links[min_index]

