from Home_page import *
from tkinter import *
from tkinter import messagebox
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

def Exit():
    end = messagebox.askquestion('Confirm Exit', 'Are you sure you want to exit?',icon="warning")
    if end == 'yes':
        window.destroy()
        exit()

def Login_here():
    global login
    login=Toplevel()
    login.title("Login Page")
    login.iconbitmap("D:/img/fashion.ico")
    login.geometry("370x334")
    LoginPage()

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Account", command=Login_here)
filemenu.add_command(label="Exit", command=Exit)
window.config(menu=menubar)

def LoginPage():
    global log_frame
    log_frame = Frame(login, width=250, height=200, bg="#ffffff")
    log_frame.place(x=60, y=60)

    # creates a heading for main window.
    title = Label(login, text="Login Page", font=("Impact", 16, "bold"), bg="#ffffff", fg="#006064")
    title.place(x=85, y=65)
    # creates a sub heading for login frame.
    admin = Label(log_frame, text="Admin Login Area", font=("Old Sans Condensed", 11, "bold"), bg="#ffffff",
                  fg="#006064")
    admin.place(x=25, y=40)

 #gloablly declared the variable for all functions.
    global user_name
    global pass_word
    global usr_entry
    global pwd_entry
    global username
    global password

    username=StringVar()
    password=StringVar()

    #defining and kepping the username login and entry box  in particular place inside the login frame.
    user_name=Label(log_frame,text="Username",bg="#ffffff",font=("Times New Roman",12),fg="#212121")
    user_name.place(x=25,y=70)
    usr_entry=Entry(log_frame,text=username,bg="#ffffff")
    usr_entry.place(x=25,y=95,width=190,height=24)

    #defining and kepping the password login and entry box in particular place inside login frame.
    pass_word=Label(log_frame,text="Password",bg="#ffffff",font=("Times New Roman",12),fg="#212121")
    pass_word.place(x=25,y=125)
    pwd_entry=Entry(log_frame,text=password,bg="#ffffff",show="*")
    pwd_entry.place(x=25,y=150,width=190,height=24)

    log_button=Button(login,text="Login",font=("Times New Roman",14),bg="#006064",fg="#ffffff",command=login_button)
    log_button.place(x=147,y=248,width=70,height=25)
    log_button.bind('<Return>', login_button)

def login_button():
    usr = username.get()
    pw = password.get()
    if usr == "admin" and pw == "admin1":
        ShowHome()
    elif usr == "" and pw == "":
        messagebox.showinfo("", "cannot be kept empty")
    else:
        messagebox.showinfo("", "invalid username or password")

def ShowHome():
    window.withdraw()
    Home()
    login.destroy()

window.mainloop()