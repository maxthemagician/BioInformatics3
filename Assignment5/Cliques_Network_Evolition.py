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

    def find_cliques(self):
        cliques = [[]]
        set_nodes = list(self.nodes)

        for node in set_nodes:
            n1 = self.getNode(node)
            for node2 in n1.nodelist:
                n2 = self.getNode(node2)

                print(list(set(n1.nodelist) & set(n2.nodelist)))
                if node2 != node:
                    for node3 in n2.nodelist:
                        print("hier")
                        print(node3)

                        n3 = self.getNode(node3)
                        if n3.hasLinkTo(n1):
                            print(found)





        print(cliques)

if __name__ == "__main__":
    network = Cliques_Network_Evolution(
        "C:\Users\CarolinM\Desktop\Bioinf3\BioInformatics3\Assignment5\Assign5_supl\\test.tsv")
    Cliques_Network_Evolution.find_cliques(network)
