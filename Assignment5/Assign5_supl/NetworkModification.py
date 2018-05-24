import random

import matplotlib.pyplot as plt
from Cliques_Network_Evolution import Cliques_Network_Evolution


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

        return [node1, node2]

    def evolving(self, timesteps):
        set_nodes = list(self.network.nodes)
        network_size = len(self.network.nodes)-1

        result = []

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

        network_copie = self.network
        sum_edges = 0
        set_nodes = list(network_copie.nodes)

        for node in set_nodes:
            n1 = network_copie.getNode(node)
            sum_edges = sum_edges + len(n1.nodelist)

        for e in range(sum_edges):

            nodes1 = NetworkModification.get_random_connected_nodes(self, network_copie)
            nodes2 = NetworkModification.get_random_connected_nodes(self, network_copie)
            while (nodes1[0] == nodes2[0]) | (nodes1[1] == nodes2[1]) | (nodes1[0] == nodes2[1]) | (nodes1[1] == nodes2[0]):
                nodes1 = NetworkModification.get_random_connected_nodes(self, network_copie)
                nodes2 = NetworkModification.get_random_connected_nodes(self, network_copie)

            n1 = network_copie.nodes[set_nodes[nodes1[0]]]
            n2 = network_copie.nodes[set_nodes[nodes1[1]]]
            n3 = network_copie.nodes[set_nodes[nodes2[0]]]
            n4 = network_copie.nodes[set_nodes[nodes2[1]]]

            n1.removeNode(n2)
            n2.removeNode(n1)
            n3.removeNode(n4)
            n4.removeNode(n3)

            n1.addLinkTo(n4)
            n2.addLinkTo(n3)
            n3.addLinkTo(n2)
            n4.addLinkTo(n1)

        sum_edges = 0
        set_nodes = list(network_copie.nodes)

        for node in set_nodes:
            n1 = network_copie.getNode(node)
            sum_edges = sum_edges + len(n1.nodelist)

        return network_copie


    def enrichment(self, n):

        randomised_cliques = []
        sum_enriched_networks = [0,0,0]
        cliques = Cliques_Network_Evolution.find_cliques(self.network, self.network)
        for i in range(n):
            val = int(i/n * 100)
            print(val.__str__() + '%', end='\r')
            r_network = NetworkModification.randomising(self)
            r_cliques = Cliques_Network_Evolution.find_cliques(self.network, r_network)
            randomised_cliques.append(r_cliques)
            #print(r_cliques)
        print('100%')

        print(randomised_cliques)

        for i in range(len(randomised_cliques)):
            if not randomised_cliques[i][0] < cliques[0]:
                sum_enriched_networks[0] = 1 + sum_enriched_networks[0]
            if not randomised_cliques[i][1] < cliques[1]:
                sum_enriched_networks[1] = 1 + sum_enriched_networks[1]
            if not randomised_cliques[i][2] < cliques[2]:
                sum_enriched_networks[2] = 1 + sum_enriched_networks[2]
        print(sum_enriched_networks)
        return [float(sum_enriched_networks[0])/n, float(sum_enriched_networks[1])/n, float(sum_enriched_networks[2])/n]

def plotNetwork(data):
    axes = plt.gca()
    axes.set_xlim([0, 100])
    plt.plot(data, marker='x')

    # remember: never forget labels!
    plt.xlabel('time')
    plt.ylabel('#cliques')

    # you don't have to do something stuff here
    plt.legend(["3", "4", "5"])
    plt.title("Plot 1")
    plt.tight_layout()
    plt.savefig("Plot_1.png")


if __name__ == "__main__":

    # evolution
    print('Start Network evolving ...')
    network = Cliques_Network_Evolution("rat_network.tsv")
    print(Cliques_Network_Evolution.find_cliques(network, network))
    ev_network = NetworkModification(network)
    res = []
    # compute cliques for first 100 time steps
    for i in range(100):
        print(i.__str__() + '%', end='\r')
        NetworkModification.evolving(ev_network, 1)
        res.append(Cliques_Network_Evolution.find_cliques(network, ev_network.network))
    print('100%')
    plotNetwork(res)
    print(res[99])
    ev2_network = NetworkModification(network)
    NetworkModification.evolving(ev2_network, 1000)
    print(Cliques_Network_Evolution.find_cliques(network, ev2_network.network))


    # enrichment, may take time
    print('Start enrichment, this will take for ever ... \n')
    network = Cliques_Network_Evolution("chicken_network.tsv")
    netmod = NetworkModification(network)
    print(NetworkModification.enrichment(netmod, 100))





