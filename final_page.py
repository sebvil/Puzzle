
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


        self.button_1 = tk.Button(self.master)
        self.button_1["text"] = "1"
        self.button_1["command"] = self.print_1
        self.button_1['font'] = FONT
        self.widgets.append(self.button_1)
        self.keys["1"] = self.button_1
        self.button_1.place(x=140, y=230 + OFFSET, width=40, height=40)
    
        self.button_2 = tk.Button(self.master)
        self.button_2["text"] = "2"
        self.button_2["command"] = self.print_2
        self.button_2['font'] = FONT
        self.widgets.append(self.button_2)
        self.keys["2"] = self.button_2
        self.button_2.place(x=180, y=230 + OFFSET, width=40, height=40)
    
        self.button_3 = tk.Button(self.master)
        self.button_3["text"] = "3"
        self.button_3["command"] = self.print_3
        self.button_3['font'] = FONT
        self.widgets.append(self.button_3)
        self.keys["3"] = self.button_3
        self.button_3.place(x=220, y=230 + OFFSET, width=40, height=40)
    
        self.button_4 = tk.Button(self.master)
        self.button_4["text"] = "4"
        self.button_4["command"] = self.print_4
        self.button_4['font'] = FONT
        self.widgets.append(self.button_4)
        self.keys["4"] = self.button_4
        self.button_4.place(x=260, y=230 + OFFSET, width=40, height=40)
    
        self.button_5 = tk.Button(self.master)
        self.button_5["text"] = "5"
        self.button_5["command"] = self.print_5
        self.button_5['font'] = FONT
        self.widgets.append(self.button_5)
        self.keys["5"] = self.button_5
        self.button_5.place(x=300, y=230 + OFFSET, width=40, height=40)
    
        self.button_6 = tk.Button(self.master)
        self.button_6["text"] = "6"
        self.button_6["command"] = self.print_6
        self.button_6['font'] = FONT
        self.widgets.append(self.button_6)
        self.keys["6"] = self.button_6
        self.button_6.place(x=340, y=230 + OFFSET, width=40, height=40)
    
        self.button_7 = tk.Button(self.master)
        self.button_7["text"] = "7"
        self.button_7["command"] = self.print_7
        self.button_7['font'] = FONT
        self.widgets.append(self.button_7)
        self.keys["7"] = self.button_7
        self.button_7.place(x=380, y=230 + OFFSET, width=40, height=40)
    
        self.button_8 = tk.Button(self.master)
        self.button_8["text"] = "8"
        self.button_8["command"] = self.print_8
        self.button_8['font'] = FONT
        self.widgets.append(self.button_8)
        self.keys["8"] = self.button_8
        self.button_8.place(x=420, y=230 + OFFSET, width=40, height=40)
    
        self.button_9 = tk.Button(self.master)
        self.button_9["text"] = "9"
        self.button_9["command"] = self.print_9
        self.button_9['font'] = FONT
        self.widgets.append(self.button_9)
        self.keys["9"] = self.button_9
        self.button_9.place(x=460, y=230 + OFFSET, width=40, height=40)
    
    def print_1(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "1")

    
    def print_2(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "2")

    
    def print_3(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "3")

    
    def print_4(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "4")

    
    def print_5(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "5")

    
    def print_6(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "6")

    
    def print_7(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "7")

    
    def print_8(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "8")

    
    def print_9(self):
        entry = self.master.focus_get()
        if isinstance(entry, tk.Tk):
            return
        if (len(entry.get()) < 1):
            entry.insert(tk.INSERT, "9")

    
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


