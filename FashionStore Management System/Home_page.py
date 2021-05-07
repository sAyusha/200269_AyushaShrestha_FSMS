from tkinter import *
from tkinter import messagebox

def close():
    end = messagebox.askquestion('Confirm Exit', 'Are you sure you want to exit?', icon="warning")
    if end == 'yes':
        Home.destroy()
        exit()

def Home():
    global Home
    Home = Tk()
    Home.title("Home Page")
    Home.geometry("730x470")

    Title = Frame(Home, relief=SOLID, bd=1)
    Title.pack(pady=10)
    title_label = Label(Title, text="Fashion Store Management System",bg="#eeeeee", font=('Times New Roman', 20))
    title_label.pack()

    menubar = Menu(Home)
    filemenu1 = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Account", menu=filemenu1)
    menubar.add_cascade(label="Store", menu=filemenu2)
    menubar.add_cascade(label="Billing",menu=filemenu3)

    filemenu1.add_command(label="Exit",command=close)

    filemenu2.add_command(label="Product",command=click)
    filemenu2.add_command(label="Supplier",command=sup_list)
    filemenu3.add_command(label="BillInsert",command=Bill)

    Home.config(menu=menubar)
    Home.config(bg="#ffffff")

