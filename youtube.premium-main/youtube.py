from tkinter import *

class youtube():
    def __init__(self, master=None):
        self.fontePadrao=('Arial','10')
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.widget2 = Frame(master)
        self.widget2.pack()

        self.widget3 = Frame(master)
        self.widget3.pack()

     
        
        self.msg = Label(self.widget1, text="YOUTUBE PREMIUM")
        self.msg.grid(column=1 ,row=0)
        self.msg.pack()

        self.pesquisa=Entry(self.widget2)
        self.pesquisa["width"] = 30
        self.pesquisa["font"] = self.fontePadrao
        self.pesquisa.grid(column=1,row=2)

        self.buttonpesquisa= Button(self.widget3)
        self.buttonpesquisa["text"] = "pesquisa"
        self.buttonpesquisa["font"] = self.fontePadrao
        self.buttonpesquisa["width"] = 10
        self.buttonpesquisa.grid(column=1,row=5)    
    
root=Tk()
youtube(root)
root.mainloop()