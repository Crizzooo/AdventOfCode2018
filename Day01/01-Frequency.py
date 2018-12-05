import os
from pprint import pprint
from functools import reduce

def calculate_frequencies():
    commands = get_file_lines()
    # process each command
    return reduce(reduce_total, commands, 0)

def reduce_total(total, command):
    operation = command[0]
    number = int(command[1:])
    if (operation == "+"):
        total += number
    else:
        total -= number
    return total

def get_file_lines():
    file_name = os.path.join(os.getcwd(), '01-Frequency-input')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    print("Output: ", calculate_frequencies())