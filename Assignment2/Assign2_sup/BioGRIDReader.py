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
        for line in file:
            if line.startswith("INTERACTOR_A"):
                read = 0
                continue
            if read == 1:
                continue
            temp = re.split(r'\t+', line)
            if(temp.__len__() != 11):
                continue
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

    def getMostAbundantTaxonIDs(self, n):
        all = []
        for key in self.organisms:
            all.append([key, self.organisms[key].number_of_interactions()])
        all.sort(key=itemgetter(1), reverse=True)
        for i in range(0,n):
            print((i+1).__str__() + ". Organism: " + all[i][0].__str__() + ";\tCount: "+ all[i][1].__str__())

    def InteractionNetwork_by_taxID(self, n, id):
        all = []
        human = self.organisms[id]
        for gene in human.interactions:
            all.append([gene, human.interactions[gene].links.__len__()])
        all.sort(key=itemgetter(1), reverse=True)
        print("Top " + n.__str__() + " Genes by degree from Organism " + id.__str__())
        for i in range(0,n):
            print((i+1).__str__() + ". Gene: " + all[i][0].__str__() + ";\tDegeree: "+ all[i][1].__str__())

    def writeInteractionFile(self, taxon_id, filename):
        file = open(filename, "w")
        if not(self.organisms.__contains__(taxon_id)):
            print("Taxon ID '" + taxon_id.__str__() +"' not found in data set...")
            return
        org = self.organisms[taxon_id]
        for gene in org.interactions:
            g = org.interactions[gene]
            links = ""
            first = 0
            for i in g.links:
                if(first == 0):
                    links = links + i
                    first = 1
                else:
                    links = links + "\t"
                    links = links + i

            file.write(org.ncbi.__str__() + "\t" + g.name.__str__() + "\t" + links + "\n")
        file.close()

class Organism:

    def __init__(self, ncbi_id):
        self.ncbi = ncbi_id
        self.interactions = {}
        self.num = 0

    def addInteraction(self, geneA, geneB):
        self.num += 1
        if not self.interactions.__contains__(geneA):
            t = Gene(geneA)
            self.interactions[geneA] = t
        if not self.interactions.__contains__(geneB):
            t = Gene(geneB)
            self.interactions[geneB] = t
        self.interactions[geneA].addLink(geneB)
        self.interactions[geneB].addLink(geneA)

    def number_of_interactions(self):
        return self.num


class Gene:

    def __init__(self, name):
        self.name = name
        self.links = []

    def addLink(self, name):
        if not(self.links.__contains__(name)):
            self.links.append(name)
