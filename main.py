from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("TxtPr")
fenetre.configure(bg="grey1")
fenetre.geometry("1200x700")


def op():
    with open("file.pr", "r+") as file:
        lignes = file.readlines()
        msg = ''
        for line in lignes:
            msg = msg + ' , ' + line
            msg = msg.replace(",", "")
            label.configure(text=msg)


def sa():
    test = E1.get("1.0",END)
    with open("file.pr", "w+") as file:
        file.write(test)


MenuBar = Menu(fenetre)

Files = Menu(MenuBar, tearoff=0)
Files.add_command(label="Open", command=op)

Files.add_command(label="Save", command=sa)
Files.add_command(label="Leave", command=fenetre.quit)

MenuBar.add_cascade(label="Files", menu=Files)

E1 = Text(fenetre, bd=2, bg="thistle3", width=65, height=36)
E1.pack(side = LEFT) 

label = Label(fenetre, text="Click on Files > Open to read the text", width = 78, height = 38)
label.pack(side = RIGHT)

fenetre.config(menu=MenuBar)
fenetre.mainloop()