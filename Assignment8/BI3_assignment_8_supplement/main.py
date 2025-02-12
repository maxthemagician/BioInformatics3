from data_matrix import DataMatrix
from network import CorrelationNetwork
from correlation import CorrelationMatrix
from cluster import CorrelationClustering


def exercise_1():

    met = DataMatrix("expression.tsv")
    met.to_tsv("Jakob_Mayer_expression.tsv")

    met = DataMatrix("methylation.tsv")
    met.to_tsv("Jakob_Mayer_methylation.tsv")


def exercise_3():
    # TODO
    pass


def exercise_4():
    # TODO
    pass

# only execute the following if this module is the entry point of the program, not when it is imported into another file
if __name__ == '__main__':
    exercise_1()
    exercise_3()
    exercise_4()
