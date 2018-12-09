import os
import re
from pprint import pprint

FABRIC_SIZE = 1000

def get_fabric_overlap():
    # create fabric data structure of 1000 x 1000 cells
    fabric = create_fabric()
    commands = get_file_lines()
    pprint(commands)
    cuts = map( lambda x: CutInstruction(x), commands)
    overlaps = 0
    # place cut in fabric
    for cut in cuts:
        # process the command and update the board
        cut_overlaps = put_cut_in_fabric(cut, fabric)
        # update overlap count
        overlaps += cut_overlaps

    # Answer 2 - do 1 more pass and find the only cut with no overlaps
    for cut in cuts:
        has_overlaps = determine_if_overlaps(cut, fabric)
        if (has_overlaps is False):
            print('no overlaps?', cut.id)
        # update overlap count
        overlaps += cut_overlaps

    return overlaps

def put_cut_in_fabric(cut, fabric):
    x, y = cut.start_coords
    # start for loop from the x coordinate and go up to x + width
    overlaps = 0
    for yy in range(int(y), int(y) + int(cut.height)):
        for xx in range(int(x), int(x) + int(cut.width)):
            curr_val = fabric[yy][xx]
            if curr_val == '.':
                fabric[yy][xx] = cut.id
            elif curr_val == 'XXX':
                pass
            else:
                fabric[yy][xx] = 'XXX'
                overlaps += 1
    return overlaps

def determine_if_overlaps(cut, fabric):
    x, y = cut.start_coords
    # start for loop from the x coordinate and go up to x + width
    for yy in range(int(y), int(y) + int(cut.height)):
        for xx in range(int(x), int(x) + int(cut.width)):
            curr_val = fabric[yy][xx]
            if curr_val == 'XXX':
                return True
    return False
    

def create_fabric():
    board = []
    # use size + 1 so that we can directly use the input commands and not worry about ranges
    # our fabric will have an extra row and an extra column that will notbe used by the inputs
    for _ in range(0, FABRIC_SIZE + 1):
        row = []
        for _ in range(0, FABRIC_SIZE + 1):
            row.append('.')
        board.append(row)
    return board

# digest the input line in to a class with all information to process a cut
class CutInstruction:
    def __init__(self, command):
        (elf_id, start_coords, cut_size) = self.get_command_pieces(command)
        self.id = elf_id
        self.start_coords = start_coords.split(',')
        ( width, height ) = cut_size.split('x')
        self.width = width
        self.height = height

    def get_command_pieces(self, command):
        command = command.replace('@', '')
        command = command.replace(':', '')
        command = re.sub(' +', ' ', command)
        return command.split(' ')

def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'input.txt')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    print('Result: ', get_fabric_overlap())