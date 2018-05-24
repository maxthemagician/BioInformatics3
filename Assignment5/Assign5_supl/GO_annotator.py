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


def findGoTerms(file):
    goterms = {}
    f = open(file, 'r')
    for line in f:
        if line.__len__() == 0:
            continue
        if not line.startswith('UniProtKB'):
            continue
        line = line.split('\t')
        if line[8] != 'P':
            continue
        term = line[4]
        gene = line[2]
        if goterms.get(gene) is not None:
            s = goterms.get(gene)
            s.append(term)
            goterms[gene] = s
        else:
            goterms[gene] = [term]
    return goterms


def overview(net):
    num_prot = net.size()
    num_interact = 0
    unique_GO = set()
    all_GO = []
    empty = 0
    high = 0
    small = 10000000000

    for i in net.nodes:
        n = net.getNode(i)
        num_interact += n.degree()
        if n.go_terms.__len__() == 0:
            empty += 1
        if n.go_terms.__len__() > high:
            high = n.go_terms.__len__()
        if n.go_terms.__len__() < small:
            small = n.go_terms.__len__()
        for j in n.go_terms:
            unique_GO.add(j)
            all_GO.append(j)
    num_interact = int(num_interact/2)
    empty_per = empty/num_prot * 100
    avg = all_GO.__len__()/num_prot
    h_GO = 0
    s_GO = 10000000000
    a_GO = all_GO.__len__()/unique_GO.__len__()
    for i in unique_GO:
        c = all_GO.count(i)
        if c < s_GO:
            s_GO = c
        if c > h_GO:
            h_GO = c


    print('Number of Proteins: ' + num_prot.__str__())
    print('Number of Interactions: ' + num_interact.__str__())
    print('Number of unique GO annotations: ' + unique_GO.__len__().__str__())
    print('Number of Proteins without any GO annotations: ' + empty.__str__() + "  ->  " + empty_per.__str__() + "%")
    print('Smallest, average, highest number of GO annotations per  protein:        ' + small.__str__() + ", " + avg.__str__() + ', '+ high.__str__())
    print('Smallest, average, highest number of proteins       per  GO annotations: ' + s_GO.__str__() + ", " + a_GO.__str__() + ', '+ h_GO.__str__())


def workflow(net_file, GO_file, uniprot_file):
    # read network
    #print("create network ...")
    net = GenericNetwork(net_file)

    # create mapping
    #print("create mappings ...")
    map = create_mapping_uniprot(uniprot_file)
    geneMap = map[1]  # mapping from uniprot to gene name
    uniprotMap = map[0]  # mapping from gene to uniprot id
    GO_terms = findGoTerms(GO_file)
    #print('map GO terms to network ...')
    for i in net.nodes:
        n = net.getNode(i)
        # get possible other gene names out of mapping
        if uniprotMap.get(n.id) is not None:
            pos = uniprotMap[n.id]
            res = set()
            for entry in pos:
                s = geneMap[entry]
                for e in s:
                    res.add(e)
        else:
            continue
        # find all goterms
        go = set()
        for gene in res:
            if GO_terms.get(gene) is not None:
                terms = GO_terms[gene]
                for i in terms:
                    go.add(i)

        for i in go:
            n.addGO(i)

    overview(net)
    return net


def getMostLeast(net, k):
    # get least anf most n annotations
    GO = {}
    all_GO = []
    for i in net.nodes:
        n = net.getNode(i)
        for j in n.go_terms:
            GO[j] = 0
            all_GO.append(j)

    for i in all_GO:
        GO[i] = GO[i] + 1

    l = sorted(GO, key=GO.get, reverse=True)
    print('Most common: ')
    most = []
    i = 0
    while i < k:
        temp = [l[i], GO[l[i]]]
        temp_list = [[l[i], GO[l[i]]]]
        j = i
        while temp[1] == GO[l[j+1]]:
            temp_list.append([l[j+1], GO[l[j+1]]])
            j += 1
        s = sorted(temp_list)
        sc = 0
        while (most.__len__() < k) & (sc < s.__len__()) :
            most.append(s[sc])
            sc += 1
        i = most.__len__()

    print(most)

    print('Least common: ')
    l = sorted(GO, key=GO.get, reverse=False)
    least = []
    i = 0
    while i < k:
        temp = [l[i], GO[l[i]]]
        temp_list = [[l[i], GO[l[i]]]]
        j = i
        while temp[1] == GO[l[j+1]]:
            temp_list.append([l[j+1], GO[l[j+1]]])
            j += 1
        s = sorted(temp_list)
        sc = 0
        while (least.__len__() < k) & (sc < s.__len__()) :
            least.append(s[sc])
            sc += 1
        i = least.__len__()

    print(least)


def binomial(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def main():
    net_files = ["chicken_network.tsv", "pig_network.tsv", "human_network.tsv"]
    GO_files = ["chicken_GO.gaf", "pig_GO.gaf", "human_GO.gaf"]
    uniprot_files = ["chicken_uniprot.tsv", "pig_uniprot.tsv", "human_uniprot.tsv"]

    for i in range(3):
        name = net_files[i].split('_')[0]
        print('\nSummary for ' + name + ':\n')
        net = workflow(net_files[i], GO_files[i], uniprot_files[i])
        if(i == 2):     # at humans
            getMostLeast(net, 5)


if __name__ == '__main__':
    main()
