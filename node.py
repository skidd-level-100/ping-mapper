# definition for node

class node():

    def __init__(self, relations, id, max_peers):
        self.id = id
        self.relations = relations
        self.chosen_peers = [] # peers this node chose
        self.following_peers = [] # peers that chose this node
        self.patched_peers = [] # unused, will be for when a node detects the next node to be offline so in turn temporarly takes on its chosen peers.
        self.max_peers = max_peers
        


def get_blank_nodes(count, max_peers):
    nodes = []
    for id in range(0,count):
        nodes.append(node([], id, max_peers))
    return nodes
