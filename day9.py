from utils import read_txt_lines_sep
import math

data = read_txt_lines_sep('data/day9.txt', ' ')


def touching(head, tail):
    """
    Functions that takes two Cartesian coordinates and determines if they are touching.
    D = (x2 - x1)^2 + (y2 - y1)^2
    :param head: Cartesian coordinates for the head of the rope.
    :param tail: Cartesian coordinates for the tail of the rope.
    :return: bool
    """
    distance = pow(abs(head[0] - tail[0]), 2) + pow(abs(head[1] - tail[1]), 2)

    if distance <= 2:
        return True
    else:
        return False

def calculate_distance(head, tail):
    """
    Functions that takes two Cartesian coordinates and calculates the Cartesian distance.
    D = (x2 - x1)^2 + (y2 - y1)^2
    :param head: Cartesian coordinates for the head of the rope.
    :param tail: Cartesian coordinates for the tail of the rope.
    :return: int denoting distance between two coordinates.
    """
    return pow(abs(head[0] - tail[0]), 2) + pow(abs(head[1] - tail[1]), 2)


def move_step(coordinate, dir):
    """
    Updates a Cartesian coordinate one step in a direction.
    :param coordinate: Cartesian starting coordinate
    :param dir: string containing 'R', 'L', 'U', or 'D'
    :return: updated Cartesian coordinate
    """
    match dir:
        case 'R':
            return coordinate[0] + 1, coordinate[1]
        case 'L':
            return coordinate[0] - 1, coordinate[1]
        case 'U':
            return coordinate[0], coordinate[1] - 1
        case 'D':
            return coordinate[0], coordinate[1] + 1

def diagonal_step(head, tail):
    """
    Head and tail have a Cartesian distance of 5. Updates tail coordinates diagonally to up-left, up-right,
    bottom-left, or bottom-right
    :param head: Cartesian coordinate for the head of the rope.
    :param tail: Cartesian coordinate for the tail of the rope.
    :return: Updated Cartesian coordinates for the tail.
    """
    new_tail = tail
    if head[0] > tail[0]:
        new_tail = (new_tail[0] + 1, new_tail[1])
    else:
        new_tail = (new_tail[0] - 1, new_tail[1])

    if head[1] > tail[1]:
        new_tail = (new_tail[0], new_tail[1] + 1)
    else:
        new_tail = (new_tail[0], new_tail[1] - 1)

    return new_tail
###### PART ONE ########
verbose = False
dim = 1000
starting_position = (int(dim/2), int(dim/2))
head_coordinates = starting_position
tail_coordinates = starting_position

tail_log = [tail_coordinates]
for [direction, distance] in data:

    for step in range(int(distance)):
        new_head_coordinates = move_step(head_coordinates, direction)
        if verbose: print(f'Head: {head_coordinates} -> {new_head_coordinates}')
        head_coordinates = new_head_coordinates

        rope_len = calculate_distance(head_coordinates, tail_coordinates)
        if verbose: print(f'Distance now: {rope_len}')
        if rope_len > 3:
            if rope_len == 4:
                # Head and tail are in same column/row, but with excessive distance.
                new_tail_coordinates = move_step(tail_coordinates, direction)
            if rope_len == 5:
                # Head and tail are diagonally spaced apart.
                new_tail_coordinates = diagonal_step(head_coordinates, tail_coordinates)

            if verbose: print(f'Tail: {tail_coordinates} - {new_tail_coordinates}')
            tail_log.append(new_tail_coordinates)
            tail_coordinates = new_tail_coordinates

        if verbose: print('')

print(f'Number of locations the tail visited: {len(set(tail_log))}')

###### PART TWO ########
verbose = False
dim = 1000
starting_position = (int(dim/2), int(dim/2))
num_knots = 10
rope_coordinates = [starting_position for i in range(num_knots)]

tail_log = [starting_position]
for [direction, distance] in data:

    for step in range(int(distance)):

        for num_knot in range(num_knots):
            if num_knot == 0:
                new_head_coordinates = move_step(rope_coordinates[0], direction)
                if verbose: print(f'Head: {rope_coordinates[0]} -> {new_head_coordinates}')
                rope_coordinates[0] = new_head_coordinates
                continue

            knot_distance = calculate_distance(rope_coordinates[num_knot-1], rope_coordinates[num_knot])
            if knot_distance > 3:
                if knot_distance == 4:
                    new_knot_coordinates = move_step(rope_coordinates[num_knot], direction)
                # if knot_distance == 5 or knot_distance == 8:
                if knot_distance > 4:
                    new_knot_coordinates = diagonal_step(rope_coordinates[num_knot-1], rope_coordinates[num_knot])

                if num_knot == num_knots - 1:
                    if verbose: print(f'Tail: {rope_coordinates[num_knot]} - {new_knot_coordinates}')
                    tail_log.append(new_knot_coordinates)
                else:
                    if verbose: print(f'Knot #{num_knot}: {rope_coordinates[num_knot]} - {new_knot_coordinates}')

                rope_coordinates[num_knot] = new_knot_coordinates

        if verbose: print('')


print(f'Number of locations the tail visited: {len(set(tail_log))}')
