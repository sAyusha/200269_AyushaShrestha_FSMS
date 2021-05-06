from tkinter import *
from PIL import ImageTk

window=Tk()
window.title("Management System")
window.iconbitmap("D:/img/fashion.ico")
window.geometry("410x300")

bg = ImageTk.PhotoImage(file="D:/img/fashion1.jpg")
bg_label = Label(window, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title=Label(window,text="Fashion Store Management System",font=("Arial",11),bg="#ffffff",fg="black")
title.grid(row=0,column=0,padx=70,pady=1,ipady=1)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Account")
filemenu.add_command(label="Exit")
window.config(menu=menubar)

window.mainloop()