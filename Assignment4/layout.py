from random import gauss
import random as r
import math
from generic_network import GenericNetwork


class Layout:
    def __init__(self, file_path):
        """
        :param file_path: path to a white-space-separated file that contains node interactions
        """
        # create a network from the given file
        self.network = GenericNetwork()
        self.network.read_from_tsv(file_path)
        # friction coefficient
        self.alpha = 0.03
        # random force interval
        self.interval = 0.3
        # initial square to distribute nodes
        self.size = 50
        # total energy
        self.total_energy = 0

    def init_positions(self):
        """
        Initialise or reset the node positions, forces and charge.
        """
        r.seed(1)
        for node_name in self.network.nodes:
            node = self.network.get_node(node_name)
            node.pos_x = r.randint(1, self.size)
            node.pos_y = r.randint(1, self.size)

        self.calculate_forces()


    def calculate_forces(self):
        """
        Calculate the force on each node during the current iteration.
        """
        self.total_energy = 0
        for n_name in self.network.nodes:
            n1 = self.network.get_node(n_name)
            n1.force_x = 0
            n1.force_y = 0

            for n1_name in self.network.nodes:
                n1 = self.network.get_node(n1_name)

                for n2_name in self.network.nodes:
                    if n1_name != n2_name:
                        w = 0
                        n2 = self.network.get_node(n2_name)
                        if n1.has_edge_to(n2):
                            w = 1

                        delta_x = n1.pos_x - n2.pos_x
                        delta_y = n1.pos_y - n2.pos_y

                        F_h_x = -1 * delta_x
                        F_h_y = -1 * delta_y

                        z_x = float(delta_x * n1.degree() * n2.degree())
                        z_y = float(delta_y * n1.degree() * n2.degree())
                        n = ((delta_x ** 2) + (delta_y ** 2)) ** (3/2)

                        f_x =(z_x/n) + (w * F_h_x)
                        f_y = (z_y/n) + (w * F_h_y)

                        n1.force_x += f_x
                        n1.force_y += f_y

                        e_c = float(n1.degree() * n2.degree())/(((delta_x ** 2) + (delta_y ** 2)) ** (1/2))
                        e_h = 0.5 * ((delta_x ** 2) + (delta_y ** 2))
                        self.total_energy += e_c + e_h


    def add_random_force(self, temperature):
        """
        Add a random force within [- temperature * interval, temperature * interval] to each node.
        (There is nothing to do here for you.)
        :param temperature: temperature in the current iteration
        """
        for node in self.network.nodes.values():
            node.force_x += gauss(0.0, self.interval * temperature)
            node.force_y += gauss(0.0, self.interval * temperature)

    def displace_nodes(self):
        """
        Change the position of each node according to the force applied to it and reset the force on each node.
        """
        for n_name in self.network.nodes:
            n = self.network.get_node(n_name)
            n.pos_x += self.alpha * n.force_x
            n.pos_y += self.alpha * n.force_y

    def calculate_energy(self):
        """
        Calculate the total energy of the network in the current iteration.
        :return: total energy
        """
        return self.total_energy/2

    def layout(self, iterations):
        """
        Executes the force directed layout algorithm. (There is nothing to do here for you.)
        :param iterations: number of iterations to perform
        :return: list of total energies
        """
        # initialise or reset the positions and forces
        self.init_positions()
        energies = []

        for _ in range(iterations):
            self.calculate_forces()
            self.displace_nodes()
            energies.append(self.calculate_energy())

        return energies

    def simulated_annealing_layout(self, iterations):
        """
        Executes the force directed layout algorithm with simulated annealing.
        :param iterations: number of iterations to perform
        :return: list of total energies
        """
        self.init_positions()
        energies = []
        temperature = iterations

        for i in range(iterations):
            # TODO: DECREASE THE TEMPERATURE IN EACH ITERATION. YOU CAN BE CREATIVE.
            temperature -= 1
            # there is nothing to do here for you
            self.calculate_forces()
            self.add_random_force(temperature)
            self.displace_nodes()
            energies.append(self.calculate_energy())

        return energies



if __name__ == "__main__":
        layout = Layout("C:\Users\CarolinM\Desktop\BioInf\supplement\star.txt")
        Layout.init_positions(layout)
        Layout.layout(layout, 1000)
        Layout.simulated_annealing_layout(layout, 1000)



