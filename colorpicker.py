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

#color1
colors=Canvas(frame,bg="teal",width=150, height=265, bd=0)
colors.place(x=20,y=90)

id1= colors.create_rectangle((10,10,50,50), fill="black")
id2= colors.create_rectangle((10,50,50,100), fill="black")
id3= colors.create_rectangle((10,100,50,150), fill="black")
id4= colors.create_rectangle((10,150,50,200), fill="black")
id5= colors.create_rectangle((10,200,50,250), fill="black")

hex1=Label(colors, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex1.place(x=60,y=15)

hex2=Label(colors, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex2.place(x=60,y=65)

hex3=Label(colors, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex3.place(x=60,y=115)

hex4=Label(colors, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex4.place(x=60,y=165)

hex5=Label(colors, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex5.place(x=60,y=215)

#color2
colors2=Canvas(frame,bg="teal",width=150, height=265, bd=0,)
colors2.place(x=180,y=90)

id6= colors2.create_rectangle((10,10,50,50), fill="#000000")
id7= colors2.create_rectangle((10,50,50,100), fill="#000000")
id8= colors2.create_rectangle((10,100,50,150), fill="#000000")
id9= colors2.create_rectangle((10,150,50,200), fill="#000000")
id10= colors2.create_rectangle((10,200,50,250), fill="#000000")

hex6=Label(colors2, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex6.place(x=60,y=15)

hex7=Label(colors2, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex7.place(x=60,y=65)

hex8=Label(colors2, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex8.place(x=60,y=115)

hex9=Label(colors2, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex9.place(x=60,y=165)

hex10=Label(colors2, text="#000000", fg="#000",font="helvetica 12 bold", bg="white")
hex10.place(x=60,y=215)


#select image
selectimage=Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350,y=10)

f=Frame(selectimage, bd=3, bg="lightblue", width=320, height=280,relief=GROOVE)
f.place(x=10, y=10)

lbl=Label(f,bg="lightblue")
lbl.place(x=0, y=0)

Button(selectimage, text="Select Image", width=12, height=1, font="helvetica 14 bold", command=showimage).place(x=10,y=300)
Button(selectimage, text="Find Colors",width=12,height=1,font="helvetica 14 bold", command =Findcolor).place(x=176, y =300)

root.mainloop()