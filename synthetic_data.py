from synth_settings import * # gets max_distance and ping_per_unit
from node import node,get_blank_nodes # gets node class
import random #duh
from operator import itemgetter 


def set_relations(nodes):

    locations = []
    for node in nodes:
        locations.append(random.randint(1,max_distance))
    
    for current_node in nodes:
        relation = []
        for index in range(0,len(nodes)):
            if index != current_node.id:
                score = abs(locations[index] - locations[current_node.id]) * ping_per_unit
                relation.append([index,score])
        relation.sort(key=itemgetter(1))
        current_node.relations = relation
        


if __name__ == '__main__':
    # test
    nodes = get_blank_nodes(10)
    set_relations(nodes)

    for node in nodes:
        print(f"{node.id:} | {node.relations}")