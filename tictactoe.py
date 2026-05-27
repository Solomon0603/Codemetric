import math

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def is_moves_left(board):
    return ' ' in board

def evaluate(board):

    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != ' ':
            return 10 if board[i*3] == 'O' else -10

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return 10 if board[i] == 'O' else -10

    if board[0] == board[4] == board[8] and board[0] != ' ':
        return 10 if board[0] == 'O' else -10
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return 10 if board[2] == 'O' else -10
        
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not is_moves_left(board): return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def play_round():
    board = [' '] * 9
    print_board(board)
    
    while is_moves_left(board) and evaluate(board) == 0:
        try:
            user_move = int(input("Enter your move (1-9): ")) - 1
            if user_move < 0 or user_move > 8 or board[user_move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        board[user_move] = 'X'
        print_board(board)
        
        if not is_moves_left(board) or evaluate(board) != 0:
            break

        print("Computer is thinking...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print_board(board)

    score = evaluate(board)
    if score == 10:
        print("Outcome: Computer wins! 🤖")
    elif score == -10:
        print("Outcome: You win! 🎉")
    else:
        print("Outcome: It's a draw! 🤝")

def main():
    print("Welcome to Minimax Tic Tac Toe!")
    print("You are 'X' and the Computer is 'O'.")
    
    while True:
        play_round()
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
