"""
Tic Tac Toe Player
"""

import math
import copy
import numpy
import sys
import traceback

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total_x_values = 0
    total_o_values = 0

    for values in board:
        for value in values:
            if value == X:
                total_x_values = total_x_values + 1
            elif value == O:
                total_o_values = total_o_values + 1

    return O if total_x_values > total_o_values else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spaces = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_spaces.add((i, j))

    return empty_spaces


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        board_copy = copy.deepcopy(board)
        board_copy[action[0]][action[1]] = player(board)
    except Exception:
        traceback.print_exc(file=sys.stdout)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check center
    if(board[0][1] == board[1][1] == board[2][1]):
        return board[0][1]

    # Check row and columns
    for new_board in [board, numpy.transpose(board)]:
        for row in new_board:
            if len(set(row)) == 1:
                return row[0]

    # Check diagonals
    if len({board[i][i] for i in range(len(board))}) == 1:
        return board[0][0]
    if len({board[i][len(board)-i-1] for i in range(len(board))}) == 1:
        return board[0][len(board)-1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return bool(winner(board) is not None or len(actions(board)) <= 0)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # winning_player = winner(board)
    # if winning_player is None:
    #     return 0

    # return 1 if winning_player is X else -1
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            max_value = findmin(result(board, action))
            if max_value > value:
                value = max_value
                best_move = action
    else:
        value = math.inf
        for action in actions(board):
            min_value = findmax(result(board, action))
            if min_value < value:
                value = min_value
                best_move = action

    return best_move


def findmax(board):
    """
    Get the max value of a move
    """
    if terminal(board):
        return utility(board)

    value = -math.inf

    for action in actions(board):
        value = max(value, findmin(result(board, action)))
        if value == 1:
            return value

    return value


def findmin(board):
    """
    Get the min value of a move
    """
    if terminal(board):
        return utility(board)

    value = math.inf

    for action in actions(board):
        value = min(value, findmax(result(board, action)))
        if value == -1:
            return value

    return value
