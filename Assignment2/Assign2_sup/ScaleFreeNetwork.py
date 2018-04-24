import random
from AbstractNetwork import AbstractNetwork
from Node import Node

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
        for i in range(3, amount_nodes):

            limit = amount_links
            network_size = AbstractNetwork.size()
            if amount_links > network_size:
                limit = network_size

            AbstractNetwork.appendNode(i)
            new_node = AbstractNetwork.getNode(self, i)

            for j in range (0, limit):
                n = random.randint(0, sorted_nodes.size())

                while not new_node.hasLinkTo(n):
                    n = random.randint(0, sorted_nodes.size())

                new_node.addLinkTo(n)
                n.addLinkTo(new_node)
                linked_nodes.extend(i)
                linked_nodes.extend(n)

