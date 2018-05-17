from AbstractNetwork import AbstractNetwork
import re

class NetworkModification:

    def __init__(self, AbstractNetwork):

        self.network = AbstractNetwork

    def evolving(self, timesteps):

        for i in range(timestep):
            node = random.randint(0, len(self.network))
            edge = random.randint(0, len(self.network.getNode(node).nodelist))

            node = Node(network.size)
            network.appendNode(node);



if __name__ == "__main__":
    network = Cliques_Network_Evolution(
        "C:\Users\CarolinM\Desktop\Bioinf3\BioInformatics3\Assignment5\Assign5_supl\chicken_network.tsv")
    Cliques_Network_Evolution.find_cliques(network)
