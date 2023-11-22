from tkinter import *
import os
image=os.path.dirname(__file__) 
class youtube():
    def __init__(self, master=None):
        self.fontePadrao=('Arial','10')
        self.widget1 = Frame(master)
        self.widget2 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="YOUTUBE PREMIUM")
        self.msg.grid(column=1 ,row=3)
        self.msg.pack()

        self.pesquisa=Entry(self.widget1)
        self.pesquisa["width"] = 30
        self.pesquisa["font"] = self.fontePadrao
        self.pesquisa.pack(side=LEFT)

        self.buttonpesquisa= Button(self.buttonpesquisa)
        

root=Tk()
youtube(root)
root.mainloop()