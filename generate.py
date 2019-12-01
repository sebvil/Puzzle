letters = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]
def generate_letter_button(letter, r, c, offset):
    size = 30
    y = size * r + 150
    x = size * c + 100 + offset
    s = letter.lower()
    button = """
        self.%s = tk.Button(self.master)
        self.%s["text"] = "%s"
        self.%s["command"] = self.print_%s
        self.%s.place(x=%i, y=%i, width=%i, height=%i)
    """ % (s, s, letter, s, s, s, x, y, size, size)
    return button

def generate_letter_function(letter):
    s = letter.lower()
    letter_function = """
    def print_%s(self):
        self.entry.insert(tk.INSERT, "%s")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    """ % (s, letter)
    return letter_function

size = 30
y = 150 + size
x = size * len(letters[1]) + 100 + 12
s =  """
import tkinter as tk

class AnswerPage(tk.Frame):
    def __init__(self, answer, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.answer = answer.upper()

    def create_widgets(self):
        self.entry = tk.Entry(self.master)
        self.entry.place(x = 140, y = 100, width=200, height=30)

        self.wrong = tk.Label(self.master, text="Wrong Answer")
        self.wrong.place(x = 120, y = -50, height=50, width=240)

        self.enter = tk.Button(self.master)
        self.enter["text"] = "SUBMIT"
        self.enter["command"] = self.submit
        self.enter.place(x=140, y=150, width=200, height=30)

        self.backspace = tk.Button(self.master)
        self.backspace["text"] = "DELETE"
        self.backspace["command"] = self.delete
        self.backspace.place(x=%i, y=%i, width=%i, height=%i)
""" % (x, y, size * 2, size)
row = 0
column = 0
offset = 0
for i in letters:
    for j in i:
        s += generate_letter_button(j,row, column, offset)
        column += 1
    if row == 0:
        offset = 12
    if row == 1:
        offset = 40
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
            self.quit()
        else:
            self.wrong.place(x = 120, y = 50, height=50, width=240)
            print(1)

    def delete(self):
        index = self.entry.index(tk.INSERT)
        self.entry.delete(index -1)


"""


f = open("answer_page.py", 'w')
f.write(s)
f.close()
