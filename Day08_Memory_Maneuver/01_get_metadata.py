import os
from pprint import pprint
# from itertools import accumulate
from functools import reduce

# rather than recurse through our tree after creation
# we can store metadata  in our global list, and sum this up later 
all_metadata = []

# Problem 1 - returns list of reaction string after performing all reactions
def get_meta_data(input): 
    data = input.split()
    # start a tree that will parse all children until there is no data left
    start_node = Node(data)
    metadata_sum = reduce( (lambda total_sum, curr: total_sum + curr), all_metadata )
    # Problem 1 return metadata_sum
    # Problem 2 - get root node value
    return start_node.get_node_value()

class Node:

    total_nodes = 0

    def __init__(self, data):
        # Start Children with empty placeholder to be able to directly plug in metadata indexes for problem 2
        self.children = [ None ]
        self.metadata = []
        self.child_count = int(data.pop(0))
        self.metadata_count = int(data.pop(0))
        Node.total_nodes += 1
        self.node_id = Node.total_nodes
 
        if (len(data) > 0):
            self.process_remaining_nodes(data)
    
    def __str__(self):
        return "child_count " + str(self.child_count) + " " + str(len(self.children)) + " metadata_count " + str(self.metadata_count) + " " + str(len(self.metadata))

    def process_remaining_nodes(self, data):
        global all_metadata
        # while there is a child count, process the child 
        while len(self.children) <= self.child_count and len(data):
            node = Node(data)
            self.children.append(node)
        # then update metadata
        while (len(self.metadata) < self.metadata_count):
            self.metadata.append(int(data.pop(0)))
        all_metadata.extend(self.metadata)

    def get_node_value(self):
        value = 0
        # if no children, a node's value is the sum of its metadata
        if (len(self.children) == 1):
            return sum(self.metadata)
        # else the node should use its metadata as indexes of its children
        # and if a child node exists at that index, it should aggregate the indexes
        for child in [self.children[index] for index in self.metadata if index < len(self.children)]:
            # for each metadata, if child node exists at that index - get its child's value
            value +=  child.get_node_value()
        return value


def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    input = get_file_lines()[0]
    # Uncomment for test Input
    # input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    print ('Result: ', get_meta_data(input))