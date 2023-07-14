from textblob import TextBlob
from tkinter import *

def Correct_spelling():
    get_data=enter1.get()
    corr=TextBlob(get_data)
    data=corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)

def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x370")
    win.resizable(False,False)
    win.config(bg="Blue")
    win.title("Spell Checker")

    labell1=Label(win,text="Incorrect spelling", font=("Time New Roman",20,"bold"),bg="Blue",fg="white")
    labell1.place(x=100,y=20,height=50,width=300)

    enter1 = Entry(win,font=("Time New Roman",20,))
    enter1.place(x=50,y=80,height=50,width=400)

    
    labell2=Label(win,text="Correct spelling", font=("Time New Roman",20,"bold"),bg="Blue",fg="white")
    labell2.place(x=100,y=140,height=50,width=300)

    enter2 = Entry(win,font=("Time New Roman",20,))
    enter2.place(x=50,y=200,height=50,width=400)

    button = Button(win,text="Done",font=("Time New Roman",20,"bold"),bg="Yellow",command=Correct_spelling)
    button.place(x=150,y=260,height=50,width=200)

    win.mainloop()

main_window()