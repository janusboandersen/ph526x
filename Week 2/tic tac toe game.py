#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 00:05:53 2017

@author: janusboandersen
"""

#tic tac toe game

import numpy as np
import random

def create_board():
    return np.zeros((3,3), dtype=int)

    
def place(board, player, position):
    #check if the specified position is already taken
    r,c = position
    if board[r][c] != 0:
        print("That tile is already taken")
    else:
        board[r][c] = player

        
def possibilities(board):
    rc = np.where(board == 0)
    rows, tuples = np.shape(rc)
    results = []
    for i in range(tuples):
        x,y = rc[0][i],rc[1][i] 
        results.append((x,y))
    return results

    
def random_place(board, player):
    (r,c) = random.choice(possibilities(board))
    board[r][c] = player


def random_play(board):
    for i in range(4):
        for player in [1, 2]:
            random_place(board, player)
            if evaluate(board) != -1 and evaluate(board) != 0:
                print("You won player ", evaluate(board))
                return evaluate(board)  #break once a player has won

            
def row_win(board, player):
    temp = np.all(board == player, axis=1) #bool vector with truth value for each row
    return np.any(temp)   #check and return if any rows have a win
    
def col_win(board, player):
    temp = np.all(board == player, axis=0) #bool vector with truth value for each col
    return np.any(temp)   #check and return if any rows have a win

def diag_win(board, player):
    d1 = np.diagonal(board)
    d2 = np.diagonal(np.fliplr(board))
    win_d1 = np.all(d1 == player)
    win_d2 = np.all(d2 == player)
    return (win_d1 or win_d2)


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if (row_win(board, player) or col_win(board, player) or diag_win(board, player)):
            winner = player
            
    if np.all(board != 0) and winner == 0:
        winner = -1
        
    return winner


    
#generate the board
board = create_board()

#place player 1 in (0,0)
#place(board, 1, (0,0))

#Play the game
random_play(board)
