import os
import string
from pprint import pprint

# Problem 1 - returns list of reaction string after performing all reactions
def perform_reaction(str): 
    i = 0
    chars = list(str)
    # when a reaction is determined, remove both characters and move index to the previous
    while i < len(chars) - 1:
        curr_char = chars[i]
        next_char = chars[i+1]
        if (is_reaction(curr_char, next_char)):
            chars.pop(i + 1)
            chars.pop(i)
            i = i - 1 
            if (i < 0):
                i = 0
        else:
            i = i + 1
    return len(''.join(chars))

# Problem 2 - get shortest reaction string when one unit is removed
# iterate over alphabet, removing all occurences of a pair
# store the result of the reaction after each removal
# return which removal led to the shortest remaining chain
def get_minimum_reaction(input):
    alphabet = list(string.ascii_lowercase)
    min_count = len(input)
    for char in alphabet:
        # replace all occurences  of the lower and upper case character
        reaction = input.replace(char, '')
        reaction = reaction.replace(char.upper(), '')
        count = perform_reaction(reaction)
        if (count < min_count):
            min_count = count
    return min_count

def is_reaction(charA, charB):
    if charA == charB:
        return False 
    if charA.upper() == charB:
        return True
    if charA.lower() == charB:
        return True
    return False

def get_file_lines():
    file_name = os.path.join(os.getcwd(), '05-input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    input = get_file_lines()[0]
    print ('Result: ', get_minimum_reaction(input))