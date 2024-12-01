import tkinter as tk
from tkinter import font as tkFont
import tkinter.messagebox

def initialization_board(root, size):
    global turn
    global board
    global buttons
    global player
    global board_size
    turn = 0
    player = "X"
    board_size = size
    board = {}
    buttons = {}
    for r in range(1, size + 1):
        for c in range(1, size + 1):
            button = tk.Button(root, text='', width=10, height=5,
                               command=lambda r=r, c=c: check_winner(r, c, buttons[(r, c)]))
            button.grid(row=r+2, column=c-1)
            buttons[(r, c)] = button
            board[r, c] = ''
    return board, buttons

def check_winner(r, c, button):
    global turn
    global player
    
    if player == "X": 
        co_lor="red"
    else: co_lor="blue"
    button.config(text=player, bg=co_lor, state="disabled")  # Update button text
    turn += 1
    board[r, c] = player
    if check_for_winner(r, c):
        tk.messagebox.showinfo("Winner", f"Player {player} wins!")
        disable_buttons()
    elif turn == board_size * board_size:
        tk.messagebox.showinfo("Draw", "It's a draw!")
    else:
        switch_player()

def check_for_winner(r, c):
    if check_row(board, r) or check_col(board, c) or Top_Left_to_Right_Bottom() or Top_Right_to_Left_Bottom() or Down_Left_to_Right():
        return True
    return False

def check_row(board, r):
    return any(all(board[r, c] == player for c in range(c, c + rule_win)) for c in range(1, board_size - rule_win + 2))

def check_col(board, c):
    return any(all(board[r, c] == player for r in range(r, r + rule_win)) for r in range(1, board_size - rule_win + 2))

def Top_Left_to_Right_Bottom():
    return any(all(board[r + i, c + i] == player for i in range(rule_win)) for r in range(1, board_size - rule_win + 2) for c in range(1, board_size - rule_win + 2))

def Top_Right_to_Left_Bottom():
    return any(all(board[r + i, c - i] == player for i in range(rule_win)) for r in range(1, board_size - rule_win + 2) for c in range(rule_win, board_size + 1))

def Down_Left_to_Right():
    return any(all(board[r + k, c + rule_win - 1 - k] == player for k in range(rule_win)) for r in range(1, board_size - rule_win + 2) for c in range(1, board_size - rule_win + 2))

def disable_buttons():
    for button in buttons.values():
        button.config(state="disabled")

def switch_player():
    global player
    player = "O" if player == "X" else "X"

player = "X"
turn = 0
size = 7
rule_win = 4  # Change this value as desired
root = tk.Tk()
root.title('TIC TAC TOE')

# add widgets Label
wf = tk.Label(root, text='Player X', fg='red')
wf.grid(row=0)

wl = tk.Label(root, text='Player O', fg='blue')
wl.grid(row=1)

# add input field
e1 = tk.Entry(root, fg='red', width=10)
e2 = tk.Entry(root, fg='blue', width=10)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

board, buttons = initialization_board(root, size)
button_new_game = tk.Button(root, text="New Game", command=lambda: initialization_board(root, size))
button_new_game.grid(row=2, column=0, columnspan=3)

root.mainloop()
