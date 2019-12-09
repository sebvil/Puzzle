import tkinter as tk
from answer_page import AnswerPage
from text_page import TextPage
from final_page import FinalPage
from passport import PassportPage
from bills import BillsPage



if __name__ == "__main__":
    answers = ["Sudden",
               "Cloak",
               "Relax",
               "Blast" ,
               "Atlantic",
               "Stardust",
               "Dollar"]
    root = tk.Tk()
    root.geometry("640x460+0-20")

    pages = []
    bills_text="\n".join(["NET WORTH\n",
                   "LADY GAGA	$01,100,000",
                   "JARED LETO 	$000,011,110",
                   "BRITNEY SPEARS	$0,001,010,000,011",
                   "KIM KARDASHIAN	$0,100,000,000,001",
                   "BERNIE SANDERS	$0,000,001,010,000"])

    for i in range(1,8):
        if i == 4:
            for j in range(1,4):
                msg = open("/home/pi/Puzzle/story%i.txt" % j).read().strip()
                page = TextPage(text= msg, title= "Story", master=root)
                pages.append(page)
        msg = open("/home/pi/Puzzle/puzzle%i.txt" % i).read().strip()
        page = TextPage(text= msg, title= "Puzzle %i" % i, master=root)
        answer_page = AnswerPage(answer=answers[i-1], title = "Puzzle %i" % i, master=root)

        pages.append(page)
        if i == 2:
            passport = PassportPage(title="passport", master=root)
            pages.append(passport)
        if i == 4:
            bills = BillsPage(title="bills", text=bills_text, master=root)
            pages.append(bills)
        if i == 6:
            final_puzzle = FinalPage(answer=answers[5], title="Puzzle 6", master=root )
            pages.append(final_puzzle)
        pages.append(answer_page)




    final_page = TextPage(text= "Done", final=True, title= "Complete", master=root)
    pages.append(final_page)

    length = len(pages)
    for i in range(length):
        if i != 0:
            pages[i].set_previous(pages[i-1])
        if i < length - 1:
            pages[i].set_next(pages[i+1])

    pages[0].create_widgets()
    pages[0].mainloop()

