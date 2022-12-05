from utils import read_txt_lines

data = read_txt_lines('data/day3.txt')
################# PART ONE ##################
all_priorities = []
for rucksack in data:
    comp1 = rucksack[:len(rucksack)//2]
    comp2 = rucksack[len(rucksack)//2:]
    [common] = list(set(comp1).intersection(comp2))
    if common.isupper():
        all_priorities.append(ord(common) - 64 + 26)
    else:
        all_priorities.append(ord(common) - 96)

print(f'Total: {sum(all_priorities)}')
################# PART TWO ##################
all_priorities = []
for i in range(len(data)//3):
    lb = i * 3
    [badge] = list(set(data[lb]).intersection(data[lb+1], data[lb + 2]))
    if badge.isupper():
        all_priorities.append(ord(badge) - 64 + 26)
    else:
        all_priorities.append(ord(badge) - 96)

print(f'Total: {sum(all_priorities)}')
