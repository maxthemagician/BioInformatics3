from AbstractNetwork import AbstractNetwork
from Node import Node
import random # you will need it :-)

class RandomNetwork(AbstractNetwork):
    """Random network implementation of AbstractNetwork"""
    
    def __createNetwork__(self, amount_nodes, amount_links): # remaining methods are taken from AbstractNetwork
        """
        Creates a random network
        1. Build a list of n nodes
        2. For i=#links steps, add a connection between for two randomly chosen nodes that are not yet connected
        """
        random.seed()

        for i in range(0, amount_nodes):
            AbstractNetwork.appendNode(self, node=Node(i))

        size = AbstractNetwork.size(self)-1
        for i in range(0, amount_links):
            k1 = random.randint(0, size)
            k2 = random.randint(0, size)
            n1 = AbstractNetwork.getNode(self, k1)
            n2 = AbstractNetwork.getNode(self, k2)
            n1.addLinkTo(n2)
            n2.addLinkTo(n1)
