import matplotlib.pyplot as plt
import math

import numpy as np


def plotDistributionComparison(histograms, legend, title):
    '''
    Plots a list of histograms with matching list of descriptions as the legend
    '''
    # determine max. length
    max_length = max(len(x) for x in histograms)
    
    # extend "shorter" distributions
    for x in histograms:
        x.extend([0.0]* (max_length-len(x)) )
        
    # plots histograms
    for h in histograms:
        plt.plot(range(len(h)), h, marker = 'x')
    
    # remember: never forget labels!
    plt.xlabel('degree')
    plt.ylabel('P')
    
    # you don't have to do something stuff here
    plt.legend(legend)
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plotDistributionComparisonLogLog(histograms, legend, title):
    '''
    Plots a list of histograms with matching list of descriptions as the legend
    '''
    ax = plt.subplot()
    # determine max. length
    max_length = max(len(x) for x in histograms)
    
    # extend "shorter" distributions
    for x in histograms:
        x.extend([0.0]* (max_length-len(x)) )
    
    ax.set_xscale("log")  
    ax.set_yscale("log")
      
    # plots histograms
    for h in histograms:
        ax.plot(range(len(h)), h, marker = 'x', linestyle='')
    
    # remember: never forget labels!
    plt.xlabel('degree')
    plt.ylabel('P')
    
    # you don't have to do something stuff here
    plt.legend(legend)
    plt.title(title)
    plt.tight_layout()
    plt.show()
    
def getScaleFreeDistributionHistogram(gamma, k):

    '''
        function to create Scale Free distribution based on the power law distribution, normalized
    '''
    histogram = [0.0] * k
    for i in range(1,k):
        histogram[i] = math.pow(i, -gamma)
    num = np.sum(histogram)
    return [i / num for i in histogram]


def simpleKSdist(histogram_a, histogram_b):
    '''
        function to compute the Kolmogorov-Smirnov distance
    '''

    a_sum = np.cumsum(histogram_a)
    b_sum = np.cumsum(histogram_b)

    index_max_deviate = -1
    for i in range(2, histogram_a.__len__()):   # start at degree 2, because no node can have degree < 2, as we start with 2
        deviate = abs(a_sum[i] - b_sum[i])
        if deviate > index_max_deviate:
            index_max_deviate = deviate

    return index_max_deviate


'''
    Function to plot a the degree distribution of the human interaction network
    takes hisogram
    creates two plots, one with a shrunken x-axis, one with all entries
'''
def plotHumanNetwork(hist):
    axes = plt.gca()
    axes.set_xlim([0, 100])
    plt.plot(hist, marker='x')

    # remember: never forget labels!
    plt.xlabel('degree')
    plt.ylabel('P')

    # you don't have to do something stuff here
    plt.legend(["Human"])
    plt.title("Plot 1")
    plt.tight_layout()
    plt.show()
    plt.savefig("Plot1")

    axes = plt.gca()
    axes.set_xlim([0, 2369])
    plt.plot(hist, marker='x')

    # remember: never forget labels!
    plt.xlabel('degree')
    plt.ylabel('P')

    # you don't have to do something stuff here
    plt.legend(["Human"])
    plt.title("Plot 2")
    plt.tight_layout()
    plt.show()
    plt.savefig("Plot2")


def getPoissonDistributionHistogram(num_nodes, num_links, k):
    '''
    Generates a Poisson distribution histogram up to k
    '''
    lam = 2 * num_links / num_nodes
    res = [0]*k
    res[0] = math.exp(-lam)
    for i in range(1, k):
        res[i] = lam/k * res[i-1]
    return res