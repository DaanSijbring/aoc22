from utils import read_txt_lines_sep_int
from copy import deepcopy

data = read_txt_lines_sep_int('data/day8.txt')
vis = 0
for i in range(len(data)):
    if (i+1) == 1 or (i+1) == len(data):
        vis += 99
        continue

    for j in range(len(data)):
        if (j+1) == 1 or (j+1) == len(data):
            vis += 1
            continue

        cur_tree = data[i][j]

        row_left = data[i][0:j]
        row_right = data[i][j+1:]
        col_up = [row[j] for row in data][0:i]
        col_down = [row[j] for row in data][i+1:]
        if cur_tree > max(row_left) or cur_tree > max(row_right) or cur_tree > max(col_up) or cur_tree > max(col_down):
            vis += 1


print(f'Total number of visible trees: {vis}')


########## PART TWO ##############
def traverse(height, tree_list):
    view_distance = 0
    for tree in tree_list:
        view_distance += 1
        if tree >= height:
            break
    return view_distance


max = 0
for i in range(len(data)):
    if (i+1) == 1 or (i+1) == len(data):
        continue
    for j in range(len(data)):
        if (j + 1) == 1 or (j + 1) == len(data):
            continue

        cur_tree = data[i][j]
        row_left = data[i][0:j]
        row_left.reverse()
        row_right = data[i][j + 1:]
        col_up = [row[j] for row in data][0:i]
        col_up.reverse()
        col_down = [row[j] for row in data][i + 1:]

        viewing_distance = traverse(cur_tree, row_left) * traverse(cur_tree, row_right) * traverse(cur_tree, col_up) * traverse(cur_tree, col_down)
        if viewing_distance > max:
            max = viewing_distance

print(f'Highest scenic score: {max}')