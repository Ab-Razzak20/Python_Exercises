## tic_tac_toe

def next_player(current_player):
    '''(str) -> (str)
    Returns the next player given the current_player.
    '''
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    return current_player

def check_valid_move(board , pos):
    '''(dict,int) --> (bool)
    Returns True or False if the position choosen has empty space.
    '''
    if board[pos] == '':
        return True

    else:
        return False
    
def check_win(board , current_player):
    '''(dict,str) --> (bool)
    Return True if current_player has won the game.
    '''
    # in rows
    for i in range(1, 10, 3):
        if all(board[i+j] == current_player for j in range(3)):
            return True
    # if board[1] == board[2] == board[3] == current_player or \
    #    board[4] == board[5] == board[6] == current_player or \
    #    board[7] == board[8] == board[9] == current_player:
    #     return True
    
    #in columns
        for i in range(3):
            if all(board[i+j] == current_player for j in range(1, 10, 3)):
                return True
    # if board[1] == board[4] == board[7] == current_player:
    #     return True
    # if board[2] == board[5] == board[8] == current_player:
    #     return True
    # if board[3] == board[6] == board[9] == current_player:
    #     return True
    
    # in diagonals 
    # if current_player in board[1] and current_player in board[5] and current_player in board[9] or\
    #    current_player in board[3] and current_player in board[5] and current_player in board[7]:
    if all(board[i] == current_player for i in [1, 5, 9]) or\
        all(board[i] == current_player for i in [3, 5, 7]):
        return True
    else:
        return False
    
    # winning_combinations = [
    #     [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
    #     [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
    #     [1, 5, 9], [3, 5, 7]              # Diagonals
    # ]

    # for combo in winning_combinations:
    #     if all(board[pos] == current_player for pos in combo):
    #         return True

    # return False

def check_draw(num_moves):
    '''(int) --> (bool)
    Return True or False given the total number of moves played given by num_moves.
    '''
    if num_moves<9:
        return False
    else:
        return True
    
print(check_valid_move({1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, 6))
print(check_win({1: 'O', 2: 'X', 3: 'O', 4: 'X', 5: 'O', 6: 'X', 7: 'X', 8: 'O', 9: 'X'}, 'O'))
    
