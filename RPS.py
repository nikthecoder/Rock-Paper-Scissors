import random

opponent_moves = []
known_patterns = {}

def player(my_move, opponent_history=[]):
    if my_move:
        opponent_history.append(my_move)

    n = 5
    opponent_moves.extend(opponent_history)

    guess = "R"
    if len(opponent_moves) > n:
        pattern = join(opponent_moves[-n:])

        if join(opponent_moves[-(n + 1):]) in known_patterns.keys():
            known_patterns[join(opponent_moves[-(n + 1):])] += 1
        else:
            known_patterns[join(opponent_moves[-(n + 1):])] = 1

        possible_moves = [pattern + "R", pattern + "P", pattern + "S"]

        for move in possible_moves:
            if move not in known_patterns.keys():
                known_patterns[move] = 0

        predicted_pattern = max(possible_moves, key=lambda move: known_patterns[move])

        if predicted_pattern[-1] == "P":
            guess = "S"
        if predicted_pattern[-1] == "R":
            guess = "P"
        if predicted_pattern[-1] == "S":
            guess = "R"

    return guess

def join(moves):
    return "".join(moves)

