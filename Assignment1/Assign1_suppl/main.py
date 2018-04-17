from RandomNetwork  import RandomNetwork
from DegreeDistribution import DegreeDistribution

def main():
    r = RandomNetwork(amount_nodes=10, amount_links=15)
    d = DegreeDistribution(r)
    print(r.__str__())
    print(d.hist)
    print(d.getNormalizedDistribution())


if __name__ == "__main__":
    main()