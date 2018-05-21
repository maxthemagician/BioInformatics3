from GenericNetwork import GenericNetwork

def create_mapping_uniprot(file):
    #read file
    #create dictionary with mapping from gene to uniprot id
    mapping_u_gl = {}
    mapping_g_ul = {}
    f = open(file, 'r')
    for line in f:
        if line.__len__() == 0:
            continue
        if line.startswith('Entry'):
            continue
        line = line.split('\t')
        entry = line[0]
        names = line[4]
        names = names.split()
        for i in names:
            # mapping from uniprot to gene
            if mapping_g_ul.get(entry) is not None:
                s = mapping_g_ul.get(entry)
                s.append(i)
                mapping_g_ul[entry] = s
            else:
                mapping_g_ul[entry] = [i]

            # mapping from gene to uniprot id
            if mapping_u_gl.get(i) is not None:
                s = mapping_u_gl.get(i)
                s.append(entry)
                mapping_u_gl[i] = s
            else:
                mapping_u_gl[i] = [entry]

    return [mapping_u_gl, mapping_g_ul]





# NRXN1
# E5DFI5
def main():

    net_file = "chicken_network.tsv"
    GO_file = "chicken_GO.gaf"
    uniprot_file = "chicken_uniprot.tsv"



    # read network
    print("create network ...")
    net = GenericNetwork(net_file)
    print("create Map ...")
    map = create_mapping_uniprot(uniprot_file)
    geneMap = map[1] # mapping from uniprot to gene name
    uniprotMap = map[0] # mapping from gene to uniprot id
    print(geneMap.keys())
    print(uniprotMap.keys())


if __name__ == '__main__':
    main()
