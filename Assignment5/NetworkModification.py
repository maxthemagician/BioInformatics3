from AbstractNetwork import AbstractNetwork
from RandomNetwork import RandomNetwork
import re
import random # you will need it :-)


class NetworkModification:

    def __init__(self, AbstractNetwork):

        self.network = AbstractNetwork

    def evolving(self, timesteps):

        for i in range(timesteps):

            modi = random.randint(0,2)
            network_size = len(self.network.nodes)
            if modi == 1:

                node1 = random.randint(0,  network_size)
                node2 = random.randint(0, len(self.network.getNode(node1).nodelist))

                n1 = self.network.nodes[node1]
                n2 = self.network.getNode(n1.nodelist[node2])

                n1.removeNode(n2)
                n2.removeNode(n1)

            if modi == 0:
                node1 = random.randint(0,  network_size)
                node2 = random.randint(0,  network_size)
                n1 = self.network.getNode(node1)
                n2 = self.network.getNode(node2)

                while node1 == node2 | n1.hasLinkTo(n2):
                    node1 = random.randint(0, network_size)
                    node2 = random.randint(0, network_size)

                n1 = self.network.getNode(node1)
                n2 = self.network.getNode(node2)

                n1.addLinkTo(n2)


if __name__ == "__main__":
    network = RandomNetwork(10, 10)
    netmod = NetworkModification(network)
    NetworkModification.evolving(netmod, 10)
