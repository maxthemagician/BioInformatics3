import matplotlib.pyplot as plt
import numpy as np
import math

def plotDistributionComparison(histograms, legend, title):
    '''
    Plots a list of histograms with matching list of descriptions as the legend
    '''
    # adjust size of elements in histogram
    maxlen = 0
    for h in histograms:
        if len(h) > maxlen:
            maxlen = len(h)

    for h in histograms:
        while len(h) != maxlen:
            h.append(0.0)

    # plots histograms
    for h in histograms:
        plt.plot(range(len(h)), h, marker = 'x')
    
    # remember: never forget labels! :-)
    plt.xlabel('Degree of k')
    plt.ylabel('Density')
    
    # you don't have to do something here
    plt.legend(legend)
    plt.title(title)
    plt.tight_layout()# might throw a warning, no problem
    plt.show()

def getPoissonDistributionHistogram(num_nodes, num_links, k):
    '''
    Generates a Poisson distribution histogram up to k
    '''
    lam = 2 * num_links / num_nodes
    res = [0]*k
    for i in range(0, k):
        res[i] = poisson(lam, i)
    return res

def poisson(lam, k):

    if(k == 0):
        return math.exp(-lam)
    else:
        return (lam/k * poisson(lam,k-1))