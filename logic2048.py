import numpy as np
from numpy import zeros, array, rot90
from random import randint, random


class board_2048():
    def __init__(self):
        self.board = zeros((4, 4), dtype = np.int)
        self.game_over = False
    
    def move(self, direction):
        pass

    def is_game_over(self):
        pass


def fill_cell(board):
    i, j = (board == 0).nonzero()
    if i.size != 0:
        rnd = randint(0, i.size - 1)
        board[i[rnd], j[rnd]] = 2 * ((random() > .8) + 1)


def move_left(col):
    new_col = zeros((4), dtype=col.dtype)
    j = 0
    previous = None
    for i in range(col.size):
        if col[i] != 0:
            if previous == None:
                previous = col[i]
            else: 
                if previous == col[i]:
                    new_col[j] = 2 * col[i]
                    j += 1
                    previous = None
                else: 
                    new_col[j] = previous
                    j += 1 
                    previous = col[i]
    if previous != None:
        new_col[j] = previous
    return new_col


def move(board, direction):
    # 0: left, 1: up, 2: right, 3: down
    rotated_board = rot90(board, direction)
    cols = [rotated_board[i, :] for i in range(4)]
    new_board = array([move_left(col) for col in cols])
    return rot90(new_board, -direction)