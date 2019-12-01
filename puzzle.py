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
    root.geometry("480x280+0+0")

    for i in range(6):
        page = AnswerPage(answer=answers[i], master=root)
        page.mainloop()
