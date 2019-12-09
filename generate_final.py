letters =list("123456789")
DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40

def generate_number_button(number, r, c):
    y = BUTTON_SIZE * r + DIM_Y / 2
    initial_x = DIM_X / 2 - BUTTON_SIZE * len(letters) / 2
    x = BUTTON_SIZE * c + initial_x
    button = """
        self.button_%s = tk.Button(self.master)
        self.button_%s["text"] = "%s"
        self.button_%s["command"] = self.print_%s
        self.button_%s['font'] = FONT
        self.widgets.append(self.button_%s)
        self.keys["%s"] = self.button_%s
        self.button_%s.place(x=%i, y=%i + OFFSET, width=%i, height=%i)
    """ % (number, number, number, number, number, number,
           number, number, number, number, x, y,
           BUTTON_SIZE, BUTTON_SIZE)
    return button

def generate_number_function(number):
    letter_function = """
    def print_%s(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "%s")

    """ % (number, number)
    return letter_function

s =  """
import tkinter as tk
from random import randint

DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35
FONT = ("Arial", 20)
OFFSET = 50


class FinalPage(tk.Frame):
    def __init__(self, answer, title, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets = []
        self.keys = {}
        self.answer = answer.upper()
        self.master.title(title)

    def set_previous(self, previous):
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def create_widgets(self):
        self.entry_left = tk.Entry(self.master, justify = "center")
        self.widgets.append(self.entry_left)
        self.entry_left["font"] = ("Arial", 30)
        x_pos = DIM_X / 2 - BUTTON_SIZE * 3
        y_pos = lambda x:  DIM_Y / 12 * x
        self.entry_left.place(x = x_pos,
                         y = y_pos(3) + OFFSET,
                         width = BUTTON_SIZE * 2,
                         height = BUTTON_SIZE * 2)

        x_pos = DIM_X / 2 + BUTTON_SIZE
        self.entry_right = tk.Entry(self.master, justify="center")
        self.widgets.append(self.entry_right)
        self.entry_right["font"] = ("Arial", 30)
        self.entry_right.place(x = x_pos,
                               y = y_pos(3) + OFFSET,
                               width = BUTTON_SIZE * 2,
                               height = BUTTON_SIZE * 2)

        self.first_letter = tk.Label(self.master)
        self.first_letter["text"] = "-"
        self.first_letter["font"] = ("Arial", 30)
        self.first_letter.place(x = DIM_X / 2 - 5 * BUTTON_SIZE / 2,
                                y = y_pos(2),
                                width = BUTTON_SIZE,
                                height = BUTTON_SIZE * 2)

        self.second_letter = tk.Label(self.master)
        self.second_letter["text"] = "-"
        self.second_letter["font"] = ("Arial", 30)
        self.second_letter.place(x = DIM_X / 2 -  BUTTON_SIZE / 2,
                                 y = y_pos(2),
                                 width = BUTTON_SIZE,
                                 height = BUTTON_SIZE * 2)


        self.third_letter = tk.Label(self.master)
        self.third_letter["text"] = "-"
        self.third_letter["font"] = ("Arial", 30)
        self.third_letter.place(x = DIM_X / 2 + 3 * BUTTON_SIZE / 2,
                                y = y_pos(2),
                                width = BUTTON_SIZE,
                                height = BUTTON_SIZE * 2)
        self.letters = [self.first_letter, self.second_letter, self.third_letter]

        for i in self.letters:
            self.widgets.append(i)




        self.enter = tk.Button(self.master)
        self.enter["text"] = "ENTER"
        self.enter["command"] = self.submit
        self.enter["font"] = FONT
        self.widgets.append(self.enter)
        self.enter.place(x = DIM_X / 2 - BUTTON_SIZE * 3,
                         y = BUTTON_SIZE  + DIM_Y / 2 + OFFSET,
                         width = BUTTON_SIZE * 3,
                         height = BUTTON_SIZE)

        self.backspace = tk.Button(self.master)
        self.backspace["text"] = "DELETE"
        self.backspace["command"] = self.delete
        self.backspace["font"] = FONT

        x_pos =  DIM_X / 2 + BUTTON_SIZE
        y_pos = BUTTON_SIZE  + DIM_Y / 2
        self.widgets.append(self.backspace)
        self.backspace.place(x = x_pos,
                             y = y_pos + OFFSET,
                             width = BUTTON_SIZE * 3,
                             height = BUTTON_SIZE)

        self.back = tk.Button(self.master)
        self.back["text"] = "BACK"
        self.back["command"] = self.go_back
        self.back["font"] = FONT
        self.widgets.append(self.back)
        self.back.place(x = 20, y = 20, width = BUTTON_SIZE * 3, height = BUTTON_SIZE)

        self.next_page = tk.Button(self.master)
        self.next_page["text"] = "Submit Final Answer"
        self.next_page["command"] = self.next_cmd
        self.next_page["font"] = ("Arial", 25)
        self.next_page.place(x = DIM_X / 2 - 4 * BUTTON_SIZE,
                        y = DIM_Y - 2 * BUTTON_SIZE,
                        width = 8 * BUTTON_SIZE,
                        height = BUTTON_SIZE)
        self.widgets.append(self.next_page)

"""
row = 0
column = 0
for i in letters:
    s += generate_number_button(int(i),row, column)
    column += 1


a = ord("A")
for i in range(1,10):
    s += generate_number_function(str(i))
s += """
    def submit(self):
        a = ord("A")
        l = self.entry_left.get()
        r = self.entry_right.get()
        if len(l) + len(r) != 2:
            for i in self.letters:
                i["text"] = "-"
            return
        l = int(l)
        print(l)
        r = int(r)
        if r > len(self.answer) or l > 3:
            for i in self.letters:
                 i["text"] = "-"
            return

        letter = self.answer[r-1]
        print(letter)
        for i in range(3):
            if i == l - 1:
                print(i)
                self.letters[i]["text"] = letter
            else:
                self.letters[i]["text"] = chr(a + randint(0,25))


    def go_back(self):
        self.destroy_widgets()
        self.destroy()
        self.quit()
        self.previous.create_widgets()
        self.previous.mainloop()

    def delete(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return

        index = entry.index(tk.INSERT)
        entry.delete(index -1)

    def destroy_widgets(self):
        for w in self.widgets:
            w.destroy()

    def next_cmd(self):
        self.destroy_widgets()
        self.destroy()
        self.quit()
        self.next.create_widgets()
        self.next.mainloop()


"""


f = open("final_page.py", 'w')
f.write(s)
f.close()
