
import tkinter as tk

DIM_X = 640
DIM_Y = 460
BUTTON_SIZE = 40
WIDTH = 200
HEIGHT = 35

class FinalPage(tk.Frame):
    def __init__(self, answer, title, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets = []
        self.keys = {}
        self.create_widgets()
        self.answer = answer.upper()
        self.master.title(title)

    def create_widgets(self):
        self.entry = tk.Entry(self.master)
        self.widgets.append(self.entry)
        x_pos = DIM_X / 2 - WIDTH / 2
        y_pos = lambda x:  DIM_Y / 12 * x
        self.entry.place(x = x_pos,
                         y = y_pos(3),
                         width = WIDTH,
                         height = HEIGHT)

        self.wrong = tk.Label(self.master, text="Wrong Answer")
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

        self.backspace = tk.Button(self.master)
        self.backspace["text"] = "DELETE"
        self.backspace["command"] = self.delete
        x_pos =  (DIM_X / 2 -
                 BUTTON_SIZE * 10 / 2 +
                 BUTTON_SIZE * 9 +
                 12)
        y_pos = BUTTON_SIZE  + DIM_Y / 2
        self.widgets.append(self.backspace)
        self.backspace.place(x = x_pos, y = y_pos, width = 80, height = 40)

        self.q = tk.Button(self.master)
        self.q["text"] = "Q"
        self.q["command"] = self.print_q
        self.widgets.append(self.q)
        self.keys["Q"] = self.q
        self.q.place(x=120, y=230, width=40, height=40)
    
        self.w = tk.Button(self.master)
        self.w["text"] = "W"
        self.w["command"] = self.print_w
        self.widgets.append(self.w)
        self.keys["W"] = self.w
        self.w.place(x=160, y=230, width=40, height=40)
    
        self.e = tk.Button(self.master)
        self.e["text"] = "E"
        self.e["command"] = self.print_e
        self.widgets.append(self.e)
        self.keys["E"] = self.e
        self.e.place(x=200, y=230, width=40, height=40)
    
        self.r = tk.Button(self.master)
        self.r["text"] = "R"
        self.r["command"] = self.print_r
        self.widgets.append(self.r)
        self.keys["R"] = self.r
        self.r.place(x=240, y=230, width=40, height=40)
    
        self.t = tk.Button(self.master)
        self.t["text"] = "T"
        self.t["command"] = self.print_t
        self.widgets.append(self.t)
        self.keys["T"] = self.t
        self.t.place(x=280, y=230, width=40, height=40)
    
        self.y = tk.Button(self.master)
        self.y["text"] = "Y"
        self.y["command"] = self.print_y
        self.widgets.append(self.y)
        self.keys["Y"] = self.y
        self.y.place(x=320, y=230, width=40, height=40)
    
        self.u = tk.Button(self.master)
        self.u["text"] = "U"
        self.u["command"] = self.print_u
        self.widgets.append(self.u)
        self.keys["U"] = self.u
        self.u.place(x=360, y=230, width=40, height=40)
    
        self.i = tk.Button(self.master)
        self.i["text"] = "I"
        self.i["command"] = self.print_i
        self.widgets.append(self.i)
        self.keys["I"] = self.i
        self.i.place(x=400, y=230, width=40, height=40)
    
        self.o = tk.Button(self.master)
        self.o["text"] = "O"
        self.o["command"] = self.print_o
        self.widgets.append(self.o)
        self.keys["O"] = self.o
        self.o.place(x=440, y=230, width=40, height=40)
    
        self.p = tk.Button(self.master)
        self.p["text"] = "P"
        self.p["command"] = self.print_p
        self.widgets.append(self.p)
        self.keys["P"] = self.p
        self.p.place(x=480, y=230, width=40, height=40)
    
        self.a = tk.Button(self.master)
        self.a["text"] = "A"
        self.a["command"] = self.print_a
        self.widgets.append(self.a)
        self.keys["A"] = self.a
        self.a.place(x=132, y=270, width=40, height=40)
    
        self.s = tk.Button(self.master)
        self.s["text"] = "S"
        self.s["command"] = self.print_s
        self.widgets.append(self.s)
        self.keys["S"] = self.s
        self.s.place(x=172, y=270, width=40, height=40)
    
        self.d = tk.Button(self.master)
        self.d["text"] = "D"
        self.d["command"] = self.print_d
        self.widgets.append(self.d)
        self.keys["D"] = self.d
        self.d.place(x=212, y=270, width=40, height=40)
    
        self.f = tk.Button(self.master)
        self.f["text"] = "F"
        self.f["command"] = self.print_f
        self.widgets.append(self.f)
        self.keys["F"] = self.f
        self.f.place(x=252, y=270, width=40, height=40)
    
        self.g = tk.Button(self.master)
        self.g["text"] = "G"
        self.g["command"] = self.print_g
        self.widgets.append(self.g)
        self.keys["G"] = self.g
        self.g.place(x=292, y=270, width=40, height=40)
    
        self.h = tk.Button(self.master)
        self.h["text"] = "H"
        self.h["command"] = self.print_h
        self.widgets.append(self.h)
        self.keys["H"] = self.h
        self.h.place(x=332, y=270, width=40, height=40)
    
        self.j = tk.Button(self.master)
        self.j["text"] = "J"
        self.j["command"] = self.print_j
        self.widgets.append(self.j)
        self.keys["J"] = self.j
        self.j.place(x=372, y=270, width=40, height=40)
    
        self.k = tk.Button(self.master)
        self.k["text"] = "K"
        self.k["command"] = self.print_k
        self.widgets.append(self.k)
        self.keys["K"] = self.k
        self.k.place(x=412, y=270, width=40, height=40)
    
        self.l = tk.Button(self.master)
        self.l["text"] = "L"
        self.l["command"] = self.print_l
        self.widgets.append(self.l)
        self.keys["L"] = self.l
        self.l.place(x=452, y=270, width=40, height=40)
    
        self.z = tk.Button(self.master)
        self.z["text"] = "Z"
        self.z["command"] = self.print_z
        self.widgets.append(self.z)
        self.keys["Z"] = self.z
        self.z.place(x=160, y=310, width=40, height=40)
    
        self.x = tk.Button(self.master)
        self.x["text"] = "X"
        self.x["command"] = self.print_x
        self.widgets.append(self.x)
        self.keys["X"] = self.x
        self.x.place(x=200, y=310, width=40, height=40)
    
        self.c = tk.Button(self.master)
        self.c["text"] = "C"
        self.c["command"] = self.print_c
        self.widgets.append(self.c)
        self.keys["C"] = self.c
        self.c.place(x=240, y=310, width=40, height=40)
    
        self.v = tk.Button(self.master)
        self.v["text"] = "V"
        self.v["command"] = self.print_v
        self.widgets.append(self.v)
        self.keys["V"] = self.v
        self.v.place(x=280, y=310, width=40, height=40)
    
        self.b = tk.Button(self.master)
        self.b["text"] = "B"
        self.b["command"] = self.print_b
        self.widgets.append(self.b)
        self.keys["B"] = self.b
        self.b.place(x=320, y=310, width=40, height=40)
    
        self.n = tk.Button(self.master)
        self.n["text"] = "N"
        self.n["command"] = self.print_n
        self.widgets.append(self.n)
        self.keys["N"] = self.n
        self.n.place(x=360, y=310, width=40, height=40)
    
        self.m = tk.Button(self.master)
        self.m["text"] = "M"
        self.m["command"] = self.print_m
        self.widgets.append(self.m)
        self.keys["M"] = self.m
        self.m.place(x=400, y=310, width=40, height=40)
    
    def print_a(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "A")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_b(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "B")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_c(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "C")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_d(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "D")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_e(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "E")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_f(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "F")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_g(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "G")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_h(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "H")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_i(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "I")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_j(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "J")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_k(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "K")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_l(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "L")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_m(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "M")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_n(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "N")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_o(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "O")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_p(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "P")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_q(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "Q")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_r(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "R")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_s(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "S")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_t(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "T")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_u(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "U")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_v(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "V")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_w(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "W")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_x(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "X")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_y(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "Y")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_z(self):
        if (len(self.entry.get()) < len(self.answer)):
            self.entry.insert(tk.INSERT, "Z")
            self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def submit(self):
        attempt = self.entry.get()
        if attempt == self.answer:
            print("CORRECT")
            self.destroy_widgets()
            self.destroy()
            self.quit()
        else:
            for i in range(len(attempt)):
                if attempt[i] != self.answer[i]:
                    if i == 0:
                        color = self.master["background"]
                        self.master["background"] = "red"
                        self.master.after(1000, self.change_color, self.master, color)
                        return
                    else:
                        letter = chr(i + ord("A") - 1)
                        widget = self.keys[letter]
                        color = widget["background"]
                        widget["background"] = "green"
                        print(2)
                        widget.after(1000, self.change_color, widget, color)
                        return
                if i == len(attempt) - 1:
                    letter = chr(i + ord("A"))
                    widget = self.keys[letter]
                    color = widget["background"]
                    widget["background"] = "green"
                    print(2)
                    widget.after(1000, self.change_color, widget, color)
                    return
            print(1)

    def delete(self):
        self.wrong.place(x = DIM_X / 2 - WIDTH / 2,
                         y = -50,
                         height = HEIGHT,
                         width = WIDTH)
        index = self.entry.index(tk.INSERT)
        self.entry.delete(index -1)

    def destroy_widgets(self):
        for w in self.widgets:
            w.destroy()

    def change_color(self, widget, color):
        widget["background"] = color
