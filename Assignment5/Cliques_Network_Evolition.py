from AbstractNetwork import AbstractNetwork
import re

class Cliques_Network_Evolution(AbstractNetwork):

    def __init__(self, filename):

        self.filename = filename  # path to file
        self.nodes = {}  # node dict
        self.__createNetwork__()  # build network

    def __createNetwork__(self):

        file = open(self.filename, "r")
        for line in file:
            temp = re.split(r'\t+', line)  # split line after tab
            if temp.__len__() != 2:  # if less/more than 2 elements, ignore
                continue
            proteinA = temp[0]
            proteinB = temp[1].replace("\n", "")

            n1 = AbstractNetwork.getNode(self, proteinA)  # node from network, according to the protein
            n2 = AbstractNetwork.getNode(self, proteinB)  # node from network, according to the proetein

            if not (n1.hasLinkTo(n2)):  # add link
                n1.addLinkTo(n2)
                n2.addLinkTo(n1)

    def find_cliques(self, network):
        cliques = []
        set_nodes = list(network.nodes)
        k = 0
        l = 0
        for node in set_nodes:

            n1 = network.getNode(node)

            for i in range(0, len(n1.nodelist)):

                for j in range(len(n1.nodelist[i].nodelist)):
                    clique_size = 0

                    if n1 in n1.nodelist[i].nodelist[j].nodelist:
                        clique_size = 3

                        for k in range(len(n1.nodelist[i].nodelist[j].nodelist)):
                            cond1 = n1 in n1.nodelist[i].nodelist[j].nodelist[k].nodelist
                            cond2 = n1.nodelist[i] in n1.nodelist[i].nodelist[j].nodelist[k].nodelist
                            if cond1 & cond2:
                                clique_size = 4

                                for l in range(len(n1.nodelist[i].nodelist[j].nodelist[k].nodelist)):
                                    cond1 = n1 in n1.nodelist[i].nodelist[j].nodelist[k].nodelist[l].nodelist
                                    cond2 = n1.nodelist[i] in n1.nodelist[i].nodelist[j].nodelist[k].nodelist[l].nodelist
                                    cond3 = n1.nodelist[i].nodelist[j] in n1.nodelist[i].nodelist[j].nodelist[k].nodelist[l].nodelist
                                    if cond1 & cond2 & cond3:
                                        clique_size = 5
                                        if sorted(
                                                [str(n1), str(n1.nodelist[i]), str(n1.nodelist[i].nodelist[j]),
                                                 str(n1.nodelist[i].nodelist[j].nodelist[k]), str(
                                                        n1.nodelist[i].nodelist[j].nodelist[k].nodelist[
                                                            l])]) not in cliques:

                                            cliques.append(sorted(
                                                [str(n1), str(n1.nodelist[i]), str(n1.nodelist[i].nodelist[j]),
                                                 str(n1.nodelist[i].nodelist[j].nodelist[k]),
                                                 str(n1.nodelist[i].nodelist[j].nodelist[k].nodelist[l])]))
                                if (clique_size == 4) & (sorted(
                                        [str(n1), str(n1.nodelist[i]), str(n1.nodelist[i].nodelist[j]),
                                         str(n1.nodelist[i].nodelist[j].nodelist[k])]) not in cliques):

                                    cliques.append(sorted(
                                        [str(n1), str(n1.nodelist[i]), str(n1.nodelist[i].nodelist[j]),
                                         str(n1.nodelist[i].nodelist[j].nodelist[k])]))


                        if (clique_size == 3) & (sorted([str(n1),  str(n1.nodelist[i]), str(n1.nodelist[i].nodelist[j])]) not in cliques):
                            cliques.append(sorted([str(n1),  str(n1.nodelist[i]), str(n1.nodelist[i].nodelist[j])]))

        sum_cliques = [0,0,0]
        for i in range(len(cliques)):
            if len(cliques[i]) == 3:
                sum_cliques[0] = sum_cliques[0] + 1
            if len(cliques[i]) == 4:
                sum_cliques[1] = sum_cliques[1] + 1
            if len(cliques[i]) == 5:
                sum_cliques[2] = sum_cliques[2] + 1

        return(sum_cliques)

if __name__ == "__main__":
    network = Cliques_Network_Evolution(
        "C:\Users\CarolinM\Desktop\Bioinf3\BioInformatics3\Assignment5\Assign5_supl\chicken_network.tsv")
    Cliques_Network_Evolution.find_cliques(network, network)
