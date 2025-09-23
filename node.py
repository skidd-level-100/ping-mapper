# definition for node

class node():

    def __init__(self, relations, id):
        self.id = id
        self.relations = relations
        


def get_blank_nodes(count):
    nodes = []
    for id in range(0,count):
        nodes.append(node([], id))
    return nodes
