from GenericNetwork import GenericNetwork
from BioGRIDReader import BioGRIDReader
import Tools


'''
    Main:
        call to run exercise 2.3 and create all content for it
'''
if __name__ == '__main__':

    # file spec, put absolute or relative path here
    filename = "BIOGRID-ALL-3.4.159.tab.txt"
    print("\n\tstart reading data from '" + filename + "' ...")
    # reads the BioGrid using the BIOGRIDReader
    grid = BioGRIDReader(filename)
    # get 5 most abundant organisms
    grid.getMostAbundantTaxonIDs(5)
    # prints the 10 most interacting genes in human(9606)
    grid.InteractionNetwork_by_taxID(n=10, id=9606);
    # writes file of all gene interactions in humans to out.txt
    grid.writeInteractionFile(9606, "out.txt")

    # creates real interaction network for humans parsing out.txt
    net = GenericNetwork("out.txt")
    # print net to see it works
    print(net)
    # get degree distribution
    hist = net.getDegreeDist()
    # plot degree distribution in two plots, a shrunken and a full version
    Tools.plotHumanNetwork(hist)








