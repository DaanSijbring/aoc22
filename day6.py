from utils import read_txt_lines

[data] = read_txt_lines('data/day6.txt')
############### PART ONE ###################
running = ['q', 'q', 'q', 'q']
for i, char in enumerate(data):
    running.pop(0)
    running.append(char)
    if len(list(set(running))) > 3:
        break

print(f'Number of chars needed: {i+1}')
############### PART TWO ###################
running = ['q'] * 14
for i, char in enumerate(data):
    running.pop(0)
    running.append(char)
    if len(list(set(running))) > 13:
        break

print(f'Number of chars needed: {i+1}')