import tkinter as tk


DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35
FONT = ("Arial", 20)

class BillsPage(tk.Frame):
    def __init__(self, title, text, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets = []
        self.title = title
        self.text = text

    def set_previous(self, previous):
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def create_widgets(self):
        self.master.title(self.title)

        self.master.title(self.title)
        print("test")
        self.message = tk.Label(self.master, text=self.text, font=("Arial", 25))
        self.message.place(x=10,y=10, width = DIM_X - 20,
                           height = DIM_Y - 3 * BUTTON_SIZE - 10)

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
        self.message.destroy()
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

