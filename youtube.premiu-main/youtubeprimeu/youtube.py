from tkinter import *
import os

pastaApp = os.path.dirname(__file__)


class youtube():
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="YOUTUBE PREMIUM")
        self.msg.grid(column=1, row= 0)
        self.logo=PhotoImage(file=pastaApp+'w = tk.Label(root, image=imagem)')
        self.labelLogo = Label(self.widget1, image=self.logo)
        self.labelLogo.grid(column=0,row=0)
root=Tk()
youtube(root)
root.mainloop()