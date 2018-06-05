# Node class, assignment 1
class BooleanNode:
    def __init__(self, identifier):
        """
        Sets node id and initialize empty node list that references its connected nodes
        """
        self.id = identifier
        self.nodelist = []
        self.state = 0

