import numpy

class DegreeDistribution:
    """Calculates a degree distribution for a network"""
    def __init__(self, network):
        """
        Inits DegreeDistribution with a network and calculate its distribution
        """
        size = network.maxDegree() +1
        self.hist = [0] * size
        for node in network.nodes:
            i = network.nodes[node].nodes.__len__()
            self.hist[i] = self.hist[i] + 1

    def getNormalizedDistribution(self):
        '''
        Returns the computed normalized distribution
        '''
        hist_nom = self.hist
        num = numpy.sum(self.hist)
        hist_nom = hist_nom / num
        return hist_nom