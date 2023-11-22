from tkinter import *
import os 
class youtube():
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="YOUTUBE PREMIUM")
        self.msg.grid(column=1, row= 0)

root=Tk()
root.geometry("400x400") 
bg = PhotoImage(file = "Your_image.png") 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
  
label2 = Label( root, text = "Welcome") 
label2.pack(pady = 50) 
frame1 = Frame(root) 
frame1.pack(pady = 20 ) 
button1 = Button(frame1,text="Exit") 
button1.pack(pady=20) 
  
button2 = Button( frame1, text = "Start") 
button2.pack(pady = 20) 
youtube(root)
root.mainloop()