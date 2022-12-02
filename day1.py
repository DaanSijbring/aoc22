from utils import read_txt_lines

############################### PART ONE ###########################
data = read_txt_lines('data/day1.txt')

elves = []

elf = []
for line in data:
    if line == '':
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

elves_summed = [sum(elf) for elf in elves]
print(f'Maximum number of calories on an elf: {max(elves_summed)}')

############################### PART TWO ###########################
n = 3
highest = sorted(elves_summed)[-n:]
print(f'Total amount of calories of the three highest scoring elves: {sum(highest)}')