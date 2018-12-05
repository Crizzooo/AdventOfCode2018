import os
from pprint import pprint
from functools import reduce


def calculate_checksum():
    lines = get_file_lines()
    double_count = 0
    triple_count = 0
    for line in lines:
        chars = { }
        for char in line:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        is_double = False 
        is_triple = False 
        for key, total in chars.items():
            if total == 2:
                is_double = True 
            if total == 3:
                is_triple = True 
        if (is_double):
            double_count += 1
        if (is_triple):
            triple_count += 1
    print (double_count * triple_count)

def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'd2-String-input')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    print("Output: ", calculate_checksum())