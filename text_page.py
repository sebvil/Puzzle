import tkinter as tk


DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35
FONT = ("Arial", 20)

class TextPage(tk.Frame):
    def __init__(self, text, title, final=False, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.text = text
        self.widgets = []
        self.final = final
        self.title = title

    def set_previous(self, previous):
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def create_widgets(self):
        super().__init__(self.master)
        self.pack()
        self.master.title(self.title)
        print("test")
        self.message = tk.Label(self, text=self.text, font=("Arial", 25))
        self.message.pack()

        if not self.final:
            self.guess = tk.Button(self)
            self.guess["text"] = "Guess"
            self.guess["command"] = self.guess_cmd
            self.guess["font"] = ("Arial", 25)
            self.guess.pack()

    def guess_cmd(self):
        self.pack_forget()
        self.destroy()
        self.quit()
        self.next.create_widgets()
        self.next.mainloop()
