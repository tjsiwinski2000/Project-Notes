import copy
board = [[1, 1,'x'], [1, 2,'x'], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]

def show(board):
    '''show each square in grid format for game play'''
    count=0
    row =''
    for n in board:
        count +=1
        # print(f'{n} : len {len(n)} :{count}')
        square = '-'
        if len(n) ==3:
            square = n[2]
        row += square
        if count % 3 == 0:
            print(row)
            row =''
            
def check_for_win(board):
    sequences = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[6,7,8],[2,4,6],[0,4,8]]
    for sequence in sequences:
        markers=''
        for s in sequence:
            markers +=board[s][2] if len(board[s])==3 else ''
        if markers == 'ooo':
            return True
    return False

def check_for_block(board):
    sequences = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[6,7,8],[2,4,6],[0,4,8]]
    for sequence in sequences:
        # print(f'in loop{sequence} of {sequences}')
        markers=''
        for s in sequence:
            markers += board[s][2] if len(board[s])==3 else ''
            if len(board[s]) != 3:
                empty_square = s
        if markers=='xx' :
            # print(f'found block in squares:{sequence}')
            # print(f'empty_square = {empty_square}, coordinate = {board[empty_square]}')
            return(board[empty_square])
    # get here nothing to block
    return None

def find_best_move(board):
    # determine possible moves
    empty=[square for square in board if len(square)==2]
    move=[0,0]
    # iterate thr. ALL possible moves in empty[]]
    for possible_move in empty:
        # wc_board is a working copy of the board
        wc_board = copy.deepcopy(board)
        # check if win possible
        for square in wc_board:
            if square[:2]  == possible_move:
                square.append('o')
                # by appending 'o' we create a "board" with that possible move
                result = check_for_win(board=wc_board)
                if result == True:
                    print(f'move:{possible_move} wins?:{result}')
                    return possible_move
    # check for blocks
    block = check_for_block(board=board)
    if block is not None:
        return block
    else:
         #add code to find best move not win, not block
         # iterate thr.  possible moves in empty[]]
         # center , 4 corners, any item
        print(f'possible moves {empty}')
        if [2,2] in empty:
            return [2,2]
        elif [1,1] in empty:
            return [1,1]
        elif [1,3] in empty:
            return [1,3]
        elif [3,1] in empty:
            return [3,1]
        elif [3,3] in empty:
            return [3,3]
        else:
            return empty[0]
        
    return move
                                 
def update_board(board,move,marker):
    for square in board:
        if square[:2] == move:
            square.append(marker)
    return board


empty=len([square for square in board if len(square)==2])
while empty > 0:
    show(board=board)
    print('-' * 40)
    move = find_best_move(board=board)
    print(move)
    board = update_board(board=board, move=move, marker='o')
    empty=len([square for square in board if len(square)==2])

show(board=board)



# print(empty)
# count=0
# print("These are the current possible moves")
# for square in empty:
#     count +=1
#     print(f'{count}. Row: {square[0]} Column: {square[1]}')
    
# human_move = None
# while human_move not in range(1,count+1):
#     human_move = int(input(f'Please enter your move 1 - {count}\n'))


# print(f'Now processing human move {human_move}')
# print(f'Move chosen was: {empty[human_move-1]} ')

# human_move_coordinates = empty[human_move-1]
# for square in board:
#     if square[:2] == human_move_coordinates:
#         square.append('x')

# print(board)

