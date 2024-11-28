BELGIAN_FLAG = "🍟"
FRENCH_FLAG = "🥐"
BOARD_SIZE = 3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (BOARD_SIZE * 3))
    print()

def check_winner(board, flag):
    for row in board:
        if all(s == flag for s in row):
            return True
    for col in range(BOARD_SIZE):
        if all(row[col] == flag for row in board):
            return True
    if all(board[i][i] == flag for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE-1-i] == flag for i in range(BOARD_SIZE)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_flag = BELGIAN_FLAG
    for _ in range(BOARD_SIZE * BOARD_SIZE):
        print_board(board)
        row, col = map(int, input(f"Enter the position for {current_flag} (row and column): ").split())
        if board[row][col] == " ":
            board[row][col] = current_flag
            if check_winner(board, current_flag):
                print_board(board)
                print(f"{current_flag} wins!")
                return
            current_flag = FRENCH_FLAG if current_flag == BELGIAN_FLAG else BELGIAN_FLAG
        else:
            print("Position already taken. Try again.")
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
