# Node class, assignment 6
from BooleanNode import BooleanNode
import itertools
from collections import defaultdict

class BooleanNetwork:
    def __init__(self):

        self.nodelist = {}
        self.state = 0
        self.attractos_basins = defaultdict(list)
        self.attractos_length = {}
        self.attractor_distribution = defaultdict(list)
        self.attractor_coverage = {}

        #node A
        node = BooleanNode(0)
        node.nodelist = [1, 1, 0, 0, 0, 0]
        self.nodelist[0] = node
        # node B
        node = BooleanNode(1)
        node.nodelist = [0, 0, 1, 0, 0, 0]
        self.nodelist[1] = node
        # node C
        node = BooleanNode(2)
        node.nodelist = [0, 1, 0, 0, 1, 0]
        self.nodelist[2] = node
        # node D
        node = BooleanNode(3)
        node.nodelist = [0, -3, 0, 0, -3, -3]
        self.nodelist[3] = node
        # node E
        node = BooleanNode(4)
        node.nodelist = [0, 0, 0, 0, 0, 1]
        self.nodelist[4] = node
        #node F
        node = BooleanNode(5)
        node.nodelist = [0, 0, 0, 1, 0, 0]
        self.nodelist[5] = node

    def propagation(self, initstart):

        #initializing
        loop_states = []
        self.state = initstart

        #propagate until a loop is found
        while self.state not in loop_states:
            loop_states.append(self.state)
            seq_state = BooleanNetwork.getSequenceFromInt(self, self.state)
            self.state = 0
            post_state = 6 * [0]

            for n in range(len(seq_state)):
                if seq_state[n] == 1:
                    post_state = [i + j for i, j in zip(post_state, self.nodelist[n].nodelist)]

            for i in range(len(post_state)):
                if post_state[i] > 0:
                    self.state += 2**i

            if self.state == 0:
                break


        if self.state != 0:
            self.attractos_basins[self.state].append(initstart)
            self.attractos_length[self.state] = len(loop_states) - loop_states.index(self.state)

        loop_states.append(self.state)
        return loop_states

    def getSequenceFromInt(self, i):
            """Function to print binary number
            for the input decimal using recursion"""
            sequence = []
            while i > 0:
                sequence.append(i % 2)
                i = i // 2

            for i in range(len(sequence),6):
                sequence.append(0)
            return sequence

    def compute_prop_for_all(self):
        self.attractos_basins = defaultdict(list)
        self.attractos_length = {}
        all_possible_intial_states = []
        for i in range(1, 7):
            all_possible_intial_states.append([list(t) for t in list(itertools.combinations([0, 1, 2, 3, 4, 5], i))])
        for i in range(len(all_possible_intial_states)):
            for j in range(len(all_possible_intial_states[i])):
                init_state = 0
                for k in all_possible_intial_states[i][j]:
                    init_state += 2**k
                prop = BooleanNetwork.propagation(self, init_state)
                if prop[len(prop) - 1] > 0:
                    BooleanNetwork.compute_distr_nodes(self,prop, prop.index(prop[len(prop)-1]))
                    self.attractor_coverage[prop[len(prop) - 1]] = len(self.attractos_basins[prop[len(prop) - 1]])/float(64)

    def compute_distr_nodes(self, prop, start):
        num_nodes = [0] * 6
        for l in range(start, len(prop) - 1):
            seq = BooleanNetwork.getSequenceFromInt(self, prop[l])
            num_nodes = [x + y for x, y in zip(seq, num_nodes)]
            orbit_length = float(self.attractos_length[prop[len(prop)-1]])
        self.attractor_distribution[prop[len(prop) - 1]] = [x/orbit_length for x in num_nodes]



if __name__ == "__main__":
    network = BooleanNetwork()
    exercise = [1,4,21,33]
    for i in exercise:
        liststates = BooleanNetwork.propagation(network, i)
        print(liststates)
    BooleanNetwork.compute_prop_for_all(network)
    print(network.attractos_length)
    print(network.attractos_basins)
    print(network.attractor_coverage)
    print(network.attractor_distribution)


