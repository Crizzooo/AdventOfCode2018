import os
from pprint import pprint
from functools import reduce


def get_repeated_frequency():
    total = 0
    commands = get_file_lines()

    previous_frequencies = set()
    # continually process commands
    while (True):
        for command in commands:
            total = add_command_to_total(total, command)
            # if total is in set, return that total
            if (total in previous_frequencies): 
                return total
            # store all possible totals 
            previous_frequencies.add(total)

def add_command_to_total(total, command):
    operation = command[0]
    number = int(command[1:])
    if (operation == "+"):
        total += number
    else:
        total -= number
    return total

def reduce_total(total, command):
    return add_command_to_total(total, command)

def get_file_lines():
    file_name = os.path.join(os.getcwd(), '01-Frequency-input')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    print("Output: ", get_repeated_frequency())