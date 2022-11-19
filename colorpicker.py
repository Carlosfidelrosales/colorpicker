from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title("Color Picker")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)

#icon
imageIcon = PhotoImage(file="icon.png")
root.iconphoto(False, imageIcon)

Label(root,width=120,height=10, bg ="red").pack()

#frame
frame = Frame(root, width=700, height=370, bg="white")
frame.place(x=50,y=50)

logo=PhotoImage(file="logo.png")
Label(frame, image=logo, bg="white").place(x=10, y=10)

Label(frame, text="COLOR FINDER", font="helvetica 23 bold", bg ="white").place(x=100,y=20)


root.mainloop()