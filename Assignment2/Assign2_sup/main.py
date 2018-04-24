from GenericNetwork import GenericNetwork
from BioGRIDReader import BioGRIDReader
import Tools

if __name__ == '__main__':
    filename = "BIOGRID-ALL-3.4.159.tab.txt"
    net = BioGRIDReader(filename)
    net.getMostAbundantTaxonIDs(5)
    net.InteractionNetwork_by_taxID(n=10, id=9606);
    net.writeInteractionFile(9606, "out.txt")

    net = GenericNetwork("out.txt")
    print(net.maxDegree())
    print(net)

    hist = net.getDegreeDist()

    Tools.plotHumanNetwork(hist)

