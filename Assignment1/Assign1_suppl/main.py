from RandomNetwork import RandomNetwork

def main():
    r = RandomNetwork(amount_nodes=10, amount_links=15)
    print(r.size())
    print(r.__str__())

if __name__ == "__main__":
    main()