# initializing board
board = [[0 for _ in range(3)] for _ in range(3)]

# player names
player1_name = 'Player-1'
player2_name = 'Player-2'

# player markers
player1_marker = +1
player2_marker = -1

# player marker to name mapping
marker_to_name_map = {
    player1_marker: player1_name,
    player2_marker: player2_name,
}

# player tokens
player1_tokens = [+1, +1, +2, +2, +3, +3]
player2_tokens = [-1, -1, -2, -2, -3, -3]

# player marker to tokens mapping
marker_to_tokens_map = {
    player1_marker: player1_tokens,
    player2_marker: player2_tokens,
}

# initializing turns
num_turns = 0


# game methods
def get_player_states(player1_state, player2_state, player_tokens):
    # checking for player-1
    check =True
    for token in player_tokens:
        check = check and (token > 0)

    if player1_state == 0 and check:
        other_player_tokens = marker_to_tokens_map[player2_marker]

        # if other player may counter
        if min(other_player_tokens) + min(player_tokens) < 0:
            player1_state = +1
        else:
            player1_state = +2
        
    # checking for player-2
    check =True
    for token in player_tokens:
        check = check and (token < 0)
    
    if player2_state == 0 and check:
        other_player_tokens = marker_to_tokens_map[player1_marker]

        # if other player may counter
        if max(other_player_tokens) + max(player_tokens) > 0:
            player2_state = -1
        else:
            player2_state = -2

    return player1_state, player2_state

    
def check_winner(prev_state):
    '''checking for winning state'''

    # game states
    #  0 : nobody winning
    # +1 : player-1 in winning position but player-2 can prevent
    # -1 : player-2 in winning position but player-1 can prevent
    # +2 : player-1 wins
    # -2 : player-2 wins

    player1_state = 0
    player2_state = 0

    # checking rows
    for r in range(3):
        player_tokens = [board[r][i] for i in range(3)]
        player1_state, player2_state = get_player_states(player1_state, player2_state, player_tokens)
    
    # checking columns
    for c in range(3):
        player_tokens = [board[i][c] for i in range(3)]
        player1_state, player2_state = get_player_states(player1_state, player2_state, player_tokens)

    # checking the diagonals
    player_tokens = [board[i][i] for i in range(3)]
    player1_state, player2_state = get_player_states(player1_state, player2_state, player_tokens)
    
    player_tokens = [board[i][2-i] for i in range(3)]
    player1_state, player2_state = get_player_states(player1_state, player2_state, player_tokens)

    # cases
    if player1_state == 0 and player2_state == 0:
        return 0
    
    if prev_state == 0:
        if player1_state != 0:
            return player1_state
        if player2_state != 0:
            return player2_state

    if prev_state == +1:
        if player1_state > 0:
            return +2
        else:
            return player2_state
    
    if prev_state == -1:
        if player2_state < 0:
            return -2
        else:
            return player1_state
    
    return 0


def print_board():
    '''printing board state'''

    separator = "----|----|----"

    print()
    for i, row in enumerate(board):
        m1 = f'+{row[0]}'[-2:] if row[0] != 0 else ' 0'
        m2 = f'+{row[1]}'[-2:] if row[1] != 0 else ' 0'
        m3 = f'+{row[2]}'[-2:] if row[2] != 0 else ' 0'

        print(f" {m1} | {m2} | {m3} ")
        if i < 2:
            print(separator)

    print()


def get_tokens_string_list(tokens):
    '''
    converting list of integer tokens to list of string tokens
    (for checking integer sign)
    '''
    return [f'+{token}'[-2:] for token in tokens]


def get_tokens_string(tokens):
    '''
    converting list of tokens to string format
    (for displaying)
    '''
    tokens_string = ''
    tokens_string_list = get_tokens_string_list(tokens)

    if len(tokens) > 0:
        for token in tokens_string_list:
            tokens_string += f'{token}, '
        tokens_string = tokens_string[:len(tokens_string)-2]

    return '{' + tokens_string +'}'


# printing game start messages
print(f'TIC-TAC-STACK')
print_board()

# game loop
prev_state = 0
draw = True

while (num_turns < 12):

    current_player = None
    if num_turns % 2 == 0:
        current_player = player1_marker
    else:
        current_player = player2_marker
    
    print(f"It is {marker_to_name_map[current_player]}'s turn.")

    # taking in and validating token input and position inputs
    token = 0
    row = -1
    col = -1

    while (token == 0 or (row == -1 and col == -1)):
        try:
            token = input(f'Choose from the following tokens: {get_tokens_string(marker_to_tokens_map[current_player])} => ')
            assert token in get_tokens_string_list(marker_to_tokens_map[current_player])
            token = int(token)

        except:
            token = 0
            print('[Invalid input: Enter valid token value, from the available tokens.]')
            print()
            continue
        
        try:
            row = int(input("Enter row => "))
            col = int(input("Enter column => "))
            assert row in [1, 2, 3]
            assert col in [1, 2, 3]

        except:
            row = -1
            col = -1
            print('[Invalid input: Enter valid integer row and column values, from {1, 2, 3}.]')
            print()

    row = row - 1
    col = col - 1

    # checking if board position capturable or not
    if board[row][col] == 0:
        pass

    elif current_player == player1_marker:
        if (board[row][col] > 0):
            print("[Position already occupied by you on the board. Try with valid position inputs.]")
            print()
            continue

        elif (board[row][col] + token <= 0):
            print("[Position cannot be captured. Try with valid token or position inputs.]")
            print()
            continue

    elif current_player == player2_marker:
        if (board[row][col] < 0):
            print("[Position already occupied by you on the board. Try with valid position inputs.]")
            print()
            continue

        elif (board[row][col] + token >= 0):
            print("[Position cannot be captured. Try with valid token or position inputs.]")
            print()
            continue

    # placing marker
    board[row][col] = token
    marker_to_tokens_map[current_player].remove(token)

    print_board()
        
    # checking for winning state
    winner = check_winner(prev_state)

    # if winner
    if abs(winner) == 2:
        print(f"{marker_to_name_map[winner//2]} has won the game.")
        draw = False
        break

    prev_state = winner

    num_turns += 1


if draw:
    print('The game ended in a draw.')

print()
print('---------------GAME OVER---------------')
print()
