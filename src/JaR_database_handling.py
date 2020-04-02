import sys

# --------------------------------------------------------------
# The structure of the tree:

def getNode(nodeID):
    with open('main_graph.json') as json_file:
        data = json.load(json_file)
    return data[nodeID]
