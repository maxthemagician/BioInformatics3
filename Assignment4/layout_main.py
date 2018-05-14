from layout import Layout
from tools import plot_layout, plot_energies

energy1 = []
energy2 = []
nets = ["star.txt", "square.txt", "star++.txt", "dog.txt"]
for name in nets:
    print("creating layout for " + name + " ...")
    temp_layout = Layout(name)
    Layout.init_positions(temp_layout)
    e1 = Layout.layout(temp_layout, 1000)
    # save energy
    energy1.append(e1)
    plot_layout(temp_layout, name + "; final energy: " + float(e1[999]).__str__())
    e2 = Layout.simulated_annealing_layout(temp_layout, 1000)
    # save energy
    energy2.append(e2)
    plot_layout(temp_layout,"simulated annealing for " + name + "; final energy: " + float(e2[999]).__str__())

plot_energies([energy1[0], energy2[0]], ["force directed", "simulated annealing"], "energy plot for star.txt")
