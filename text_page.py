import tkinter as tk

class TextPage(tk.Frame):
    def __init__(self, text, title, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.text = text
        self.widgets = []
        self.create_widgets()
        self.master.title(title)


    def create_widgets(self):
        self.message = tk.Label(self, text=self.text)
        self.message.pack()

        self.guess = tk.Button(self)
        self.guess["text"] = "Guess"
        self.guess["command"] = self.guess_cmd
        self.guess.pack()

    def guess_cmd(self):
        self.pack_forget()
        self.destroy()
        self.quit()
