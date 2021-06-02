import supplier
import viewpage
from viewpage import *
from supplier import *
from tkinter import *
from tkinter import messagebox

# Function to create a frame
# and various types of menus
# and set the configuration of home page.
def Home():
    global Home
    Home = Tk()
    Home.title("Home Page")
    width = 730
    height = 470
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Home.config()

    Title = Frame(Home, relief=SOLID, bd=1)
    Title.pack(pady=10)
    title_label = Label(Title, text="Fashion Store Management System",bg="#eeeeee", font=('Times New Roman', 20))
    title_label.pack()

# Creates the mini frame for keeping the record of the suppliers, products and total purchase amount reports.
    report_frame = Frame(Home, width=710, height=370, bg="#f5f5f5", highlightthickness=2,highlightbackground='#000000')
    report_frame.place(x=10, y=70)

    product_report_frame = Frame(Home, width=220, height=110, bg="#d84315", highlightthickness=2,
                                  highlightbackground='#000000')
    product_report_frame.place(x=80, y=120)
    productReportData = viewpage.count_products()
    productReportData = Label(product_report_frame, text=productReportData, font=('Calibre', 35, 'bold'),
                              bg='#d84315', fg='#ffffff')
    productReportData .place(x=20, y=40)
    label = Label(product_report_frame, text="Total Products", font=('Roboto', 10, 'bold'),
                  bg='#d84315', fg='#ffffff')
    label.place(x=20, y=5)


    supplier_report_frame = Frame(Home, width=230, height=110, bg="#2e7d32", highlightthickness=2,
                                  highlightbackground='#000000')
    supplier_report_frame.place(x=440, y=120)
    supplierReportData = supplier.count_suppliers()
    supplierReportData = Label(supplier_report_frame, text=supplierReportData, font=('Calibre', 35, 'bold'),
                                 bg='#2e7d32', fg='#ffffff')
    supplierReportData.place(x=20, y=40)
    label2 = Label(supplier_report_frame, text="Total Suppliers", font=('Roboto', 10, 'bold'), bg='#2e7d32',
                       fg='#ffffff')
    label2.place(x=20, y=5)

    total_report_frame = Frame(Home, width=230, height=110, bg="#b71c1c", highlightthickness=2,
                                 highlightbackground='#000000')
    total_report_frame.place(x=245, y=290)
    amountReportData = viewpage.TotalAmount()
    amount = Label(total_report_frame, text="Rs.", font=('Roboto', 20, 'bold'), bg='#b71c1c', fg='#ffffff')
    amount.place(x=15, y=60)
    amountReportData = Label(total_report_frame, text=amountReportData, font=('Calibre', 20, 'bold'),
                                bg='#b71c1c', fg='#ffffff')
    amountReportData.place(x=65, y=61)
    label3 = Label(total_report_frame, text="Total Purchase Amount", font=('Roboto', 10, 'bold'),
                        bg='#b71c1c', fg='#ffffff')
    label3.place(x=20, y=21)

    menubar = Menu(Home)
    filemenu1 = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Account", menu=filemenu1)
    menubar.add_cascade(label="Store", menu=filemenu2)

    filemenu1.add_command(label="Exit",command=close)

    filemenu2.add_command(label="Product",command=click)
    filemenu2.add_command(label="Supplier",command=sup_list)

    Home.config(menu=menubar)
    Home.config(bg="#ffffff")


def close():
    """ Function defined by close to close the home page."""
    end = messagebox.askquestion('Confirm Exit', 'Are you sure you want to exit?', icon="warning")
    if end == 'yes':
        Home.destroy()
        exit()
