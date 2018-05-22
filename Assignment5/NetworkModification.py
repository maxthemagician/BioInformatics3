from AbstractNetwork import AbstractNetwork
from RandomNetwork import RandomNetwork
from  Cliques_Network_Evolition import Cliques_Network_Evolution
import re
import random # you will need it :-)


class NetworkModification:

    def __init__(self, AbstractNetwork):

        self.network = AbstractNetwork


    def get_random_connected_nodes(self, network):

        set_nodes = list(network.nodes)
        network_size = len(network.nodes)-1

        node1 = random.randint(0, network_size)
        node2 = random.randint(0, network_size)
        n1 = network.nodes[set_nodes[node1]]
        n2 = network.nodes[set_nodes[node2]]

        while (node1 == node2) or not (n1.hasLinkTo(n2)):
            node1 = random.randint(0, network_size)
            node2 = random.randint(0, network_size)
            n1 = network.nodes[set_nodes[node1]]
            n2 = network.nodes[set_nodes[node2]]

        return [node1,node2]

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

                nodes = NetworkModification.get_random_connected_nodes(self, self.network)
                n1 = self.network.nodes[set_nodes[nodes[0]]]
                n2 = self.network.nodes[set_nodes[nodes[1]]]

                n1.removeNode(n2)
                n2.removeNode(n1)




    def randomising(self):

        network = self.network
        sum_edges = 0
        set_nodes = list(network.nodes)
        for node in set_nodes:
            n1 = network.getNode(node)
            sum_edges =+ len(n1.nodelist)

        for e in range(sum_edges):

            nodes1 = NetworkModification.get_random_connected_nodes(self, network)
            nodes2 = NetworkModification.get_random_connected_nodes(self, network)

            n1 = network.nodes[set_nodes[nodes1[0]]]
            n2 = network.nodes[set_nodes[nodes1[1]]]
            n3 = network.nodes[set_nodes[nodes2[0]]]
            n4 = network.nodes[set_nodes[nodes2[1]]]

            n1.removeNode(n2)
            n2.removeNode(n1)
            n3.removeNode(n4)
            n4.removeNode(n3)

            n1.addLinkTo(n4)
            n2.addLinkTo(n3)
            n3.addLinkTo(n2)
            n4.addLinkTo(n1)

        return network



if __name__ == "__main__":
    network = Cliques_Network_Evolution(
        "C:\Users\CarolinM\Desktop\Bioinf3\BioInformatics3\Assignment5\Assign5_supl\chicken_network.tsv")
    netmod = NetworkModification(network)
    NetworkModification.evolving(netmod, 10)
    NetworkModification.randomising(netmod)
