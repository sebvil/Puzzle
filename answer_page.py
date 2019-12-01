
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
        self.backspace.place(x=382, y=180, width=60, height=30)

        self.q = tk.Button(self.master)
        self.q["text"] = "Q"
        self.q["command"] = self.print_q
        self.q.place(x=100, y=150, width=30, height=30)
    
        self.w = tk.Button(self.master)
        self.w["text"] = "W"
        self.w["command"] = self.print_w
        self.w.place(x=130, y=150, width=30, height=30)
    
        self.e = tk.Button(self.master)
        self.e["text"] = "E"
        self.e["command"] = self.print_e
        self.e.place(x=160, y=150, width=30, height=30)
    
        self.r = tk.Button(self.master)
        self.r["text"] = "R"
        self.r["command"] = self.print_r
        self.r.place(x=190, y=150, width=30, height=30)
    
        self.t = tk.Button(self.master)
        self.t["text"] = "T"
        self.t["command"] = self.print_t
        self.t.place(x=220, y=150, width=30, height=30)
    
        self.y = tk.Button(self.master)
        self.y["text"] = "Y"
        self.y["command"] = self.print_y
        self.y.place(x=250, y=150, width=30, height=30)
    
        self.u = tk.Button(self.master)
        self.u["text"] = "U"
        self.u["command"] = self.print_u
        self.u.place(x=280, y=150, width=30, height=30)
    
        self.i = tk.Button(self.master)
        self.i["text"] = "I"
        self.i["command"] = self.print_i
        self.i.place(x=310, y=150, width=30, height=30)
    
        self.o = tk.Button(self.master)
        self.o["text"] = "O"
        self.o["command"] = self.print_o
        self.o.place(x=340, y=150, width=30, height=30)
    
        self.p = tk.Button(self.master)
        self.p["text"] = "P"
        self.p["command"] = self.print_p
        self.p.place(x=370, y=150, width=30, height=30)
    
        self.a = tk.Button(self.master)
        self.a["text"] = "A"
        self.a["command"] = self.print_a
        self.a.place(x=112, y=180, width=30, height=30)
    
        self.s = tk.Button(self.master)
        self.s["text"] = "S"
        self.s["command"] = self.print_s
        self.s.place(x=142, y=180, width=30, height=30)
    
        self.d = tk.Button(self.master)
        self.d["text"] = "D"
        self.d["command"] = self.print_d
        self.d.place(x=172, y=180, width=30, height=30)
    
        self.f = tk.Button(self.master)
        self.f["text"] = "F"
        self.f["command"] = self.print_f
        self.f.place(x=202, y=180, width=30, height=30)
    
        self.g = tk.Button(self.master)
        self.g["text"] = "G"
        self.g["command"] = self.print_g
        self.g.place(x=232, y=180, width=30, height=30)
    
        self.h = tk.Button(self.master)
        self.h["text"] = "H"
        self.h["command"] = self.print_h
        self.h.place(x=262, y=180, width=30, height=30)
    
        self.j = tk.Button(self.master)
        self.j["text"] = "J"
        self.j["command"] = self.print_j
        self.j.place(x=292, y=180, width=30, height=30)
    
        self.k = tk.Button(self.master)
        self.k["text"] = "K"
        self.k["command"] = self.print_k
        self.k.place(x=322, y=180, width=30, height=30)
    
        self.l = tk.Button(self.master)
        self.l["text"] = "L"
        self.l["command"] = self.print_l
        self.l.place(x=352, y=180, width=30, height=30)
    
        self.z = tk.Button(self.master)
        self.z["text"] = "Z"
        self.z["command"] = self.print_z
        self.z.place(x=140, y=210, width=30, height=30)
    
        self.x = tk.Button(self.master)
        self.x["text"] = "X"
        self.x["command"] = self.print_x
        self.x.place(x=170, y=210, width=30, height=30)
    
        self.c = tk.Button(self.master)
        self.c["text"] = "C"
        self.c["command"] = self.print_c
        self.c.place(x=200, y=210, width=30, height=30)
    
        self.v = tk.Button(self.master)
        self.v["text"] = "V"
        self.v["command"] = self.print_v
        self.v.place(x=230, y=210, width=30, height=30)
    
        self.b = tk.Button(self.master)
        self.b["text"] = "B"
        self.b["command"] = self.print_b
        self.b.place(x=260, y=210, width=30, height=30)
    
        self.n = tk.Button(self.master)
        self.n["text"] = "N"
        self.n["command"] = self.print_n
        self.n.place(x=290, y=210, width=30, height=30)
    
        self.m = tk.Button(self.master)
        self.m["text"] = "M"
        self.m["command"] = self.print_m
        self.m.place(x=320, y=210, width=30, height=30)
    
    def print_a(self):
        self.entry.insert(tk.INSERT, "A")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_b(self):
        self.entry.insert(tk.INSERT, "B")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_c(self):
        self.entry.insert(tk.INSERT, "C")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_d(self):
        self.entry.insert(tk.INSERT, "D")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_e(self):
        self.entry.insert(tk.INSERT, "E")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_f(self):
        self.entry.insert(tk.INSERT, "F")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_g(self):
        self.entry.insert(tk.INSERT, "G")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_h(self):
        self.entry.insert(tk.INSERT, "H")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_i(self):
        self.entry.insert(tk.INSERT, "I")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_j(self):
        self.entry.insert(tk.INSERT, "J")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_k(self):
        self.entry.insert(tk.INSERT, "K")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_l(self):
        self.entry.insert(tk.INSERT, "L")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_m(self):
        self.entry.insert(tk.INSERT, "M")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_n(self):
        self.entry.insert(tk.INSERT, "N")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_o(self):
        self.entry.insert(tk.INSERT, "O")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_p(self):
        self.entry.insert(tk.INSERT, "P")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_q(self):
        self.entry.insert(tk.INSERT, "Q")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_r(self):
        self.entry.insert(tk.INSERT, "R")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_s(self):
        self.entry.insert(tk.INSERT, "S")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_t(self):
        self.entry.insert(tk.INSERT, "T")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_u(self):
        self.entry.insert(tk.INSERT, "U")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_v(self):
        self.entry.insert(tk.INSERT, "V")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_w(self):
        self.entry.insert(tk.INSERT, "W")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_x(self):
        self.entry.insert(tk.INSERT, "X")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_y(self):
        self.entry.insert(tk.INSERT, "Y")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
    def print_z(self):
        self.entry.insert(tk.INSERT, "Z")
        self.wrong.place(x = 120, y =-50, height=50, width=240)

    
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


