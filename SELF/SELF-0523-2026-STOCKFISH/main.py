from stockfish import Stockfish

# 0525-2026 - TJS
# Python Wrapper calls local stockfish binary
# Full game play

sf = Stockfish(path=r"C:\Users\TJ\source\repos\Project-Notes\SELF\SELF-0523-2026-STOCKFISH\stockfish\stockfish-windows-x86-64-avx2.exe")


# Set skill level
sf.set_elo_rating(1500)

# Print board
print(sf.get_board_visual())

while True:
    print('Enter move (e.g. e2e4)')
    myMove = input()

    # Update the board with user's move (assume legal)
    sf.make_moves_from_current_position([myMove])

    # Get Stockfish's move
    computerMove = sf.get_best_move()
    print("Stockfish plays: ", computerMove)

    # Update the board with computer's move
    sf.make_moves_from_current_position([computerMove])

    print(sf.get_board_visual())