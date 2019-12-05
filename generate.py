letters = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]
offsets = [0, 12, 40]
DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40

def generate_letter_button(letter, r, c, offset):
    y = BUTTON_SIZE * r + DIM_Y / 2
    initial_x = DIM_X / 2 - BUTTON_SIZE * len(letters[0]) / 2
    x = BUTTON_SIZE * c + initial_x  + offset
    s = letter.lower()
    button = """
        self.%s = tk.Button(self.master)
        self.%s["text"] = "%s"
        self.%s["command"] = self.print_%s
        self.%s["font"] = FONT
        self.widgets.append(self.%s)
        self.%s.place(x=%i, y=%i, width=%i, height=%i)
    """ % (s, s, letter, s, s, s, s, s, x, y, BUTTON_SIZE, BUTTON_SIZE)
    return button

def generate_letter_function(letter):
    s = letter.lower()
    letter_function = """
    def print_%s(self):
        self.entry.insert(tk.INSERT, "%s")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    """ % (s, letter)
    return letter_function

s =  """
import tkinter as tk

DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35
FONT = ("Arial", 20)

class AnswerPage(tk.Frame):
    def __init__(self, answer, title, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets = []
        self.answer = answer.upper()
        self.master.title(title)

    def set_previous(self, previous):
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def create_widgets(self):
        self.entry = tk.Entry(self.master)
        self.widgets.append(self.entry)
        x_pos = DIM_X / 2 - WIDTH / 2
        y_pos = lambda x:  DIM_Y / 12 * x
        self.entry.place(x = x_pos,
                         y = y_pos(3),
                         width = WIDTH,
                         height = HEIGHT)
        self.entry['font'] = FONT


        self.wrong = tk.Label(self.master,
                              text="Wrong Answer",
                              font=FONT)
        self.widgets.append(self.wrong)
        self.wrong.place(x = x_pos,
                         y = -50,
                         height = HEIGHT,
                         width = WIDTH)


        self.enter = tk.Button(self.master)
        self.enter["text"] = "SUBMIT"
        self.enter["command"] = self.submit
        self.widgets.append(self.enter)
        self.enter.place(x = x_pos,
                         y = y_pos(4),
                         width = WIDTH,
                         height = HEIGHT)
        self.enter["font"] = FONT

        self.backspace = tk.Button(self.master)
        self.backspace["text"] = "DELETE"
        self.backspace["command"] = self.delete
        self.backspace["font"] = FONT

        x_pos =  (DIM_X / 2 -
                 BUTTON_SIZE * %i / 2 +
                 BUTTON_SIZE * %i +
                 12)
        y_pos = BUTTON_SIZE  + DIM_Y / 2
        self.widgets.append(self.backspace)
        self.backspace.place(x = x_pos, y = y_pos, width = %i, height = %i)

        self.back = tk.Button(self.master)
        self.back["text"] = "BACK"
        self.back["command"] = self.go_back
        self.back["font"] = FONT
        self.widgets.append(self.back)
        self.back.place(x = 20, y = 20, width = BUTTON_SIZE * 3, height = BUTTON_SIZE)
""" % (len(letters[0]), len(letters[1]), BUTTON_SIZE * 3, BUTTON_SIZE)
row = 0
column = 0
offset = 0
for i in letters:
    for j in i:
        s += generate_letter_button(j,row, column, offsets[row])
        column += 1
    row += 1
    column = 0

a = ord("A")
for i in range(26):
    s += generate_letter_function(chr(i + a))
s += """
    def submit(self):
        attempt = self.entry.get()
        if attempt == self.answer:
            print("CORRECT")
            self.destroy_widgets()
            self.destroy()
            self.quit()
            self.next.create_widgets()
            self.next.mainloop()
        else:
            self.wrong.place(x = DIM_X / 2 - WIDTH / 2,
                             y = DIM_Y / 12 * 2,
                             height= HEIGHT,
                             width= WIDTH)
            print(self.answer)

    def delete(self):
        self.wrong.place(x = DIM_X / 2 - WIDTH / 2,
                         y = -50,
                         height = HEIGHT,
                         width = WIDTH)
        index = self.entry.index(tk.INSERT)
        self.entry.delete(index -1)

    def go_back(self):
        self.destroy_widgets()
        self.destroy()
        self.quit()
        self.previous.create_widgets()
        self.previous.mainloop()

    def destroy_widgets(self):
        for w in self.widgets:
            w.destroy()


"""


f = open("answer_page.py", 'w')
f.write(s)
f.close()
