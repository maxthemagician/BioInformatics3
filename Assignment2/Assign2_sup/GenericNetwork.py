from AbstractNetwork import AbstractNetwork
import re
import numpy

class GenericNetwork(AbstractNetwork):

    def __init__(self, filename):
        self.filename = filename
        self.nodes = {}
        self.__createNetwork__()

    def __createNetwork__(self):
        file = open(self.filename, "r")
        for line in file:
            temp = re.split(r'\t+', line)
            if (temp.__len__() < 2):
                continue
            geneA = temp[1]
            n1 = AbstractNetwork.getNode(self, geneA)
            for i in range(2, temp.__len__()):
                ntemp = AbstractNetwork.getNode(self, temp[i])
                if(n1.id == ntemp.id):
                    continue
                if not (n1.hasLinkTo(ntemp)):
                    n1.addLinkTo(ntemp)
                if not (ntemp.hasLinkTo(n1)):
                    ntemp.addLinkTo(n1)

    def getDegreeDist(self):
        size = self.maxDegree() + 1
        hist = [0] * size
        for node in self.nodes:
            i = self.nodes[node].nodelist.__len__()
            hist[i] = hist[i] + 1
        num = numpy.sum(hist)
        return [i / num for i in hist]