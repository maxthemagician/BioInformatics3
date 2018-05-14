from AbstractNetwork import AbstractNetwork
import re

class Cliques_Network_Evolution(AbstractNetwork):

    def __init__(self, filename):
         self.filename = filename    # path to file
         self.nodes = {}             # node dict
         self.__createNetwork__()    # build network

    def __createNetwork__(self):

        file = open(self.filename, "r")

        for line in file:
            temp = re.split(r'\t+', line)  # split line after tab
            if temp.__len__() != 2:  # if less/more than 2 elements, ignore
                continue
            proteinA = temp[0]
            proteinB = temp[1]

            n1 = AbstractNetwork.getNode(self, proteinA)  # node from network, according to the protein
            n2 = AbstractNetwork.getNode(self, proteinB)  # node from network, according to the proetein

            if not (n1.hasLinkTo(n2)):  # add link
                n1.addLinkTo(n2)
                n2.addLinkTo(n1)


    def find_cliques(self):
        

if __name__ == "__main__":

    network = Cliques_Network_Evolution("C:\Users\CarolinM\Desktop\Bioinf3\BioInformatics3\Assignment5\Assign5_supl\human_network.tsv")
