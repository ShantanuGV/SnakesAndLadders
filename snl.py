import tkinter as tk
import random

# Snakes and ladders positions
snakes = {16: 6, 48: 30, 62: 19, 88: 24, 95: 56, 97: 78}
ladders = {3: 22, 5: 8, 15: 25, 18: 45, 21: 42, 28: 55, 51: 67, 71: 91, 80: 99}

class SnakeLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder")
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()

        self.board_size = 10
        self.cell_size = 60
        self.players = ["red", "blue"]
        self.positions = [1, 1]
        self.turn = 0

        self.draw_board()
        self.draw_snakes_and_ladders()

        self.pieces = [
            self.canvas.create_oval(10, 550, 30, 570, fill=self.players[0]),
            self.canvas.create_oval(10, 550, 30, 570, fill=self.players[1])
        ]

        self.dice_btn = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.dice_btn.pack()
        self.info = tk.Label(master, text="Player 1's turn")
        self.info.pack()

    def draw_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                x1 = col * self.cell_size
                y1 = (9 - row) * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                num = row * self.board_size + (col + 1 if row % 2 == 0 else self.board_size - col)
                self.canvas.create_text(x1 + 30, y1 + 30, text=str(num))

    def get_coordinates(self, position):
        row = (position - 1) // 10
        col = (position - 1) % 10
        if row % 2 != 0:
            col = 9 - col
        x = col * self.cell_size + 10 + (20 * self.turn)
        y = (9 - row) * self.cell_size + 10
        return x, y

    def move_piece(self, player):
        x, y = self.get_coordinates(self.positions[player])
        self.canvas.coords(self.pieces[player], x, y, x + 20, y + 20)

    def roll_dice(self):
        dice = random.randint(1, 6)
        current = self.turn % 2
        self.info.config(text=f"Player {current + 1} rolled a {dice}")

        if self.positions[current] + dice <= 100:
            self.positions[current] += dice
            if self.positions[current] in snakes:
                self.positions[current] = snakes[self.positions[current]]
            elif self.positions[current] in ladders:
                self.positions[current] = ladders[self.positions[current]]

        self.move_piece(current)

        if self.positions[current] == 100:
            self.info.config(text=f"🎉 Player {current + 1} wins! 🎉")
            self.dice_btn.config(state="disabled")
        else:
            self.turn += 1
            next_player = (self.turn % 2) + 1
            self.info.config(text=f"Player {next_player}'s turn")

    def get_center_coords(self, position):
        row = (position ) // 10
        col = (position ) % 10
        if row % 2 != 0:
            col = 9 - col
        x = col * self.cell_size + self.cell_size // 2
        y = (9 - row) * self.cell_size + self.cell_size // 2
        return x, y

    def draw_snakes_and_ladders(self):
        # Draw ladders
        for start, end in ladders.items():
            x1, y1 = self.get_center_coords(start)
            x2, y2 = self.get_center_coords(end)
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=4, arrow=tk.LAST)

        # Draw snakes
        for start, end in snakes.items():
            x1, y1 = self.get_center_coords(start)
            x2, y2 = self.get_center_coords(end)
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=4, arrow=tk.LAST)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
