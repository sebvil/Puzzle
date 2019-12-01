
import tkinter as tk

class AnswerPage(tk.Frame):
    def __init__(self, answer, title, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets = []
        self.create_widgets()
        self.answer = answer.upper()
        self.master.title(title)

    def create_widgets(self):
        self.entry = tk.Entry(self.master)
        self.widgets.append(self.entry)
        self.entry.place(x = 220, y = 100, width=200, height=30)

        self.wrong = tk.Label(self.master, text="Wrong Answer")
        self.widgets.append(self.wrong)
        self.wrong.place(x = 200, y = -50, height=50, width=240)

        self.enter = tk.Button(self.master)
        self.enter["text"] = "SUBMIT"
        self.enter["command"] = self.submit
        self.widgets.append(self.enter)
        self.enter.place(x=220, y=150, width=200, height=30)

        self.backspace = tk.Button(self.master)
        self.backspace["text"] = "DELETE"
        self.backspace["command"] = self.delete
        self.widgets.append(self.backspace)
        self.backspace.place(x=492, y=240, width=80, height=40)

        self.q = tk.Button(self.master)
        self.q["text"] = "Q"
        self.q["command"] = self.print_q
        self.widgets.append(self.q)
        self.q.place(x=120, y=200, width=40, height=40)
    
        self.w = tk.Button(self.master)
        self.w["text"] = "W"
        self.w["command"] = self.print_w
        self.widgets.append(self.w)
        self.w.place(x=160, y=200, width=40, height=40)
    
        self.e = tk.Button(self.master)
        self.e["text"] = "E"
        self.e["command"] = self.print_e
        self.widgets.append(self.e)
        self.e.place(x=200, y=200, width=40, height=40)
    
        self.r = tk.Button(self.master)
        self.r["text"] = "R"
        self.r["command"] = self.print_r
        self.widgets.append(self.r)
        self.r.place(x=240, y=200, width=40, height=40)
    
        self.t = tk.Button(self.master)
        self.t["text"] = "T"
        self.t["command"] = self.print_t
        self.widgets.append(self.t)
        self.t.place(x=280, y=200, width=40, height=40)
    
        self.y = tk.Button(self.master)
        self.y["text"] = "Y"
        self.y["command"] = self.print_y
        self.widgets.append(self.y)
        self.y.place(x=320, y=200, width=40, height=40)
    
        self.u = tk.Button(self.master)
        self.u["text"] = "U"
        self.u["command"] = self.print_u
        self.widgets.append(self.u)
        self.u.place(x=360, y=200, width=40, height=40)
    
        self.i = tk.Button(self.master)
        self.i["text"] = "I"
        self.i["command"] = self.print_i
        self.widgets.append(self.i)
        self.i.place(x=400, y=200, width=40, height=40)
    
        self.o = tk.Button(self.master)
        self.o["text"] = "O"
        self.o["command"] = self.print_o
        self.widgets.append(self.o)
        self.o.place(x=440, y=200, width=40, height=40)
    
        self.p = tk.Button(self.master)
        self.p["text"] = "P"
        self.p["command"] = self.print_p
        self.widgets.append(self.p)
        self.p.place(x=480, y=200, width=40, height=40)
    
        self.a = tk.Button(self.master)
        self.a["text"] = "A"
        self.a["command"] = self.print_a
        self.widgets.append(self.a)
        self.a.place(x=132, y=240, width=40, height=40)
    
        self.s = tk.Button(self.master)
        self.s["text"] = "S"
        self.s["command"] = self.print_s
        self.widgets.append(self.s)
        self.s.place(x=172, y=240, width=40, height=40)
    
        self.d = tk.Button(self.master)
        self.d["text"] = "D"
        self.d["command"] = self.print_d
        self.widgets.append(self.d)
        self.d.place(x=212, y=240, width=40, height=40)
    
        self.f = tk.Button(self.master)
        self.f["text"] = "F"
        self.f["command"] = self.print_f
        self.widgets.append(self.f)
        self.f.place(x=252, y=240, width=40, height=40)
    
        self.g = tk.Button(self.master)
        self.g["text"] = "G"
        self.g["command"] = self.print_g
        self.widgets.append(self.g)
        self.g.place(x=292, y=240, width=40, height=40)
    
        self.h = tk.Button(self.master)
        self.h["text"] = "H"
        self.h["command"] = self.print_h
        self.widgets.append(self.h)
        self.h.place(x=332, y=240, width=40, height=40)
    
        self.j = tk.Button(self.master)
        self.j["text"] = "J"
        self.j["command"] = self.print_j
        self.widgets.append(self.j)
        self.j.place(x=372, y=240, width=40, height=40)
    
        self.k = tk.Button(self.master)
        self.k["text"] = "K"
        self.k["command"] = self.print_k
        self.widgets.append(self.k)
        self.k.place(x=412, y=240, width=40, height=40)
    
        self.l = tk.Button(self.master)
        self.l["text"] = "L"
        self.l["command"] = self.print_l
        self.widgets.append(self.l)
        self.l.place(x=452, y=240, width=40, height=40)
    
        self.z = tk.Button(self.master)
        self.z["text"] = "Z"
        self.z["command"] = self.print_z
        self.widgets.append(self.z)
        self.z.place(x=160, y=280, width=40, height=40)
    
        self.x = tk.Button(self.master)
        self.x["text"] = "X"
        self.x["command"] = self.print_x
        self.widgets.append(self.x)
        self.x.place(x=200, y=280, width=40, height=40)
    
        self.c = tk.Button(self.master)
        self.c["text"] = "C"
        self.c["command"] = self.print_c
        self.widgets.append(self.c)
        self.c.place(x=240, y=280, width=40, height=40)
    
        self.v = tk.Button(self.master)
        self.v["text"] = "V"
        self.v["command"] = self.print_v
        self.widgets.append(self.v)
        self.v.place(x=280, y=280, width=40, height=40)
    
        self.b = tk.Button(self.master)
        self.b["text"] = "B"
        self.b["command"] = self.print_b
        self.widgets.append(self.b)
        self.b.place(x=320, y=280, width=40, height=40)
    
        self.n = tk.Button(self.master)
        self.n["text"] = "N"
        self.n["command"] = self.print_n
        self.widgets.append(self.n)
        self.n.place(x=360, y=280, width=40, height=40)
    
        self.m = tk.Button(self.master)
        self.m["text"] = "M"
        self.m["command"] = self.print_m
        self.widgets.append(self.m)
        self.m.place(x=400, y=280, width=40, height=40)
    
    def print_a(self):
        self.entry.insert(tk.INSERT, "A")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_b(self):
        self.entry.insert(tk.INSERT, "B")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_c(self):
        self.entry.insert(tk.INSERT, "C")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_d(self):
        self.entry.insert(tk.INSERT, "D")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_e(self):
        self.entry.insert(tk.INSERT, "E")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_f(self):
        self.entry.insert(tk.INSERT, "F")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_g(self):
        self.entry.insert(tk.INSERT, "G")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_h(self):
        self.entry.insert(tk.INSERT, "H")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_i(self):
        self.entry.insert(tk.INSERT, "I")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_j(self):
        self.entry.insert(tk.INSERT, "J")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_k(self):
        self.entry.insert(tk.INSERT, "K")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_l(self):
        self.entry.insert(tk.INSERT, "L")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_m(self):
        self.entry.insert(tk.INSERT, "M")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_n(self):
        self.entry.insert(tk.INSERT, "N")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_o(self):
        self.entry.insert(tk.INSERT, "O")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_p(self):
        self.entry.insert(tk.INSERT, "P")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_q(self):
        self.entry.insert(tk.INSERT, "Q")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_r(self):
        self.entry.insert(tk.INSERT, "R")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_s(self):
        self.entry.insert(tk.INSERT, "S")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_t(self):
        self.entry.insert(tk.INSERT, "T")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_u(self):
        self.entry.insert(tk.INSERT, "U")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_v(self):
        self.entry.insert(tk.INSERT, "V")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_w(self):
        self.entry.insert(tk.INSERT, "W")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_x(self):
        self.entry.insert(tk.INSERT, "X")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_y(self):
        self.entry.insert(tk.INSERT, "Y")
        self.wrong.place(x = 200, y =-50, height=50, width=240)

    
    def print_z(self):
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
            self.wrong.place(x = 120, y = 20, height=25, width=240)
            print(1)

    def delete(self):
        self.wrong.place(x = 120, y = -50, height=25, width=240)
        index = self.entry.index(tk.INSERT)
        self.entry.delete(index -1)

    def destroy_widgets(self):
        for w in self.widgets:
            w.destroy()


