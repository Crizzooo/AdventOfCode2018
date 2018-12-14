import os
import re
from pprint import pprint

#
# C {
#   required_by: [ 'A', 'F' ]
#   prerequisite: []
# },
# A {
#   required_by: ['B', 'D'],
#   prerequisite: ['C']
# }
# B {
# required_by: ['E']
#  prerequisite: ['A']
# }
# D {
#   req_by: ['E']
#   prerequisite: ['A'] 
# }
# E {
#   req_by: []
#   prerequisite: ['B', 'D', 'F' ]
# }
# F {
#   req_by: ['E'],
#   prereq: ['C']
# }
# 

# start = node with no prerequisites
# start = C
# go to first requirement of C
# A
# 

# stack to complete = [ 'F', 'A' ]
#  all A prerequisite is met, so add B D to stack  and take off A

# stack to complete = [ 'F' , 'D', 'B' ]
# CAB have been completed 
# stack = [ 'F', 'D', 'E' ]

# E still requires D
# look backwards through stack and find first with no prerequisites
# CABD
# D - d is now completed
# stack = [ 'F', 'E' ]

# loop backwards and find first with no prerequisites
#  F - f is now completed

# add 'E' to stack
# stack = [ 'E', 'E' ]

# E now has no prerequisites, so remove all occurences of E 
# stack = []

# start with node that has no prerequisites
# add its required elements to the stack in reverse alphabetical order

# process element
# remove element from stack 
# add to final list
# add its required children to stack in reverse order

# while stack has length
    # i = stack length - 1
    # grab last element 
        # if element's requirements have been met
            # process element and continue 
        # else, move backwards 

class Action_Chain:

    action_pattern = re.compile("Step (.*) must be finished before step (.*) can begin.")

    def __init__(self, action_list):
        self.actions = {}
        for instruction in action_list:
            self.process_action(instruction)
        pprint(self.actions)

    # @classmethod
    def process_action(self, action_str):
        # (prerequisite, action) parse action
        (prerequisite, required_by) = Action_Chain.parse_action(action_str)
        if prerequisite not in self.actions:
            self.actions[prerequisite] = self.Action(prerequisite)
        if required_by not in self.actions:
            self.actions[required_by] = self.Action(required_by)
        prerequisite = self.actions[prerequisite]
        required_by = self.actions[required_by]
        # add prerequisite
        prerequisite.add_requirement(required_by)
        required_by.add_prerequisite(prerequisite)

        # add requirement

        pass

    @classmethod
    def parse_action(cls, action_str):
        # return the required step and the prerequisite
        matches = cls.action_pattern.search(action_str)
        if matches is None:
            raise Exception("Action: '" + action_str + "' could not be parsed")
        (prerequisite, required_by) = matches.groups()
        return (prerequisite, required_by)

    class Action():
        def __init__(self, action_name):
            # process action
            self.name = action_name
            self.prerequisites = {}
            self.required_by = {}

        def add_action(self, action, action_type):
            if (action_type not in ['req', 'prereq']):
                raise Exception(action_type, ' is not a valid action type to add')
            if (action_type == 'req'):
                pass
            else:
                pass
                # its a prereq


        def add_requirement(self, requirement):
            self.add_action(requirement, action_type='req')
            pass 

        def add_prerequisite(self, prereq):
            self.add_action(prereq, action_type='prereq')
            pass




def problem_one(action_list):
    chain = Action_Chain(action_list)
    print (Action_Chain.parse_action(action_list[0]))


def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    input = get_file_lines()[0]
    # Uncomment for test Input
    test_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
    input = test_input.split('\n')
    print ('Result: ', problem_one(input))