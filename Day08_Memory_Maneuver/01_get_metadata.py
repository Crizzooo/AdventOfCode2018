import os
from pprint import pprint
# from itertools import accumulate
from functools import reduce

# rather than recurse through our tree after creation
# we can store metadata  in our global list, and sum this up later 
all_metadata = []

# Problem 1 - returns list of reaction string after performing all reactions
def get_meta_data(input): 
    print(input)
    data = input.split()
    # start a tree that will parse all children until there is no data left
    start_node = Node(data)
    # pprint(all_metadata)

    metadata_sum = reduce( (lambda total_sum, curr: total_sum + curr), all_metadata )
    # return metadata_sum
    return start_node.get_node_value()
    # starting with the start_node, go through all children and get their sums



class Node:

    total_nodes = 0

    def __init__(self, data):
        self.children = [ None ]
        self.metadata = []
        self.child_count = int(data.pop(0))
        self.metadata_count = int(data.pop(0))
        Node.total_nodes += 1
        self.node_id = Node.total_nodes
        # print ('processing node number', self.node_id)
  
        # print ('found child count and metadata for node: ', self.node_id, self.child_count, self.metadata_count)
        # print(len(data))
        if (len(data) > 0):
            self.process_remaining_nodes(data)
        # print ("Done with node", self.node_id)
        # print(self)
        # TODO: Calculate 'value' of this node 
            # go get the value of all children
                # metadata is reference to index of where the child is
                # so plug in the metadata - 1 to children array to find its child
                # or we can initiate children array with None 
                # if a node has no children, its value is the sum of its metadata
        pass
    
    def __str__(self):
        return "child_count " + str(self.child_count) + " " + str(len(self.children)) + " metadata_count " + str(self.metadata_count) + " " + str(len(self.metadata))

    def process_remaining_nodes(self, data):
        global all_metadata
        # while there is a child count, process the child 
        while len(self.children) <= self.child_count and len(data):
            # print ('making child for node id: ', self.node_id)
            node = Node(data)
            self.children.append(node)
        # then update metadata
        while (len(self.metadata) < self.metadata_count):
            # print ('pre metadata removal', len(data))
            self.metadata.append(int(data.pop(0)))
        #     print ('post metadata removal', len(data))
        # print ('found metadata for node: ', self.node_id)
        pprint(self.metadata)
        pprint(self.children)
        all_metadata.extend(self.metadata)
        # print ('child length and children', self.child_count, len(self.children))
    def get_node_value(self):
        value = 0
        # found_child = False
        if (len(self.children) == 1):
            return sum(self.metadata)
        # loop through metadata
        for index in self.metadata:
            # for each metadata, if child node exists at that index
            if index < len(self.children):
                child = self.children[index]
                # found_child = True 
                # aggregate its value
                print('getting node value of child', child.node_id)
                value = value +  child.get_node_value()
        return value


def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    input = get_file_lines()[0]
    # Testing
    # input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    print ('Result: ', get_meta_data(input))