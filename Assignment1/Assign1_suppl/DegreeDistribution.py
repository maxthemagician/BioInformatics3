class DegreeDistribution:
    """Calculates a degree distribution for a network"""

    def __init__(self, network):
        """
        Inits DegreeDistribution with a network and calculate its distribution
        """
        self.hist = [0] * network.maxDegree()
        for node in network.nodes:
            i = self.nodes[node].nodes.__len__()
            self.hist[i] = self.hist[i] + 1


    
    def getNormalizedDistribution(self):
        '''
        Returns the computed normalized distribution
        '''
        