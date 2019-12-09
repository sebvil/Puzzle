import tkinter as tk


DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35
FONT = ("Arial", 15)

class TextPage(tk.Frame):
    def __init__(self, text, title, final=False, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.text = text
        self.widgets = []
        self.final = final
        self.title = title
        self.next = None

    def set_previous(self, previous):
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def create_widgets(self):
        self.master.title(self.title)
        print("test")
        self.message = tk.Label(self.master, text=self.text, font=("Arial", 25))
        self.message.place(x=10,y=10, width = DIM_X - 20,
                           height = DIM_Y - 3 * BUTTON_SIZE - 10)


        self.next_page = tk.Button(self.master)
        if not self.final:
            self.next_page["text"] = "Next"
        else:
            self.next_page["text"] = "Finish"
        self.next_page["command"] = self.next_cmd
        self.next_page["font"] = ("Arial", 25)
        self.next_page.place(x = DIM_X / 2 - BUTTON_SIZE * 3 / 2,
                             y = DIM_Y - 2 * BUTTON_SIZE,
                             width = 3 * BUTTON_SIZE,
                             height = BUTTON_SIZE)

    def destroy_widgets(self):
        self.next_page.destroy()
        self.message.destroy()

    def next_cmd(self):
        self.destroy_widgets()
        self.destroy()
        self.quit()
        if self.final:
            self.master.quit()
        if not self.final:
            self.next.create_widgets()
            self.next.mainloop()
