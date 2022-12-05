from utils import read_txt_lines
###################### PART ONE ##################
base_scores = {
    'X': 1,     # ROCK
    'Y': 2,     # PAPER
    'Z': 3      # SCISSORS
}

game_outcomes = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

file = open('data/day2.txt', 'r')
lines = file.readlines()

data = []
for line in lines:
    data.append(line.strip().split(' '))

game_scores = []
for game in data:
    base_score = base_scores[game[1]]
    game_outcome = game_outcomes[game[0]+game[1]]

    game_scores.append(base_score + game_outcome)

print(f'Total score: {sum(game_scores)}')

###################### PART TWO ##################
game_dict = {
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    },
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
}

game_outcomes2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}


game2_scores = []
for game in data:
    game_outcome = game_outcomes2[game[1]]
    hand_to_play = game_dict[game[1]][game[0]]
    base_score = base_scores[hand_to_play]

    game2_scores.append(base_score + game_outcome)

print(f'Total score for game 2: {sum(game2_scores)}')