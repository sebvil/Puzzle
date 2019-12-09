import tkinter as tk


DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35
FONT = ("Arial", 20)

class PassportPage(tk.Frame):
    def __init__(self, title, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets = []
        self.title = title

    def set_previous(self, previous):
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def create_widgets(self):
        self.master.title(self.title)
        self.canvas = tk.Canvas(self.master)
        square_dim = DIM_Y - 10 - 3 * BUTTON_SIZE
        start_x = DIM_X / 2 - square_dim / 2
        square_dim /= 5
        colors = ["red", "blue", "green", "yellow", "orange", "purple"]
        coordinates = [(0,0), (0,2), (1, 4), (2, 1), (3, 3),(4, 2)]
        index = 0
        for i in range(5):
            for j in range(5):
                self.canvas.create_rectangle(i * square_dim + start_x,
                                             j * square_dim + 10,
                                             i * square_dim + start_x + square_dim,
                                             j * square_dim + 10 + square_dim,
                                             outline="black")
                if (j, i) in coordinates:
                    offset = 10
                    self.canvas.create_oval(i * square_dim + start_x + offset,
                                            j * square_dim + 10 + offset,
                                            i * square_dim + start_x + square_dim - offset,
                                            j * square_dim + 10 + square_dim - offset,
                                            fill=colors[index])
                    index += 1
        self.canvas.place(x=0,y=0, width = DIM_X, height=DIM_Y)

        self.next_page = tk.Button(self.master)
        self.next_page["text"] = "Next"
        self.next_page["command"] = self.next_cmd
        self.next_page["font"] = ("Arial", 25)
        self.next_page.place(x = DIM_X / 2 + BUTTON_SIZE,
                        y = DIM_Y - 2 * BUTTON_SIZE,
                        width = 3 * BUTTON_SIZE,
                        height = BUTTON_SIZE)

        self.back = tk.Button(self.master)
        self.back["text"] = "Back"
        self.back["command"] = self.go_back
        self.back["font"] = ("Arial", 25)
        self.back.place(x = DIM_X / 2 - BUTTON_SIZE * 4,
                        y = DIM_Y - 2 * BUTTON_SIZE,
                        width = 3 * BUTTON_SIZE,
                        height = BUTTON_SIZE)

    def destroy_widgets(self):
        self.canvas.destroy()
        self.back.destroy()
        self.next_page.destroy()

    def go_back(self):
        self.destroy_widgets()
        self.destroy()
        self.quit()
        self.previous.create_widgets()
        self.previous.mainloop()

    def next_cmd(self):
        self.destroy_widgets()
        self.destroy()
        self.quit()
        self.next.create_widgets()
        self.next.mainloop()

