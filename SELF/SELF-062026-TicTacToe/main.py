# 0626-2026
# Tic Tac Toe 
# Hopefully with new skills.

# board is list of coordinates
# coordinate is a list [x,y,value] , value [x,o,missing]
import copy
board =[]

def setup():
    global board
    for x in range(1,4):
        for y in range(1,4):
            coordinate =[]
            coordinate.append(x)
            coordinate.append(y)
            board.append(coordinate)
         
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

def show_coordinates(board):
    '''show each square in 3x3 grid format
        note each square which is actually a list 
        e.g. [2,2,'x] is x in the middle square'''
    count=0
    row =''
    for n in board:
        count +=1
        row +=str(n)
        if count % 3 == 0:
            print(row)
            row =''

def make_human_move(board):
    empty=[square for square in board if len(square)==2]

    count=0
    print("These are the current possible moves")
    for square in empty:
        count +=1
        # show menu of open squares
        print(f'{count}. Row: {square[0]} Column: {square[1]}')
        
    human_move_index = None
    # accept / validate input 
    while human_move_index not in range(1,count+1):
       human_move_index = int(input(f'Please enter your move 1 - {count}\n'))
       
    # update board 
    human_move_coordinates = empty[human_move_index-1]
    for square in board:
        if square[:2] == human_move_coordinates:
            square.append('x')

    # show board
    show(board=board)
  
def check_for_win(board,check_both=False):
    sequences = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    # print(f'in check_for_win\n\tboard :{board}\n\tcheck_both:{check_both}')
    for sequence in sequences:
        markers=''
        for s in sequence:
            markers +=board[s][2] if len(board[s])==3 else ''
        # print(f'markers: {markers}')
        if markers == 'ooo':
            return True
        if check_both == True and (markers =='xxx' or markers =='ooo'):
            return True
    return False

def check_for_block(board):
    sequences = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    for sequence in sequences:
        # print(f'in loop{sequence} of {sequences}')
        markers=''
        empty_square = None
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
                    # print(f'move:{possible_move} wins?:{result}')
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
# ====================================
# NonFunction starts here

setup() 
global empty
empty=len([square for square in board if len(square)==2])
while empty > 0:
    show(board=board)
    make_human_move(board=board)
    # did someone win?
    if check_for_win(board=board,check_both=True):
        print('Human has won. I am sad')
        break
    print('-' * 40)
    move = find_best_move(board=board)
    print(move)
    board = update_board(board=board, move=move, marker='o')
    if check_for_win(board=board,check_both=True):
        print('Computer has won. Resistance is futile')
        show(board=board)
        break
    empty=len([square for square in board if len(square)==2])