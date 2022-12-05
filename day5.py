from utils import read_txt_lines
import re

data = read_txt_lines('data/day5.txt')
config = [
    ['C','Z','N','B','M','W','Q','V'],
    ['H','Z','R','W','C','B'],
    ['F','Q','R','J'],
    ['Z','S','W','H','F','N','M','T'],
    ['G','F','W','L','N','Q','P'],
    ['L','P','W'],
    ['V','B','D','R','G','C','Q','J'],
    ['Z','Q','N','B','W'],
    ['H','L','F','C','G','T','J']
]
instructions = data[10:]

############### PART ONE ##############
for instruction in instructions:
    nums = [int(num) for num in re.findall(r'\d+', instruction)]
    idx_from = nums[1] - 1
    idx_to = nums[2] - 1
    num_to_move = nums[0]

    list_from = config[idx_from]
    list_to = config[idx_to]

    items_to_move = list_from[len(list_from)-num_to_move:]
    new_list_to = list_to + list(reversed(items_to_move))
    new_list_from = list_from[:len(list_from)-num_to_move]

    config[idx_from] = new_list_from
    config[idx_to] = new_list_to

tops = ''.join([ls[-1] for ls in config])

print(f'Answer: {tops}')
########## PART TWO ###########
config = [
    ['C','Z','N','B','M','W','Q','V'],
    ['H','Z','R','W','C','B'],
    ['F','Q','R','J'],
    ['Z','S','W','H','F','N','M','T'],
    ['G','F','W','L','N','Q','P'],
    ['L','P','W'],
    ['V','B','D','R','G','C','Q','J'],
    ['Z','Q','N','B','W'],
    ['H','L','F','C','G','T','J']
]
for instruction in instructions:
    nums = [int(num) for num in re.findall(r'\d+', instruction)]
    idx_from = nums[1] - 1
    idx_to = nums[2] - 1
    num_to_move = nums[0]

    list_from = config[idx_from]
    list_to = config[idx_to]

    items_to_move = list_from[len(list_from)-num_to_move:]
    new_list_to = list_to + items_to_move
    new_list_from = list_from[:len(list_from)-num_to_move]

    config[idx_from] = new_list_from
    config[idx_to] = new_list_to

tops = ''.join([ls[-1] for ls in config])

print(f'Answer: {tops}')