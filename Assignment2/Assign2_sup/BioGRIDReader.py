import re
from operator import itemgetter

class BioGRIDReader:
    '''Reads BioGRID tab files'''
    def __init__(self, filename):
        '''
        Initialization, read in file and build any data structure that makes you happy
        '''
        self.organisms = {}
        self.file = filename
        file = open(filename, "r")
        read = 1
        count = 0
        total = 0
        for line in file:
            if line.startswith("INTERACTOR_A"):
                read = 0
                continue
            if read == 1:
                continue
            temp = re.split(r'\t+', line)
            if(temp.__len__() != 11):
                continue
            total +=1
            geneA = temp[2]
            geneB = temp[3]
            orgA = int(temp[9])
            orgB = int(temp[10])
            if(orgA == orgB):
                if(self.organisms.__contains__(orgA)):
                    self.organisms[orgA].addInteraction(geneA, geneB)
                else:
                    t = Organism(orgA)
                    self.organisms[orgA] = t
            else:
                if (self.organisms.__contains__(orgA)):
                    self.organisms[orgA].addInteraction(geneA, geneB)
                else:
                    t = Organism(orgA)
                    self.organisms[orgA] = t
                if (self.organisms.__contains__(orgB)):
                    self.organisms[orgA].addInteraction(geneB, geneA)
                else:
                    t = Organism(orgB)
                    self.organisms[orgB] = t

    def getMostAbundantTaxonIDs(self, n):
        all = []
        for key in self.organisms:
            all.append([key, self.organisms[key].interactions.__len__()])
        all.sort(key=itemgetter(1), reverse=True)
        for i in range(0,n):
            print((i+1).__str__() + ". Organism: " + all[i][0].__str__() + ";\tCount: "+ all[i][1].__str__())



class Organism:

    def __init__(self, ncbi_id):
        self.ncbi = ncbi_id
        self.interactions = []

    def addInteraction(self, geneA, geneB):
        self.interactions.append([geneA, geneB])

    def number_of_interactions(self):
        return self.interactions.__len__()

def main():
    filename = "BIOGRID-ALL-3.4.159.tab.txt"
    net = BioGRIDReader(filename)
    net.getMostAbundantTaxonIDs(3)

if __name__ == "__main__":
    main()



