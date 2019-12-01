import tkinter as tk
from answer_page import AnswerPage
from text_page import TextPage



if __name__ == "__main__":
    answers = ["Rodent",
               "Cloak",
               "Relax",
               "Blast" ,
               "Atlantic",
               "Stardust"]
    root = tk.Tk()
    root.geometry("640x460+0-20")
    msg = "hbecipeub\neuiuebdu\nebbcieub"

    for i in range(6):
        page = TextPage(text= msg, title= ("Puzzle %i" % (i+1)), master=root)
        page.mainloop()
        page1 = AnswerPage(answer=answers[i], title = ("Puzzle %i" % (i+1)), master=root)
        page1.mainloop()
