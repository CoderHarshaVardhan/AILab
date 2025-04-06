board = [" " for _ in range(9)]
print(board)

def print_board():
    print("\n")
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(player):
    win_pos = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    return any(all(board[i] == player for i in combo) for combo in win_pos)

def play_game():
    current = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current}, choose (0-8): "))

        while board[move] != " ":
            print("Spot taken! Try again.")
            move = int(input(f"Player {current}, choose (0-8): "))

        board[move] = current
        if check_winner(current):
            print_board()
            print(f"Player {current} wins!")
            return

        current = "O" if current == "X" else "X"

    print_board()
    print("It's a draw!")

play_game()
