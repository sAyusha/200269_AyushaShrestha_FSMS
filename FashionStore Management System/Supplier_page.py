from tkinter import *
from tkinter import ttk

def sup_list():
    global supp
    supp=Toplevel()
    supp.title("Suppliers Page")
    supp.iconbitmap("D:/img/fashion.ico")
    supp.geometry("850x450")
    supp.config(bg="#ffffff")
    SupplierPage()

def SupplierPage():
    global tree
    global supp_name
    global pan_no
    global contact

    frame1=Frame(supp,width=300,relief=SOLID,bd=1)
    frame1.pack(side=TOP,fill=X)
    label1=Label(frame1,text="Supplier List", font=('Times New Roman', 15), width=300,bg="#fb8c00",fg="#212121")
    label1.pack(fill=X)
    frame2=Frame(supp, width=100,bg="#000000")
    frame2.pack(side=LEFT, fill=Y)
    label2 = Label(frame2, text="Suppliers", font=('Roboto', 12),bg="#000000",fg="#ffffff")
    label2.pack(side=TOP)
    frame3=Frame(supp,width=500)
    frame3.pack(side=RIGHT)
    x = Scrollbar(frame3, orient=HORIZONTAL)
    y = Scrollbar(frame3, orient=VERTICAL)
    tree = ttk.Treeview(frame3, columns=("Supplier Name", "Pan No", "Contact No"),
                        selectmode="extended", height=20, yscrollcommand=y.set, xscrollcommand=x.set)
    y.config(command=tree.yview)
    y.pack(side=RIGHT,fill=Y)
    x.config(command=tree.xview)
    x.pack(side=BOTTOM,fill=X)
    tree.heading('#0', text='Supplier Name')
    tree.heading('#1', text='Pan No')
    tree.heading('#2', text='Contact No')
    tree.column('#0', stretch=YES, width=200)
    tree.column('#1', stretch=YES, width=180)
    tree.column('#2', stretch=YES, width=200)
    tree.pack()


    supplier_name=StringVar()
    pan_no=StringVar()
    contact=StringVar()

    name = Label(frame2, text="Supplier Name:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    name.pack(side=TOP,padx=10,anchor=W)
    name_ety = Entry(frame2, text=supplier_name, bg="#ffffff")
    name_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    pan = Label(frame2, text="Pan No:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    pan.pack(side=TOP,padx=10,anchor=W)
    pan_ety = Entry(frame2, text=pan_no, bg="#ffffff")
    pan_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    conc = Label(frame2, text="Contact No:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    conc.pack(side=TOP,padx=10,anchor=W)
    conc_ety = Entry(frame2, text=contact, bg="#ffffff")
    conc_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    s_btn = Button(frame2, text="Search",bg="#fb8c00",fg="#ffffff")
    s_btn.pack(side=TOP,padx=20,pady=5,fill=X)
    add_btn = Button(frame2, text="Add",bg="#fb8c00",fg="#ffffff")
    add_btn.pack(side=TOP,padx=20,pady=3,fill=X)
    updt_btn = Button(frame2, text="Update",bg="#fb8c00",fg="#ffffff")
    updt_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    clr_btn = Button(frame2, text="Clear",bg="#fb8c00",fg="#ffffff")
    clr_btn.pack(side=TOP, padx=20, pady=3, fill=X)


