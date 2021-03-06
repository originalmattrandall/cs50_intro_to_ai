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
    available_moves = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available_moves.add((i, j))

    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        board_copy = copy.deepcopy(board)
        board_copy[action[0]][action[1]] = player(board)
    except Exception as error:
        print(error)
        traceback.print_exc(file=sys.stdout)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

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
    # return False if winner(board) is None else True
    return not winner(board) is None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player is None:
        return 0

    return 1 if winning_player is X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            max_value = minmove(result(board, action))
            if max_value > value:
                value = max_value
                best_move = action
    else:
        value = math.inf
        for action in actions(board):
            min_value = maxmove(result(board, action))
            if min_value < value:
                value = min_value
                best_move = action

    return best_move


def maxmove(board):
    """
    Get the max value of a move
    """
    if terminal(board):
        return utility(board)

    value = -math.inf

    for action in actions(board):
        value = max(value, minmove(result(board, action)))

    return value


def minmove(board):
    """
    Get the min value of a move
    """
    if terminal(board):
        return utility(board)

    value = math.inf

    for action in actions(board):
        value = min(value, maxmove(result(board, action)))

    return value
