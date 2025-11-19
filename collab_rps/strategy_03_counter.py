import random

NAME = "Strategy 3 - Counter"

def move(opponent_last_move):

    # first round - opponent won't have a last move
    if opponent_last_move is None:
        choices = ["R", "P", "S"]
        return random.choice(choices)

    # counter the opponent's last move
    # P beats R, R beats S, S beats P
    if opponent_last_move == "R":
        return "P"
    elif opponent_last_move == "P":
        return "S"
    elif opponent_last_move == "S":
        return "R"

    # in case the opponent did a goofy move
    return "R"
