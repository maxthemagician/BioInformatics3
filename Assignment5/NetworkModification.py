from AbstractNetwork import AbstractNetwork
from RandomNetwork import RandomNetwork
from  Cliques_Network_Evolition import Cliques_Network_Evolution
import re
import random # you will need it :-)


class NetworkModification:

    def __init__(self, AbstractNetwork):

        self.network = AbstractNetwork

    def evolving(self, timesteps):
        set_nodes = list(self.network.nodes)
        network_size = len(self.network.nodes)-1

        for i in range(timesteps):

            modi = random.randint(0, 2)


            node1 = random.randint(0,network_size)
            node2 = random.randint(0,network_size)
            n1 = self.network.nodes[set_nodes[node1]]
            n2 = self.network.nodes[set_nodes[node2]]

            if modi == 1:

                while (node1 == node2) or (n1.hasLinkTo(n2)):
                    node1 = random.randint(0,network_size)
                    node2 = random.randint(0,network_size)
                    n1 = self.network.nodes[set_nodes[node1]]
                    n2 = self.network.nodes[set_nodes[node2]]

                n1.addLinkTo(n2)
                n2.addLinkTo(n1)

            if modi == 0:
                while (node1 == node2) or not (n1.hasLinkTo(n2)):
                    node1 = random.randint(0,network_size)
                    node2 = random.randint(0,network_size)
                    n1 = self.network.nodes[set_nodes[node1]]
                    n2 = self.network.nodes[set_nodes[node2]]

                n1.removeNode(n2)
                n2.removeNode(n1)


if __name__ == "__main__":
    network = Cliques_Network_Evolution(
        "C:\Users\CarolinM\Desktop\Bioinf3\BioInformatics3\Assignment5\Assign5_supl\chicken_network.tsv")
    netmod = NetworkModification(network)
    NetworkModification.evolving(netmod, 10)
