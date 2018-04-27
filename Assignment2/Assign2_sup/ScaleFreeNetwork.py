import random
from AbstractNetwork import AbstractNetwork
from Node import Node
import numpy as np

class ScaleFreeNetwork(AbstractNetwork):
    """Scale-free network implementation of AbstractNetwork"""
          
    def __createNetwork__(self, amount_nodes, amount_links):
        """
        Create a network with an amount of n nodes, add m links per iteration step
        for n nodes:
            for m links:
                link node to other nodes
        """
        random.seed()

        for i in range(0, 3):
            AbstractNetwork.appendNode(self, node=Node(i))

        n0 = AbstractNetwork.getNode(self, 0)
        n1 = AbstractNetwork.getNode(self, 1)
        n2 = AbstractNetwork.getNode(self, 2)
        n0.addLinkTo(n1)
        n1.addLinkTo(n2)
        n2.addLinkTo(n0)
        n0.addLinkTo(n2)
        n1.addLinkTo(n0)
        n2.addLinkTo(n1)

        linked_nodes = [0,0,1,1,2,2]
        limit = amount_links

        for i in range(3, amount_nodes):
            network_size = self.size()
            if amount_links > network_size:
                limit = network_size

            new_node = AbstractNetwork.getNode(self, i)
            for j in range(0, limit):
                ns = random.randint(0, linked_nodes.__len__()-1)
                while new_node.hasLinkTo(linked_nodes[ns]):
                    ns = random.randint(0, linked_nodes.__len__()-1)
                n = AbstractNetwork.getNode(self, linked_nodes[ns])
                new_node.addLinkTo(n)
                n.addLinkTo(new_node)
                linked_nodes.append(i)
                linked_nodes.append(linked_nodes[ns])

    def getDegreeDist(self):
        size = self.maxDegree() + 1
        hist = [0] * size
        for node in self.nodes:
            i = self.nodes[node].nodelist.__len__()
            hist[i] = hist[i] + 1
        num = np.sum(hist)
        return [i / num for i in hist]

    def getNumLinks(self):
        size = self.maxDegree() + 1
        hist = [0] * size
        for node in self.nodes:
            i = self.nodes[node].nodelist.__len__()
            hist[i] = hist[i] + 1
        return np.sum(hist)