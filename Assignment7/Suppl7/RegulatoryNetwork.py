# Regulatory Network Prediction, assignment 7
import sys
import numpy as np
from scipy.stats import norm
import re
import math
from operator import itemgetter
from collections import OrderedDict

class RegulatoryNetwork:
    def __init__(self, filename):
        self.expr_matrix = np.zeros((10,10))
        self.p = {}
        self.deleted = []
        self.regulators = {}
        self.p_size = 0
        file = open(filename, "r")
        for i,line in enumerate(file):
            line = line.strip('\n')
            temp = re.split(r'\t+', line)  # split line after tab
            if i == 1:
                self.wildtype = map(float, temp[1:11])
            if i > 1:
                temp = map(float, temp[1:11])
                for s in range(10):
                    self.expr_matrix[s][i-2] = temp[s]

    def computeInitialP(self):
        for i in range(10):
            for j in range(10):
                if i != j:
                    sigma = np.var(self.expr_matrix[i])
                    p_value = norm.cdf((math.fabs(self.expr_matrix[i][j] - self.wildtype[i])) /sigma)
                    p_value = (2 * p_value) - 1
                    if p_value <= 0.05:
                        self.regulators[tuple([i,j])] = p_value
                    else:
                        self.p[tuple([i, j])] = p_value
        self.deleted = [0] * len(self.p)
        self.p_size = len(self.p)

    def computeSigma(self, r):
        sum_ = 0
        p_size = 0
        for i in range(len(self.p)):
            if self.deleted[i] == 0 and r == self.p.keys()[i][0]:
                b = self.p.keys()[i][1]
                sum_ += (self.expr_matrix[r][b] - self.wildtype[r])**2
                p_size += 1
        if p_size == 1:
            return 0
        return math.sqrt(float(sum_)/(p_size - 1))

    def computeWildType(self):
        for i in range(10):
            sum_ = 0
            sum_pairs = 0
            for j in range(len(self.p)):
                if self.deleted[j] == 0 and self.p.keys()[j][0] == i:
                    b = self.p.keys()[j][1]
                    sum_ += self.expr_matrix[i][b]
                    sum_pairs += 1
            self.wildtype[i] = float(self.wildtype[i] + sum_)/(1 + sum_pairs)

    def computeP(self):
        sigma = [0] * 10
        RegulatoryNetwork.computeWildType(self)
        to_delete = self.deleted
        for i in range(10): sigma[i] = RegulatoryNetwork.computeSigma(self, i)
        count_deleted = 0
        for i in range(len(self.p.keys())):
            if self.deleted[i] == 0:
                a = self.p.keys()[i][0]
                b = self.p.keys()[i][1]
                p_value = 1
                if sigma[a] != 0:
                    x = float(math.fabs(self.expr_matrix[a][b] - self.wildtype[a])) / sigma[a]
                    p_value = (2 * norm.cdf(x)) - 1
                if p_value <= 0.05:
                    self.regulators[tuple([a, b])] = p_value
                    to_delete[i] = 1
                    count_deleted += 1
        self.deleted = to_delete
        self.p_size = self.p_size - count_deleted

    def compute(self):
        RegulatoryNetwork.computeInitialP(self)
        prae_size = 0
        while(self.p_size != prae_size or self.p_size == 0):
            prae_size = self.p_size
            RegulatoryNetwork.computeP(self)
        return self.regulators


    def printOutput(self):

        sorted_significant = OrderedDict(sorted(self.regulators.items(), key=itemgetter(1)))
        sorted_p = OrderedDict(sorted(self.p.items(), key=itemgetter(1)))
        for i in range(len(sorted_significant)):
            print(str(sorted_significant.keys()[i][1]) + "\t" + str(sorted_significant.keys()[i][0]) + "\t" + str(sorted_significant.values()[i]))
        for i in range(len(sorted_p)):
            print(str(sorted_p.keys()[i][1]) + "\t" + str(sorted_p.keys()[i][0]) + "\t" + str(
                sorted_p.values()[i]))

def main(path):
    rn = RegulatoryNetwork(path)
    RegulatoryNetwork.computeInitialP(rn)
    rn.compute()
    RegulatoryNetwork.printOutput(rn)

main(sys.argv[1])