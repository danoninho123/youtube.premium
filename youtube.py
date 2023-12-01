from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from video import abrirYoutube



root=tk.Tk()
titulo=Label(root, text='Youtubanana', font=('Arial',40))
titulo.grid(column=1,row=0, padx=30,pady=30)
imagem = Image.open('youtubelogo.png')
imagem = imagem.resize((117,83))
imagemTK = ImageTk.PhotoImage(imagem)
w = Label(root, image=imagemTK)
w.grid(column=0,row=0)
videos=StringVar()
pesquisa=Entry(root, textvariable=videos)
pesquisa['width']=50
pesquisa.grid(column=1,row=2)
botao= Button(root, text='pesquisa', command=lambda: abrirYoutube(pesquisa.get()))
botao.grid(column=1,row=3)

    
root.mainloop()
