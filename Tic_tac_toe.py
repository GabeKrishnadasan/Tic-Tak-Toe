import tkinter as tk

class Tik_tac_toe:
    def __init__(self):
        self.spaces = [[2,2,2], [2,2,2], [2,2,2]]

        self.state = 0

        self.window = tk.Tk()
        self.window.title("Tik Tac Toe")

        self.top_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)
        self.top_frame.grid(row = 1, column = 1)
        self.bottom_frame.grid(row = 2, column = 1)

        self.quit_button = tk.Button(self.bottom_frame, text = "Quit", command = self.quit)
        self.quit_button.grid(row = 1, column = 1)
        self.start_again_button = tk.Button(self.bottom_frame, text = "Play again", command = self.play_again)
        self.start_again_button.grid(row = 1, column = 2)

        self.canvas = tk.Canvas(self.top_frame, width = 600, height = 600)
        self.canvas.grid(row=1, column=1)

        self.create_gameboard()

        self.canvas.bind("<ButtonRelease-1>", self.click_handler)

        tk.mainloop()

    def create_gameboard(self):
        self.canvas.create_line(200,0,200,600)
        self.canvas.create_line(400,0,400,600)
        self.canvas.create_line(0,200,600,200)
        self.canvas.create_line(0,400,600,400)

    def click_handler(self, event):
        row = -1
        column = -1
        if event.x < 200:
            if event.y < 200:
                row = 0
                column = 0
            elif event.y < 400 and event.y > 200:
                row = 0
                column = 1
            elif event.y < 600 and event.y > 400:
                row = 0
                column = 2
        elif event.x > 200 and event.x < 400:
            if event.y < 200:
                row = 1
                column = 0
            elif event.y < 400 and event.y > 200:
                row = 1
                column = 1
            elif event.y < 600 and event.y > 400:
                row = 1
                column = 2
        elif event.x > 400 and event.x < 600:
            if event.y < 200:
                row = 2
                column = 0
            elif event.y < 400 and event.y > 200:
                row = 2
                column = 1
            elif event.y < 600 and event.y > 400:
                row = 2
                column = 2

        if self.state == 0:
            if self.is_legal(row,column):
                self.make_move(row, column)
                self.state = 1
                self.check_winner()
        elif self.state == 1:
            if self.is_legal(row,column):
                self.make_move(row, column)
                self.state = 0
                self.check_winner()

    def is_legal(self, row, column):
        if self.spaces[row][column] == 2:
            return True
        else:
            return False

    def make_move(self, row, column):
        if self.state == 0:
            self.spaces[row][column] = self.state
            self.make_x(row, column)
        elif self.state == 1:
            self.spaces[row][column] = self.state
            self.make_o(row, column)

    def make_x(self, row, column):
        self.canvas.create_line(50 + (row * 200), 50 + (column * 200), 150 + (row * 200), 150 + (column * 200), tag = "game")
        self.canvas.create_line(150 + (row * 200), 50 + (column * 200), 50 + (row * 200), 150 + (column * 200), tag = "game")
    
    def make_o(self, row, column):
        self.canvas.create_oval(50 + (row * 200), 50 + (column * 200), 150 + (row * 200), 150 + (column * 200), tag = "game")

    def check_winner(self):
        if self.spaces[0][0] == 0 and self.spaces[0][1] == 0 and self.spaces[0][2] == 0 or self.spaces[1][0] == 0 and self.spaces[1][1] == 0 and self.spaces[1][2] == 0 or self.spaces[2][0] == 0 and self.spaces[2][1] == 0 and self.spaces[2][2] == 0:
            print("Player 1 wins")
            print("Game over")
            self.state = 2
        elif self.spaces[0][0] == 1 and self.spaces[0][1] == 1 and self.spaces[0][2] == 1 or self.spaces[1][0] == 1 and self.spaces[1][1] == 1 and self.spaces[1][2] == 1 or self.spaces[2][0] == 1 and self.spaces[2][1] == 1 and self.spaces[2][2] == 1:
            print("Player 2 wins")
            print("Game over")
            self.state = 2
        if self.spaces[0][0] == 0 and self.spaces[1][0] == 0 and self.spaces[2][0] == 0 or self.spaces[0][1] == 0 and self.spaces[1][1] == 0 and self.spaces[2][1] == 0 or self.spaces[0][2] == 0 and self.spaces[1][2] == 0 and self.spaces[2][2] == 0:
            print("Player 1 wins")
            print("Game over")
            self.state = 2
        elif self.spaces[0][0] == 1 and self.spaces[1][0] == 1 and self.spaces[2][0] == 1 or self.spaces[0][1] == 1 and self.spaces[1][1] == 1 and self.spaces[2][1] == 1 or self.spaces[0][2] == 1 and self.spaces[1][2] == 1 and self.spaces[2][2] == 1:
            print("Player 2 wins")
            print("Game over")
            self.state = 2
        if self.spaces[0][0] == 0 and self.spaces[1][1] == 0 and self.spaces[2][2] == 0 or self.spaces[0][2] == 0 and self.spaces[1][1] == 0 and self.spaces[2][0] == 0:
            print("Player 1 wins")
            print("Game over")
            self.state = 2
        elif (self.spaces[0][0] == 1 and self.spaces[1][1] == 1 and self.spaces[2][2] == 1)  or (self.spaces[0][2] == 1 and self.spaces[1][1] == 1 and self.spaces[2][0] == 1):
            print("Player 2 wins")
            print("Game over")
            self.state = 2

    def play_again(self):
        self.canvas.delete("game")
        self.spaces = [[2,2,2], [2,2,2], [2,2,2]]
        self.state = 0

    def quit(self):
        self.window.destroy()
    
if __name__ == "__main__":
    Tik_tac_toe()
