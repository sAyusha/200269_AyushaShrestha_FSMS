from tkinter import *
from tkinter import ttk

def click():
    global view
    view=Toplevel()
    view.title("Product Page")
    view.iconbitmap("D:/img/fashion.ico")
    view.geometry("850x450")
    view.config(bg="#ffffff")
    ViewPage()

def ViewPage():
    global Tree
    global product_id
    global prd_name
    global prd_price
    global qnty

    frame1=Frame(view,width=300,relief=SOLID,bd=1)
    frame1.pack(side=TOP,fill=X)
    label1=Label(frame1,text="View Products List", font=('arial', 15), width=300,bg="#e0f7fa")
    label1.pack(fill=X)
    frame2=Frame(view, width=100,bg="#e0f7fa")
    frame2.pack(side=LEFT, fill=Y)
    label2 = Label(frame2, text="Fashion Store", font=('calibre', 11),bg="#e0f7fa")
    label2.pack(side=TOP)
    frame3=Frame(view,width=600)
    frame3.pack(side=RIGHT)
    x = Scrollbar(frame3, orient=HORIZONTAL)
    y = Scrollbar(frame3, orient=VERTICAL)
    tree = ttk.Treeview(frame3, columns=("ProductID", "Product Name", "Product Price", "Quantity"),
                        selectmode="extended", height=20, yscrollcommand=y.set, xscrollcommand=x.set)
    y.config(command=tree.yview)
    y.pack(side=RIGHT,fill=Y)
    x.config(command=tree.xview)
    x.pack(side=BOTTOM,fill=X)
    tree.heading('#0', text='Product Id')
    tree.heading('#1', text='Product Name')
    tree.heading('#2', text='Product Price')
    tree.heading('#3', text='Quantity')
    tree.column('#0', stretch=YES, width=155)
    tree.column('#1', stretch=YES, width=220)
    tree.column('#2', stretch=YES, width=155)
    tree.column('#3', stretch=YES, width=155)
    tree.pack()


    product_id=StringVar()
    prd_price=StringVar()
    prd_name=StringVar()
    qnty=StringVar()

    id = Label(frame2, text="Product ID:",font=("Calibre",9),bg="#e0f7fa")
    id.pack(side=TOP,padx=10,anchor=W)
    id_ety = Entry(frame2, text=product_id, bg="#ffffff")
    id_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    name = Label(frame2, text="Product Name:",font=("Calibre",9),bg="#e0f7fa")
    name.pack(side=TOP,padx=10,anchor=W)
    name_ety = Entry(frame2, text=prd_name, bg="#ffffff")
    name_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    price = Label(frame2, text="Product Price:",font=("Calibre",9),bg="#e0f7fa")
    price.pack(side=TOP,padx=10,anchor=W)
    price_ety = Entry(frame2, text=prd_price, bg="#ffffff")
    price_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    quantity = Label(frame2, text="Quantity:",font=("Calibre",9),bg="#e0f7fa")
    quantity.pack(side=TOP,padx=10,anchor=W)
    quantity_ety = Entry(frame2, text=qnty, bg="#ffffff")
    quantity_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    s_btn = Button(frame2, text="Search",bg="#e0f7fa")
    s_btn.pack(side=TOP,padx=20,pady=5,fill=X)
    add_btn = Button(frame2, text="Add",bg="#e0f7fa")
    add_btn.pack(side=TOP,padx=20,pady=3,fill=X)
    updt_btn = Button(frame2, text="Update",bg="#e0f7fa")
    updt_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    dlt_btn = Button(frame2, text="Delete",bg="#e0f7fa")
    dlt_btn.pack(side=TOP, padx=20, pady=3, fill=X)
