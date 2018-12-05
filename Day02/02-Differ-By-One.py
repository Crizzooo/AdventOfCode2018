import os
from pprint import pprint

def find_off_by_one():
    lines = get_file_lines()
    for index, line in enumerate(lines):
        other_lines = lines[index:]
        # O(n^2)
        # compare current line against all other lines
        for second_line in other_lines:
            diff = 0
            for index, char in enumerate(line):
                if second_line[index] is not char:
                    diff += 1
            if (diff == 1):
                final_chars = ""
                for index, char in enumerate(line):
                    if second_line[index] is  char:
                        final_chars += char
                return final_chars

def get_file_lines():
    file_name = os.path.join(os.getcwd(), 'd2-String-input')
    file = open(file_name, "r")
    lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    print("Output: ", find_off_by_one())