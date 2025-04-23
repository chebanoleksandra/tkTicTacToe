import random
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TikTacToe")
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=("Arial", 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] =="":
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_info("X"):
                messagebox.showinfo("Game over", "You WIN!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game over", "DRAW")
                self.reset_game()
            else:
                self.root.after(500, self.comp_move)

    def comp_move(self):
        empty_ind = [i for i,v in enumerate(self.board) if v ==""]
        if not empty_ind:
            return
        move = random.choice(empty_ind)
        self.board[move] = "0"
        self.buttons[move].config(text="0")
        if self.check_info("0"):
            messagebox.showinfo("Game over", "Comp WINS")
            self.reset_game()
        elif "" not in self.board:
                messagebox.showinfo("Game over", "DRAW")
                self.reset_game()

    def check_info(self, symbol):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] == symbol:
                return True
        return False
    def reset_game(self):
        self.board = [""]  * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    win = TicTacToe(root)
    root.mainloop()
