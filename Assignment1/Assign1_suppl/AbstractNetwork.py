class AbstractNetwork:
    """Abstract network definition, can not be instantiated"""
    
    def __init__(self, amount_nodes, amount_links):
        """
        Creates empty nodelist and call createNetwork of the extending class
        """
        self.nodes = {}
        self.maxDegree = 0
        self.__createNetwork__(amount_nodes, amount_links)

    def __createNetwork__(self, amount_nodes, amount_links):
        """
        Method overwritten by subclasses, nothing to do here
        """
        raise NotImplementedError

    def appendNode(self, node):
        """
        Appends node to network
        """
        self.nodes[node.id] = node
        if(self.maxDegree < node.degree()):
            self.maxDegree = node.degree()

    def maxDegree(self):
        """
        Returns the maximum degree in this network
        """
        return self.maxDegree

    def size(self):
        """
        Returns network size (here: number of nodes)
        """
        return self.nodes.__len__()

    def __str__(self):
        '''
        Any string-representation of the network (something simply is enough)
        '''
        s = ""
        for node in self.nodes:
            s = s + "{ " + str(node) + " }"
            s = s + " -> { "
            for k in self.nodes[node].nodes:
                s = s + str(k) + " "
            s = s + "}\n"
        return s

    def getNode(self, identifier):
        """
        Returns node according to key
        """
        return self.nodes[identifier]
