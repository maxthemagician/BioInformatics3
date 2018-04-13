class Node:
    def __init__(self, identifier):
        """
        Sets node id and initialize empty node list that references its connected nodes
        """
        self.id = identifier
        self.nodes = {}
        
    def hasLinkTo(self, node):
        """
        Returns True if this node is connected to node asked for,
        False otherwise
        """
        return node in self.nodes

    def addLinkTo(self, node):
        """
        Adds link from this node to parameter node (only if there is no link connection already),
        does not automatically care for a link from parameter node to this node
        """
        if not (self.hasLinkTo(node)):
            self.nodes[node.id] = node

    def degree(self):
        """
        Returns degree of this node
        """
        return self.nodes.__len__()

    def __str__(self):
        """
        Returns id of node as string
        """
        return self.id
