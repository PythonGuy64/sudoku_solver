import numpy
import time

"""
difficulté extrême:

0 0 0 8 0 1 0 0 0
0 0 0 0 0 0 0 4 3
5 0 0 0 0 0 0 0 0
0 0 0 0 7 0 8 0 0
0 0 0 0 0 0 1 0 0
0 2 0 0 3 0 0 0 0
6 0 0 0 0 0 0 7 5
0 0 3 4 0 0 0 0 0
0 0 0 2 0 0 6 0 0

2 3 7 8 4 1 5 6 9
1 8 6 7 9 5 2 4 3
5 9 4 3 2 6 7 1 8
3 1 5 6 7 4 8 9 2
4 6 9 5 8 2 1 3 7
7 2 8 1 3 9 4 5 6
6 4 2 9 1 8 3 7 5
8 5 3 4 6 7 9 2 1
9 7 1 2 5 3 6 8 4

difficulté facile:

7 8 0 4 0 0 1 2 0
6 0 0 0 7 5 0 0 9
0 0 0 6 0 1 0 7 8
0 0 7 0 4 0 2 6 0
0 0 1 0 5 0 9 3 0
9 0 4 0 6 0 0 0 5
0 7 0 3 0 0 0 1 2
1 2 0 0 0 7 4 0 0
0 4 9 2 0 6 0 0 7

7 8 5 4 3 9 1 2 6
6 1 2 8 7 5 3 4 9
4 9 3 6 2 1 5 7 8
8 5 7 9 4 3 2 6 1
2 6 1 7 5 8 9 3 4
9 3 4 1 6 2 7 8 5
5 7 8 3 9 4 6 1 2
1 2 6 5 8 7 4 9 3
3 4 9 2 1 6 8 5 7
"""


def valid_number(board, y, x, n):
    for x2 in range(9):
        if board[y][x2] == n:
            return False

    for y2 in range(9):
        if board[y2][x] == n:
            return False

    sy2 = y - y % 3
    sx2 = x - x % 3

    for y2 in range(sy2, sy2 + 3):
        for x2 in range(sx2, sx2 + 3):
            if board[y2][x2] == n:
                return False

    return True


def solve(board):
    targets = []
    current_index = -1

    for y in range(9):
        for x in range(9):
            if not board[y][x]:
                targets.append((y, x))
                current_index += 1

                for n in range(1, 10):
                    if valid_number(board, y, x, n):
                        board[y][x] = n
                        break
                else:
                    blocked = True
                    direction = -1

                    while blocked:
                        current_index += direction
                        y2, x2 = targets[current_index]

                        for n in range(board[y2][x2] + 1, 10):
                            if valid_number(board, y2, x2, n):
                                board[y2][x2] = n

                                if current_index == len(targets) - 1:
                                    blocked = False
                                    break

                                direction = 1
                                break
                        else:
                            board[y2][x2] = 0
                            direction = -1


def solve_2(board):
    """
    This function tells if the sudoku has 1 or multiple solution(s). It finds a maximum of 2 solutions.
    Sudokus with multiple solutions are not valid.
    """
    global solution_count

    for y in range(9):
        for x in range(9):
            if not board[y][x]:
                for n in range(1, 10):
                    if valid_number(board, y, x, n):
                        board[y][x] = n

                        if solve_2(board) == 2:
                            return 2

                board[y][x] = 0
                return 0

    solution_count += 1
    return solution_count


def solve_all(board):
    """
    This function tells how many solution(s) the sudoku has. Sudokus with multiple solutions are not valid.
    """
    global solution_count

    for y in range(9):
        for x in range(9):
            if not board[y][x]:
                for n in range(1, 10):
                    if valid_number(board, y, x, n):
                        board[y][x] = n
                        solve_all(board)

                board[y][x] = 0
                return

    solution_count += 1


# Extremely hard sudoku
"""sudoku = [
    [0, 0, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 3],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 3, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 7, 5],
    [0, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 6, 0, 0]
]"""

# Easy sudoku
sudoku = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Safety check
"""valid_board = True

for y in range(9):
    for x in range(9):
        number = sudoku[y][x]

        if number and not valid_number(sudoku, (y, x), number):
            valid_board = False
            break

    if not valid_board:
        print("Invalid board!")
        break

if valid_board:
    solve(sudoku)"""

# To check if the sudoku has 1 or multiple solution(s)
"""solution_count = 0
solve_2(sudoku)
print(f" The sudoku has {'1 solution' if solution_count == 1 else 'multiple solutions'}\n")"""

# To check how many solution(s) the sudoku has
"""solution_count = 0
solve_all(sudoku)
print(f" The sudoku has {solution_count} solution{'' if solution_count == 1 else 's'}\n")"""

# Make sure the board is valid
start = time.time()
solve(sudoku)
duration = time.time() - start
print(f"{numpy.matrix(sudoku)}\n\n {duration:.3f} seconds.")
input()
