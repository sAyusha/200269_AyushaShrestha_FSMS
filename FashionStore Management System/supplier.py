from tkinter import *
from tkinter import ttk
import sqlite3

# Create Supplier Details Page and set the configuration.
def sup_list():
    global supplier
    supplier=Toplevel()
    supplier.title("Supplier Details Page")
    supplier.iconbitmap("D:/img/fashion.ico")
    width = 950
    height = 550
    screen_width = supplier.winfo_screenwidth()
    screen_height = supplier.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    supplier.geometry("%dx%d+%d+%d" % (width, height, x, y))
    supplier.resizable(0, 0)
    supplier.config()
    supplier.config(bg="#ffffff")
    SupplierPage()

# Create a frame and do editing of the suppliers.
# Create entry box and buttons and setting its configuration.
def SupplierPage():
    global tree
    global supplier_id
    global supplier_name
    global pan_no
    global contact_no

    global id_entry
    global name_entry
    global pan_entry
    global contact_entry

    supplier_frame1=Frame(supplier,width=300,relief=SOLID,bd=1)
    supplier_frame1.pack(side=TOP,fill=X)
    supplier_label1=Label(supplier_frame1,text="Supplier List", font=('Times New Roman', 15), width=300,bg="#fb8c00",fg="#212121")
    supplier_label1.pack(fill=X)
    supplier_frame2=Frame(supplier, width=100,bg="#000000")
    supplier_frame2.pack(side=LEFT, fill=Y)
    supplier_label2 = Label(supplier_frame2, text="Suppliers", font=('Roboto', 12),bg="#000000",fg="#ffffff")
    supplier_label2.pack(side=TOP)

    # Tree View represents the data hierarchically and gives an improved look to the data columns.
    supplier_frame3=Frame(supplier,width=500)
    supplier_frame3.pack(side=RIGHT)
    x = Scrollbar(supplier_frame3, orient=HORIZONTAL)
    y = Scrollbar(supplier_frame3, orient=VERTICAL)
    tree = ttk.Treeview(supplier_frame3, columns=(1,2,3,4), show="headings",
                        selectmode="extended", height=100, yscrollcommand=y.set, xscrollcommand=x.set)
    y.config(command=tree.yview)
    y.pack(side=RIGHT,fill=Y)
    x.config(command=tree.xview)
    x.pack(side=BOTTOM,fill=X)
    tree.heading(1, text='Supplier ID')
    tree.heading(2, text='Supplier Name')
    tree.heading(3, text='Pan No')
    tree.heading(4, text='Contact No')
    tree.column(1, stretch=YES, width=150)
    tree.column(2, stretch=YES, width=250)
    tree.column(3, stretch=YES, width=200)
    tree.column(4, stretch=YES, width=200)
    tree.pack()

    supplier_id=StringVar()
    supplier_name=StringVar()
    pan_no=StringVar()
    contact_no=StringVar()

    supplier_id_label = Label(supplier_frame2, text="Supplier ID:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_id_label.pack(side=TOP,padx=10,anchor=W)
    id_entry = Entry(supplier_frame2, text=supplier_id, bg="#ffffff")
    id_entry.pack(side=TOP,padx=10,pady=1,fill=X)

    supplier_name_label = Label(supplier_frame2, text="Supplier Name:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_name_label.pack(side=TOP,padx=10,anchor=W)
    name_entry = Entry(supplier_frame2, text=supplier_name, bg="#ffffff")
    name_entry.pack(side=TOP,padx=10,pady=1,fill=X)

    supplier_pan_no = Label(supplier_frame2, text="Pan No:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_pan_no.pack(side=TOP,padx=10,anchor=W)
    pan_entry = Entry(supplier_frame2, text=pan_no, bg="#ffffff")
    pan_entry.pack(side=TOP,padx=10,pady=1,fill=X)

    supplier_contact = Label(supplier_frame2, text="Contact No:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_contact.pack(side=TOP,padx=10,anchor=W)
    contact_entry = Entry(supplier_frame2, text=contact_no, bg="#ffffff")
    contact_entry.pack(side=TOP,padx=10,pady=1,fill=X)

    view_btn = Button(supplier_frame2, text="View",bg="#fb8c00",fg="#ffffff",command=View)
    view_btn.pack(side=TOP,padx=20,pady=5,fill=X)
    add_btn = Button(supplier_frame2, text="Add",bg="#fb8c00",fg="#ffffff",command=Insert)
    add_btn.pack(side=TOP,padx=20,pady=3,fill=X)
    search_btn = Button(supplier_frame2, text="Search", bg="#fb8c00", fg="#ffffff", command=Search)
    search_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    update_btn = Button(supplier_frame2, text="Update",bg="#fb8c00",fg="#ffffff",command=Update)
    update_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    clear_btn = Button(supplier_frame2, text="Clear",bg="#fb8c00",fg="#ffffff",command=Delete)
    clear_btn.pack(side=TOP, padx=20, pady=3, fill=X)

# Create the database for the suppliers details.
def database2():
    global supplier_db, c
    supplier_db=sqlite3.connect("suppliers.db")
    c=supplier_db.cursor()
    c.execute(
       "CREATE TABLE IF NOT EXISTS SupplierDetails(id INTEGER PRIMARY KEY, name TEXT, pan INTEGER, contact INTEGER)")
    supplier_db.commit()
    supplier_db.close()

# Inserting Various Data.
def Insert():
    database2()
    supplier_db = sqlite3.connect("suppliers.db")
    c = supplier_db.cursor()
    c.execute("INSERT INTO SupplierDetails (id, name, pan, contact) VALUES(?,?,?,?)",
              (supplier_id.get(), supplier_name.get(), pan_no.get(), contact_no.get()))
    supplier_db.commit()
    supplier_id.set("")
    supplier_name.set("")
    pan_no.set("")
    contact_no.set("")
    c.close()
    supplier_db.close()

# Clear the data that are in the table.
def clear():
    global tree
    for records in tree.get_children():
        tree.delete(records)

# Display the various data.
def View():
    database2()
    tree.delete(*tree.get_children())
    supplier_db=sqlite3.connect("suppliers.db")
    c=supplier_db.cursor()
    c.execute("SELECT * FROM SupplierDetails")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", END, values=row)
    supplier_db.close()

# Modify the selected data in the table.
def Update():
    database2()
    supplier_db=sqlite3.connect("suppliers.db")
    c=supplier_db.cursor()
    c.execute("UPDATE SupplierDetails set id=?,name=?,pan=?,contact=? WHERE id=?",
              (supplier_id.get(), supplier_name.get(), pan_no.get(), contact_no.get(), supplier_id.get()))
    supplier_db.commit()
    c.close()
    supplier_db.close()

# Display particular data that we search for.
def Search():
    database2()
    clear()
    supplier_db = sqlite3.connect("suppliers.db")
    c = supplier_db.cursor()
    c.execute("SELECT * FROM SupplierDetails WHERE id=? OR name=?",
              (supplier_id.get(), supplier_name.get()))
    rows = c.fetchall()
    for row in rows:
        tree.insert("", END, values=row)
    supplier_db.close()

# Delete the selected data from the table.
def Delete():
    database2()
    supplier_db = sqlite3.connect("suppliers.db")
    c = supplier_db.cursor()
    c.execute('DELETE FROM SupplierDetails WHERE id = ?', (supplier_id.get(),))
    supplier_db.commit()
    c.close()
    supplier_db.close()

# Create for counting the report of total suppliers.
def count_suppliers():
    supplier_db = sqlite3.connect("suppliers.db")
    c = supplier_db.cursor()
    count_num = c.execute("SELECT COUNT(DISTINCT name) FROM SupplierDetails").fetchall()
    for num in count_num:
        return num
    supplier_db.commit()
    supplier_db.close()
