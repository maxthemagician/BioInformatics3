from ScaleFreeNetwork import ScaleFreeNetwork
import Tools

'''
    function to iterate over an interval using floats
    same as range(start, stop, step), but using floats
'''
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


'''
    Main to produce all content needed for exercise 2.1
'''
if __name__ == '__main__':

    # A) see ScaleFreeNetwork.py

    # B) create two scale free networks
    net = ScaleFreeNetwork(10000, 2)        # network with  10 000 nodes
    net2 = ScaleFreeNetwork(100000, 2)      # network with 100 000 nodes
    hist = [0, 1]
    hist2 = [0, 1]
    hist[0] = net.getDegreeDist()           # degree distribution of nets
    hist[1] = net2.getDegreeDist()

    # plot them against each other
    Tools.plotDistributionComparisonLogLog(hist, ["n:  10 000", "n: 100 000"], "Scale Free Networks")

    # compare scale free network of 10 000 nodes with Poisson Distribution
    hist2[0] = hist[0]
    hist2[1] = Tools.getPoissonDistributionHistogram(10000, net.getNumLinks(), hist[0].__len__())
    Tools.plotDistributionComparisonLogLog(hist2, ["n: 10 000", "random"], "Scale Free vs Random")

    # C) using KS distance to compare ScaleFree network and the power law distribution
    min = 1
    index = 0
    # iterate over grid from 1.0 to 3.0 in 0.1 steps to obtain best value of γ
    for i in frange(1.0, 3.0, 0.1):
        z = Tools.getScaleFreeDistributionHistogram(i, hist[0].__len__())   # power dist for γ
        dist = Tools.simpleKSdist(z, hist[0])                               # compute KS distance
        if dist < min:                                                      # keep minimal
            min = dist
            index = i

    # plot power dist for minimal γ against the degree dist of our Scale Free network
    z = Tools.getScaleFreeDistributionHistogram(index, hist[0].__len__())
    Tools.plotDistributionComparisonLogLog([z, hist[0]], ["power law, γ =  " + str(index), "ScaleFreeNet, Node= 10 000"],
                                           "power law vs ScaleFree degree distribution")
