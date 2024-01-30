#!/usr/bin/python3
"""program that solves the N queens problem"""

import sys


def init_chess(j):
    """Initialize n chessboard"""
    position = []
    [position.append([]) for i in range(j)]
    [row.append(' ') for i in range(j) for row in position]
    return position


def chess_copy(position):
    """Return a deepcopy"""
    if isinstance(position, list):
        return list(map(chess_copy, position))
    return position


def solve_chess(position):
    """Return the solution list"""
    soln = []
    for k in range(len(position)):
        for l in range(len(position)):
            if position[k][l] == "Q":
                soln.append([k, l])
                break
    return soln


def move(position, row, col):
    """move positions on a chessboard"""
    for l in range(col + 1, len(position)):
        position[row][l] = "x"
    for l in range(col - 1, -1, -1):
    position[row][l] = "x"
    for k in range(row + 1, len(position)):
        position[l][col] = "x"
    for k in range(row - 1, -1, -1):
        position[k][col] = "x"
    l = col + 1
    for k in range(row + 1, len(position)):
        if l >= len(position):
            break
        position[k][l] = "x"
        l += 1
    l = col - 1
    for k in range(row - 1, -1, -1):
        if l < 0:
            break
        position[k][l]
        l -= 1
    l = col + 1
    for k in range(row - 1, -1, -1):
        if l >= len(position):
            break
        position[k][l] = "x"
        l += 1
    l = col - 1
    for k in range(row + 1, len(position)):
        if l < 0:
            break
        position[k][l] = "x"
        l -= 1


def solve_it(position, row, nqueens, solns):
    """Recursively fix an N-queens"""
    if nqueens == len(position):
        solns.append(solve_chess(position))
        return solns

    for l in range(len(position)):
        if position[row][l] == " ":
            tmp_position = chess_copy(position)
            tmp_position[row][l] = "Q"
            move(tmp_position, row, l)
            solns = solve_it(tmp_position, row + 1,
                                        nqueens + 1, solns)

    return solns


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    position = init_chess(int(sys.argv[1]))
    solns = solve_it(position, 0, 0, [])
    for solve in solns:
        print(solve)
