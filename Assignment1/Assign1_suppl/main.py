from RandomNetwork  import RandomNetwork
from DegreeDistribution import DegreeDistribution

def main():
    r = RandomNetwork(amount_nodes=1000, amount_links=2000)
    d = DegreeDistribution(r)
    print(d.hist)
    print(d.getNormalizedDistribution())


if __name__ == "__main__":
    main()