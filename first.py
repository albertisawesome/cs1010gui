from tkinter import *
import wikipedia


def search():
 entry_value = entry.get()
 answer.delete(1.0, END)
 try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
 except:
        answer.insert(INSERT, "please check you input or internet connection")

root = Tk()
root.geometry('500x300')
root.configure(bg='green')





topframe = Frame(root, bg='#80c1ff', bd=5, padx=2)
topframe.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n', height=-2)
entry = Entry(topframe, width="50")
entry.pack()
button = Button(topframe, text="search", command=search, font="Arial 10")
button.pack()
topframe.pack(side = TOP)


bottomframe = Frame(root)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer = Text(bottomframe, width=30, height=100, yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

root.mainloop()

