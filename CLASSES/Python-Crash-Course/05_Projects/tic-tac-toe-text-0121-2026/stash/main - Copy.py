#0121-2026-Udemy-Lesson86 
#tic-tac-toe  - text based 
# human plays X and moves first; computer plays O , second

def show_board(board):
    for count in range(0,9,3):
        print(f"{board[count]} | {board[count+1]}  | {board[count+2]}")
    
    
#initial position
initial_board_position =  ['-','-','-','-','-','-','-','-','-']
#display initial board
board_position = initial_board_position 
show_board(board_position)
#all rows / columns, diagonals by designation
list_three_consecutive =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def move_is_legal(board,move):
    if move >= 0 and move <=8:
        if board_position[move]== '-':
            return True
        else:
            return False
    else:
        return False

def check_game_over(board,move):
    pass

def determine_computer_move(board):
    #determine how many moves already made
    num_moves = 9-board.count('-')
    print(num_moves)
    if num_moves == 1:
        if move_is_legal(board,4):
            return(4) # take center if available
        else:
            for num in (0,2,6,8):
                if move_is_legal(board,num):
                    return(num) # take first available corner if !center
    else:
        #not first move
        # check if computer can WIN
        move = determine_two_row(list_three_consecutive,"O")
        if move >= 0:
            return move
        # check if computer needs to BLOCK human from winning
        move = determine_two_row(list_three_consecutive,"X")
        if move  >= 0:
            return move
        else:
            pass
            #nothing to block 1)try to win 
            # 2)iterate thr.corners and then all other squares go to first empty

def determine_two_row(input_list,char):
    for my_list in input_list:
        pos1 = my_list[0]
        pos2 = my_list[1]
        pos3 = my_list[2]
        test_list=[board_position[pos1],board_position[pos2],board_position[pos3]]
        print(f"test_list= {test_list}")
        if test_list.count(char) == 2:
            if board_position[pos1] == '-':
                return pos1
            if board_position[pos2] == '-':
                return pos2
            if board_position[pos3] == '-':
                return pos3
        else:
            continue
    #reach here then there aren't any two in a row
    return -1
    

while True:
    move=int(input("what square do you want to move to"))
    if move_is_legal(board_position,move) is False:
        print("Illegal move, please try again, remember squares are numbered 0 - 8 ")
        continue
            
    board_position[move] ='X'
    print(board_position)
    if check_game_over == True:
        print('Thank you for playing')
        print("\n\n")
        board_position= initial_board_position
        continue
    show_board(board_position)
    computer_move = int(determine_computer_move(board_position))
    board_position[computer_move] = 'O'
    show_board(board_position)