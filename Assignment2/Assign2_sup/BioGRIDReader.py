import re
from operator import itemgetter


class BioGRIDReader:
    '''Reads BioGRID tab files'''

    def __init__(self, filename):
        '''
        Initialization, read in file and build any data structure that makes you happy
        '''
        self.organisms = {}  # dictionary of all organisms in the data
        self.file = filename
        file = open(filename, "r")  # open file to read
        read = 1
        for line in file:
            if line.startswith("INTERACTOR_A"):   # skip intro in file until header of table occurs
                read = 0
                continue
            if read == 1:
                continue

            temp = re.split(r'\t+', line)  # split every line
            if (temp.__len__() != 11):
                continue
            geneA = temp[2]     # extract only name of genes and both organisms
            geneB = temp[3]
            orgA = int(temp[9])
            orgB = int(temp[10])
            if (orgA == orgB):     # add to the according dictionary if the two organisms are the same
                if (self.organisms.__contains__(orgA)):
                    self.organisms[orgA].addInteraction(geneA, geneB)
                else:
                    t = Organism(orgA)
                    self.organisms[orgA] = t

    '''
        function to get the most 'n' abundant Organisms from the data based on simple linkage counting
    '''
    def getMostAbundantTaxonIDs(self, n):
        all = []
        for key in self.organisms:      # export all organisms with count
            all.append([key, self.organisms[key].number_of_interactions()])
        all.sort(key=itemgetter(1), reverse=True)   # sort by counting

        # print n top organisms
        print("Top " + n.__str__() + " Organism by number of gene interactions")
        for i in range(0, n):
            print((i + 1).__str__() + ". Organism: " + all[i][0].__str__() + ";\tCount: " + all[i][1].__str__())

        return all[0:n]

    '''
        Function to print the 'n' Genes with highest degree for a given taxon ID
    '''
    def InteractionNetwork_by_taxID(self, n, id):
        all = []
        if not (self.organisms.__contains__(id)):   # print if id not in set
            print("Taxon ID '" + id.__str__() + "' not found in data set...")
            return

        org = self.organisms[id]
        for gene in org.interactions:   # export every gene with degree
            all.append([gene, org.interactions[gene].links.__len__()])
        all.sort(key=itemgetter(1), reverse=True)   # sort by degree

        # printing top n genes
        print("Top " + n.__str__() + " Genes by degree from Organism " + id.__str__())
        for i in range(0, n):
            print((i + 1).__str__() + ". Gene: " + all[i][0].__str__() + ";\tDegeree: " + all[i][1].__str__())

    '''
        Function to write a file with all gene interactions in the read dataset
        according to the given taxon id
        Format: (tab delimited)
        Organism_Id     Gene_ID     List of Gene_ID where a interaction was found
    '''
    def writeInteractionFile(self, taxon_id, filename):
        file = open(filename, "w")
        if not (self.organisms.__contains__(taxon_id)):  # print if id not in set
            print("Taxon ID '" + taxon_id.__str__() + "' not found in data set...")
            return
        org = self.organisms[taxon_id]
        for gene in org.interactions:
            g = org.interactions[gene]
            links = ""
            first = 0
            for i in g.links:
                if (first == 0):
                    links = links + i
                    first = 1
                else:
                    links = links + "\t"
                    links = links + i

            file.write(org.ncbi.__str__() + "\t" + g.name.__str__() + "\t" + links + "\n")
        file.close()

'''
    Class to represent an organism
'''
class Organism:

    def __init__(self, ncbi_id):
        self.ncbi = ncbi_id     # id
        self.interactions = {}  # list if genes with interactions
        self.num = 0            # number of interactions

    '''
        add interaction between two given genes
    '''
    def addInteraction(self, geneA, geneB):
        self.num += 1   # increase counter of interactions
        if not self.interactions.__contains__(geneA):   # if genes not in dictionary yet, create new gene
            t = Gene(geneA)
            self.interactions[geneA] = t
        if not self.interactions.__contains__(geneB):   # if genes not in dictionary yet, create new gene
            t = Gene(geneB)
            self.interactions[geneB] = t
        self.interactions[geneA].addLink(geneB)     # add link
        self.interactions[geneB].addLink(geneA)     # add link

    '''
        function to get the number of interactions 
    '''
    def number_of_interactions(self):
        return self.num


'''
    class to represent a gene
'''
class Gene:

    '''
        got name and a list of genes, which it interacts with
    '''
    def __init__(self, name):
        self.name = name
        self.links = []

    '''
        add link to gene, if link does not exist yet
    '''
    def addLink(self, name):
        if(name == self.name):  # no self links are allowd
            return
        if not (self.links.__contains__(name)):
            self.links.append(name)
