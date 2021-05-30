from tkinter import *
from tkinter import ttk
import sqlite3

# function to open the product page
# and configuration of the page.
def click():
    global view
    view=Toplevel()
    view.title("Product Page")
    view.iconbitmap("D:/img/fashion.ico")
    view.geometry("1000x550")
    view.config(bg="#ffffff")
    ViewPage()

# Creating a database for product page.
def database():
    global product_db, c
    product_db=sqlite3.connect("products.db")
    c=product_db.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS ProductItem(id INTEGER PRIMARY KEY, name TEXT, price TEXT, quantity TEXT, total TEXT)")
    product_db.commit()
    product_db.close()

# Inserting Various Data.
def AddItems():
    database()
    product_db = sqlite3.connect("products.db")
    c = product_db.cursor()
    c.execute("INSERT INTO ProductItem (id, name, price, quantity,total) VALUES(?,?,?,?,?)",
              (product_id.get(), prd_name.get(), prd_price.get(),qnty.get(),totalAmount.get()))
    product_db.commit()
    product_id.set("")
    prd_name.set("")
    prd_price.set("")
    qnty.set("")
    totalAmount.set("")
    c.close()
    product_db.close()

def onclick_focusin(event):
    database()
    price_val = int(price_ety.get())
    quan_val = int(quantity_ety.get())
    tot = price_val * quan_val
    if total_amt_ety.get() == "":
        total_amt_ety.insert(0, tot)
        total_amt_ety.config(fg='black')
        print(type(tot))

# Function to create a frame
# and set the configuration
# and do the editing of products.
def ViewPage():
    global tree
    global product_id
    global prd_name
    global prd_price
    global qnty
    global totalAmount

    global id_ety
    global name_ety
    global price_ety
    global quantity_ety
    global total_amt_ety

    frame1=Frame(view,width=300,relief=SOLID,bd=1)
    frame1.pack(side=TOP,fill=X)
    label1=Label(frame1,text="View Products List", font=('arial', 15), width=300,bg="#e0f7fa")
    label1.pack(fill=X)
    frame2=Frame(view, width=100,bg="#e0f7fa")
    frame2.pack(side=LEFT, fill=Y)
    label2 = Label(frame2, text="Fashion Store", font=('calibre', 11),bg="#e0f7fa")
    label2.pack(side=TOP)

    frame3 = Frame(view, width=600)
    frame3.pack(side=RIGHT)
    x = Scrollbar(frame3, orient=HORIZONTAL)
    y = Scrollbar(frame3, orient=VERTICAL)
    tree = ttk.Treeview(frame3, columns=(1, 2, 3, 4, 5), show="headings",
                        selectmode="extended", height=200, yscrollcommand=y.set, xscrollcommand=x.set)
    y.config(command=tree.yview)
    y.pack(side=RIGHT, fill=Y)
    x.config(command=tree.xview)
    x.pack(side=BOTTOM, fill=X)
    tree.heading(1, text='Product id')
    tree.heading(2, text='Product Name')
    tree.heading(3, text='Sell Price')
    tree.heading(4, text='Quantity')
    tree.heading(5, text='Total Amount')
    tree.column(1, stretch=YES, width=130)
    tree.column(2, stretch=YES, width=230)
    tree.column(3, stretch=YES, width=160)
    tree.column(4, stretch=YES, width=150)
    tree.column(5, stretch=YES, width=170)
    tree.pack()

    product_id=StringVar()
    prd_price=StringVar()
    prd_name=StringVar()
    qnty=StringVar()
    totalAmount=StringVar()

    id = Label(frame2, text="Product ID:",font=("Calibre",9),bg="#e0f7fa")
    id.pack(side=TOP,padx=10,anchor=W)
    id_ety = Entry(frame2, text=product_id, bg="#ffffff")
    id_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    name = Label(frame2, text="Product Name:", font=("Calibre", 9), bg="#e0f7fa")
    name.pack(side=TOP, padx=10, anchor=W)
    name_ety = Entry(frame2, text=prd_name, bg="#ffffff")
    name_ety.pack(side=TOP, padx=10, pady=1, fill=X)

    price = Label(frame2, text="Product Price:", font=("Calibre", 9), bg="#e0f7fa")
    price.pack(side=TOP, padx=10, anchor=W)
    price_ety = Entry(frame2, text=prd_price, bg="#ffffff")
    price_ety.pack(side=TOP, padx=10, pady=1, fill=X)

    quantity = Label(frame2, text="Quantity:", font=("Calibre", 9), bg="#e0f7fa")
    quantity.pack(side=TOP, padx=10, anchor=W)
    quantity_ety = Entry(frame2, text=qnty, bg="#ffffff")
    quantity_ety.pack(side=TOP, padx=10, pady=1, fill=X)

    total_amt = Label(frame2, text="Total:", font=("Calibre", 9), bg="#e0f7fa")
    total_amt.pack(side=TOP, padx=10, anchor=W)
    total_amt_ety = Entry(frame2, text=totalAmount, bg="#ffffff")
    total_amt_ety.pack(side=TOP, padx=10, pady=1, fill=X)
    total_amt_ety.insert(0, '')
    total_amt_ety.bind("<FocusIn>", onclick_focusin)

    v_btn = Button(frame2, text="Display", bg="#e0f7fa",command=ShowItems)
    v_btn.pack(side=TOP, padx=20, pady=5, fill=X)
    s_btn = Button(frame2, text="Search", bg="#e0f7fa", command=SearchItems)
    s_btn.pack(side=TOP, padx=20, pady=5, fill=X)
    add_btn = Button(frame2, text="Add", bg="#e0f7fa",command=AddItems)
    add_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    updt_btn = Button(frame2, text="Update", bg="#e0f7fa",command=UpdateItems)
    updt_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    dlt_btn = Button(frame2, text="Delete", bg="#e0f7fa",command=DeleteItems)
    dlt_btn.pack(side=TOP, padx=20, pady=3, fill=X)

def clear():
    global tree
    for records in tree.get_children():
        tree.delete(records)

# Display the items.
def ShowItems():
    database()
    tree.delete(*tree.get_children())
    product_db=sqlite3.connect("products.db")
    c=product_db.cursor()
    c.execute("SELECT * FROM ProductItem")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", END, values=row)
    product_db.close()

def SearchItems():
    database()
    clear()
    product_db = sqlite3.connect("products.db")
    c = product_db.cursor()
    c.execute("SELECT * FROM ProductItem WHERE name=? OR price=? OR quantity=? OR total=?",
              (prd_name.get(),prd_price.get(),qnty.get(),totalAmount.get()))
    rows = c.fetchall()
    for row in rows:
        tree.insert("", END, values=row)
    product_db.close()

# Modify the selected item in the table.
def UpdateItems():
    database()
    product_db=sqlite3.connect("products.db")
    c=product_db.cursor()
    c.execute("UPDATE ProductItem set id=?,name=?,price=?,quantity=?,total=? WHERE id=?",
              (product_id.get(),prd_name.get(),prd_price.get(),qnty.get(),totalAmount.get(),product_id.get()))
    product_db.commit()
    c.close()
    product_db.close()

# Delete the selected item from the table.
def DeleteItems():
    database()
    product_db = sqlite3.connect("products.db")
    c = product_db.cursor()
    c.execute('DELETE FROM ProductItem WHERE id = ?',(product_id.get(),))
    product_db.commit()
    c.close()
    product_db.close()

def purchase_amount():
    database()
    product_db = sqlite3.connect("products.db")
    c = product_db.cursor()
    sum = c.execute("SELECT name, sum(total) FROM ProductItem")
    total = sum.fetchall()
    for x in total:
        print(x)
    product_db.commit()
    product_db.close()