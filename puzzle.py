import tkinter as tk
from answer_page import AnswerPage
from text_page import TextPage
from final_page import FinalPage



if __name__ == "__main__":
    answers = ["Rodent",
               "Cloak",
               "Relax",
               "Blast" ,
               "Atlantic",
               "Stardust"]
    root = tk.Tk()
    root.geometry("640x460+0-20")

    for i in range(1,6):
        msg = open("~/Puzzle/puzzle%i.txt" % i).read()
        page = TextPage(text= msg, title= "Puzzle %i" % i, master=root)
        page.mainloop()
        page1 = AnswerPage(answer=answers[i-1], title = "Puzzle %i" % i, master=root)
        page1.mainloop()

    msg = open("~/Puzzle/puzzle6.txt").read()
    page = TextPage(text= msg, title= ("Puzzle %i" % (6)), master=root)
    page.mainloop()
    page1 = FinalPage(answer=answers[5], title = ("Puzzle %i" % (6)), master=root)
    page1.mainloop()
    page = TextPage(text="You have solved the puzzle", title='Done', final=True, master=root)
    page.mainloop()