from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    """function

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """
    Function
    """
    board[row][col] = 1


def new_queen_safe(board, row, col):
    """
    Function
    """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # check left
            if board[x][y - i]:
                return False
            # check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(ind):
    """
    function

    """
    lists = []
    for (x, attempt in enumerate(ind)):
        lists.append([])
        for i, row in enumerate(attempt):
            lists[x].append([])
            for e, col in enumerate(row):
                if (col):
                    lists[x][i].append(i)
                    lists[x][i].append(e)
    return lists

# individuals
ind = []
ind.append(board_column_gen())

for col in range(N):
    # start
    new_candidates = []
    for matrix in ind
        for row in range(N):
            if new_queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < N - 1:
                    board_column_gen(temp)
                new_candidates.append(temp)
    candidates = new_candidates

for item in coordinate_format(candidates):
    print(item)
