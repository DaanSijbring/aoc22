from utils import read_txt_lines

data = read_txt_lines('data/day4.txt')
################# PART ONE ##################
fully_comprised = 0
for pair in data:
    elf_ranges = [list(range(int(elf.split('-')[0]), int(elf.split('-')[1])+1)) for elf in pair.split(',')]
    if set(elf_ranges[0]).issubset(set(elf_ranges[1])) or set(elf_ranges[1]).issubset(set(elf_ranges[0])):
        fully_comprised += 1

print(f'Number of fully encompassed lists: {fully_comprised}')
################# PART TWO ##################
partial_overlap = 0
for pair in data:
    elf_ranges = [list(range(int(elf.split('-')[0]), int(elf.split('-')[1])+1)) for elf in pair.split(',')]
    if bool(set(elf_ranges[0]) & set(elf_ranges[1])):
        partial_overlap += 1

print(f'Number of partial overlaps: {partial_overlap}')