def read_txt_lines_int(path):
    file = open(path, 'r')
    lines = file.readlines()

    data = []
    for line in lines:
        data.append(int(line.strip()))

    return data

def read_txt_lines(path):
    file = open(path, 'r')
    lines = file.readlines()

    data = []
    for line in lines:
        data.append(line.strip())

    return data

def read_txt_lines_sep(path, seperator):
    file = open(path, 'r')
    lines = file.readlines()

    data = []
    for line in lines:
        data.append(line.strip().split(seperator))

    return data

def read_txt_lines_sep_int(path):
    file = open(path, 'r')
    lines = file.readlines()

    data = []
    for line in lines:
        data.append([int(s) for s in line.strip()])

    return data