from AbstractNetwork import AbstractNetwork
import re
import numpy

'''
    class to extend AbstractNetwork to read network from file
'''
class GenericNetwork(AbstractNetwork):

    def __init__(self, filename):
        self.filename = filename    # path to file
        self.nodes = {}             # node dict
        self.__createNetwork__()    # build network

    '''
        function to read file and build network
    '''
    def __createNetwork__(self):
        file = open(self.filename, "r")
        for line in file:
            temp = re.split(r'\t+', line)   # split line after tab
            if (temp.__len__() < 2):        # if less than 2 elements, ignore
                continue
            geneA = temp[1]                 # gene, part of all following interactions
            n1 = AbstractNetwork.getNode(self, geneA)   # node from network, according to the gene
            for i in range(2, temp.__len__()):          # iterate over all genes in list, add all links to the network
                # can use getNode(), as it adds a new node automatically if node is not in network yet
                ntemp = AbstractNetwork.getNode(self, temp[i])
                if(n1.id == ntemp.id):                            # not self links allowed
                    continue
                if not (n1.hasLinkTo(ntemp)):                     # add link
                    n1.addLinkTo(ntemp)
                if not (ntemp.hasLinkTo(n1)):                     # add link
                    ntemp.addLinkTo(n1)

    '''
        function to obtain the normalized degree distribution of the network
    '''
    def getDegreeDist(self):
        size = self.maxDegree() + 1
        hist = [0] * size
        for node in self.nodes:
            i = self.nodes[node].nodelist.__len__()
            hist[i] = hist[i] + 1
        num = numpy.sum(hist)
        return [i / num for i in hist]
