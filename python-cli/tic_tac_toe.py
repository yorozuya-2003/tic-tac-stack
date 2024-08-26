# initializing board
board = [[0 for _ in range(3)] for _ in range(3)]

# player names
player1_name = 'Player-1'
player2_name = 'Player-2'

# player markers
player1_marker = 1      # representing X
player2_marker = -1     # representing O

# player marker to name mapping
marker_to_name_map = {
    player1_marker: player1_name,
    player2_marker: player2_name,
}

# marker to symbol mapping (for displaying)
marker_to_symbol_map = {-1: 'O', 1: 'X', 0: ' '}

# initializing turns
num_turns = 0


# game methods
def check_winner():
    '''checking for winning state'''

    # checking rows
    for i in range(3):
        row_sum = 0
        for j in range(3):
            row_sum += board[i][j]
        if row_sum == 3:
            return player1_marker
        elif row_sum == -3:
            return player2_marker
     
    # checking cols
    for i in range(3):
        col_sum = 0
        for j in range(3):
            col_sum += board[j][i]
        if col_sum == 3:
            return player1_marker
        elif col_sum == -3:
            return player2_marker
    
    # checking the diagonals
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += board[i][i]
    if diagonal_sum == 3:
        return player1_marker
    elif diagonal_sum == -3:
        return player2_marker
    
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += board[i][2-i]
    if diagonal_sum == 3:
        return player1_marker
    elif diagonal_sum == -3:
        return player2_marker
    
    return 0


def print_board():
    '''printing board state'''

    separator = "---|---|---"

    print()
    for i, row in enumerate(board):
        print(f" {marker_to_symbol_map[row[0]]} | {marker_to_symbol_map[row[1]]} | {marker_to_symbol_map[row[2]]} ")
        if i < 2:
            print(separator)

    print()


# printing game start messages
print(f'TIC-TAC-TOE')
print(f'Player-1: {player1_name} (X)')
print(f'Player-2: {player2_name} (O)')
print_board()


# game loop
while (num_turns < 9):

    current_player = None
    if num_turns % 2 == 0:
        current_player = player1_marker
    else:
        current_player = player2_marker
    
    print(f"It is {marker_to_name_map[current_player]}'s ({marker_to_symbol_map[current_player]}) turn.")
    
    # taking in and validating move inputs
    try:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        assert row in [1, 2, 3]
        assert col in [1, 2, 3]

    except:
        print('[Invalid input: Enter valid integer row and column values, from {1, 2, 3}.]')
        print()
        continue

    row = row - 1
    col = col - 1

    # checking if board position already occupied
    if (board[row][col] != 0):
        print("[Position already occupied on the board. Try with valid position arguments.]")
        print()
        continue

    # placing marker
    board[row][col] = current_player
    print_board()
        
    # checking for winning state
    winner = check_winner()

    # if winner
    if winner != 0:
        print(f"{marker_to_name_map[winner]} has won the game.")
        break

    num_turns += 1


if num_turns == 9:
    print('The game ended in a draw.')

print()
print('---------------GAME OVER---------------')
print()