from node import *;
from synthetic_data import *;
#synth data

#0 | [[1, 4], [4, 146], [2, 160], [7, 242], [5, 364], [3, 382], [8, 382], [9, 452], [6, 524]]
#1 | [[0, 4], [4, 142], [2, 164], [7, 238], [5, 368], [3, 386], [8, 386], [9, 456], [6, 528]]
#2 | [[0, 160], [1, 164], [5, 204], [3, 222], [8, 222], [9, 292], [4, 306], [6, 364], [7, 402]]
#3 | [[8, 0], [5, 18], [9, 70], [6, 142], [2, 222], [0, 382], [1, 386], [4, 528], [7, 624]]
#4 | [[7, 96], [1, 142], [0, 146], [2, 306], [5, 510], [3, 528], [8, 528], [9, 598], [6, 670]]
#5 | [[3, 18], [8, 18], [9, 88], [6, 160], [2, 204], [0, 364], [1, 368], [4, 510], [7, 606]]
#6 | [[9, 72], [3, 142], [8, 142], [5, 160], [2, 364], [0, 524], [1, 528], [4, 670], [7, 766]]
#7 | [[4, 96], [1, 238], [0, 242], [2, 402], [5, 606], [3, 624], [8, 624], [9, 694], [6, 766]]
#8 | [[3, 0], [5, 18], [9, 70], [6, 142], [2, 222], [0, 382], [1, 386], [4, 528], [7, 624]]
#9 | [[3, 70], [8, 70], [6, 72], [5, 88], [2, 292], [0, 452], [1, 456], [4, 598], [7, 694]]

from operator import itemgetter 


def aquire_best_peers(nodes):

    all_relations = []
    for node in nodes:
        all_relations.append(node.relations)

    total_relations_in_each_list = len(all_relations) - 1 # nodes dont inculde themselfs  in their relations so the list size is one less

    for relation_layer_index in range(0,total_relations_in_each_list):

        for node_id in range(0,len(nodes)):
            winner = who_gets(node_id, relation_layer_index, all_relations, nodes)
            if winner != False:
                nodes[winner].chosen_peers.append(node_id)
                nodes[node_id].following_peers.append(winner)


    # patch the holes!
    for node in nodes:
        counter = 0
        while len(node.following_peers) < node.max_peers / 2:
            if node.relations[counter][0] not in node.following_peers + node.chosen_peers:
                node.following_peers.append(node.relations[counter][0])
                nodes[node.relations[counter][0]].chosen_peers.append(node.id)
            counter += 1

        counter = 0
        while len(node.chosen_peers) < node.max_peers / 2:
            if node.relations[counter][0] not in node.following_peers + node.chosen_peers:
                node.chosen_peers.append(node.relations[counter][0])
                nodes[node.relations[counter][0]].following_peers.append(node.id)
            counter += 1


def who_gets(wanted_node_id, relation_layer_index, all_relations, nodes):
    wanters = []


    for node_id,relation in enumerate(all_relations):
        if relation[relation_layer_index][0] == wanted_node_id:
            
            if relation_layer_index < len(relation) - 1:
                relation_layer_index_next = relation_layer_index + 1
            else:
                relation_layer_index_next = relation_layer_index

            if len(nodes[wanted_node_id].following_peers) < (nodes[wanted_node_id].max_peers / 2):
                if wanted_node_id not in nodes[node_id].chosen_peers + nodes[node_id].following_peers and len(nodes[node_id].chosen_peers) < (nodes[node_id].max_peers / 2):
                    want_level = relation[relation_layer_index_next][1] - relation[relation_layer_index][1]
                    wanters.append([node_id, want_level])

    wanters.sort(key = itemgetter(1), reverse=True)
    if wanters:
        return wanters[0][0]
    else:
        return False

def main():
    # mock peers test
    nodes = get_blank_nodes(500, 4)
    set_relations(nodes) # in practice replace this with your own peer scoring function, sort the list from best(score 0) to worst (very high score(ping)) [[node  id, score],[node  id, score],etc]
    aquire_best_peers(nodes)

    print("\nwho connects to who (node id, (input peers, output peers))")
    print("HINT: output to input peers if information comes from output peers")
    for index,node in enumerate(nodes):
        print(f"    node id: {index} | input peers: {node.following_peers} | output peers: {node.chosen_peers}")

if __name__ == '__main__':
    main()