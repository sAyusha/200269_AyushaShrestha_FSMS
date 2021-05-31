from tkinter import *
from tkinter import messagebox
from Home_page import *
from PIL import ImageTk

# Create the main screen and set its configuration.
window=Tk()
window.title("Management System")
window.iconbitmap("D:/img/fashion.ico")
width = 410
height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)
window.config()


bg = ImageTk.PhotoImage(file="D:/img/fashion1.jpg")
bg_label = Label(window, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title=Label(window,text="Fashion Store Management System",font=("Arial",11),bg="#ffffff",fg="black")
title.grid(row=0,column=0,padx=70,pady=1,ipady=1)

# Function to close the main screen.
def Exit():
    end = messagebox.askquestion('Confirm Exit', 'Are you sure you want to exit?',icon="warning")
    if end == 'yes':
        window.destroy()
        exit()

# create a login page and set its configuration.
def Login_here():
    global login
    login=Toplevel()
    login.title("Login Page")
    login.iconbitmap("D:/img/fashion.ico")
    width = 370
    height = 334
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    login.geometry("%dx%d+%d+%d" % (width, height, x, y))
    login.resizable(0, 0)
    login.config()
    LoginPage()

# create the various types of menu
# just under the title bar of main window.
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Account", command=Login_here)
filemenu.add_command(label="Exit", command=Exit)
window.config(menu=menubar)

# Create a frame and do the editing of login.
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

    # globally declared the variable for all functions.
    global user_name
    global pass_word
    global usr_entry
    global pwd_entry
    global username
    global password
    global output

    username=StringVar()
    password=StringVar()

    # defining and keeping the username login and entry box  in particular place inside the login frame.
    user_name=Label(log_frame,text="Username",bg="#ffffff",font=("Times New Roman",12),fg="#212121")
    user_name.place(x=25,y=70)
    usr_entry=Entry(log_frame,text=username,bg="#ffffff")
    usr_entry.place(x=25,y=95,width=190,height=24)

    # defining and keeping the password login and entry box in particular place inside login frame.
    pass_word=Label(log_frame,text="Password",bg="#ffffff",font=("Times New Roman",12),fg="#212121")
    pass_word.place(x=25,y=125)
    pwd_entry=Entry(log_frame,text=password,bg="#ffffff",show="*")
    pwd_entry.place(x=25,y=150,width=190,height=24)
    output = Label(login, text="", font=('Times New Roman', 11))
    output.place(x=70,y=280)
    log_button=Button(login,text="Login",font=("Times New Roman",14),bg="#006064",fg="#ffffff",command=login_button)
    log_button.place(x=147,y=248,width=70,height=25)
    log_button.bind('<Return>', login_button)

# function to authenticate the login credentials details with login button.
def login_button():
    usr = username.get()
    pw = password.get()
    if usr == "admin" and pw == "admin1":
        ShowHome()
    elif usr == "" and pw == "":
        output.config(text="Please enter the credentials to login!", fg="#000000")
    else:
        output.config(text="Invalid username and password!!", fg="#000000")

def ShowHome():
    """ Function that is defined by ShowHome to display home page and close login page. """
    window.withdraw()
    Home()
    login.destroy()

# start the program.
window.mainloop()