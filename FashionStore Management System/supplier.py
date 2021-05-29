from tkinter import *
from tkinter import ttk
import sqlite3

# Create Supplier Details Page and set the configuration.
def sup_list():
    global supp
    supp=Toplevel()
    supp.title("Supplier Details Page")
    supp.iconbitmap("D:/img/fashion.ico")
    supp.geometry("850x450")
    supp.config(bg="#ffffff")
    SupplierPage()

# Create Database for supplier page.
def database2():
    global supp_db, c
    supp_db=sqlite3.connect("suppliers.db")
    c=supp_db.cursor()
    c.execute(
       "CREATE TABLE IF NOT EXISTS SupplierDetails(id INTEGER PRIMARY KEY, name TEXT, pan INTEGER, contact INTEGER)")
    supp_db.commit()
    supp_db.close()

# Inserting Various Data.
def Insert():
    database2()
    supp_db = sqlite3.connect("suppliers.db")
    c = supp_db.cursor()
    c.execute("INSERT INTO SupplierDetails (id, name, pan, contact) VALUES(?,?,?,?)",
              (supplier_id.get(), supplier_name.get(), pan_no.get(), contact_no.get()))
    supp_db.commit()
    supplier_id.set("")
    supplier_name.set("")
    pan_no.set("")
    contact_no.set("")
    c.close()
    supp_db.close()

# Create a frame and do editing of the suppliers.
# Create entry box and buttons and setting its configuration.
def SupplierPage():
    global tree
    global supplier_id
    global supplier_name
    global pan_no
    global contact_no

    supplier_frame1=Frame(supp,width=300,relief=SOLID,bd=1)
    supplier_frame1.pack(side=TOP,fill=X)
    supplier_label1=Label(supplier_frame1,text="Supplier List", font=('Times New Roman', 15), width=300,bg="#fb8c00",fg="#212121")
    supplier_label1.pack(fill=X)
    supplier_frame2=Frame(supp, width=100,bg="#000000")
    supplier_frame2.pack(side=LEFT, fill=Y)
    supplier_label2 = Label(supplier_frame2, text="Suppliers", font=('Roboto', 12),bg="#000000",fg="#ffffff")
    supplier_label2.pack(side=TOP)
    supplier_frame3=Frame(supp,width=500)
    supplier_frame3.pack(side=RIGHT)
    x = Scrollbar(supplier_frame3, orient=HORIZONTAL)
    y = Scrollbar(supplier_frame3, orient=VERTICAL)
    tree = ttk.Treeview(supplier_frame3, columns=(1,2,3,4), show="headings",
                        selectmode="extended", height=20, yscrollcommand=y.set, xscrollcommand=x.set)
    y.config(command=tree.yview)
    y.pack(side=RIGHT,fill=Y)
    x.config(command=tree.xview)
    x.pack(side=BOTTOM,fill=X)
    tree.heading(1, text='Supplier ID')
    tree.heading(2, text='Supplier Name')
    tree.heading(3, text='Pan No')
    tree.heading(4, text='Contact No')
    tree.column(1, stretch=YES, width=156)
    tree.column(2, stretch=YES, width=250)
    tree.column(3, stretch=YES, width=150)
    tree.column(4, stretch=YES, width=150)
    tree.pack()

    supplier_id=StringVar()
    supplier_name=StringVar()
    pan_no=StringVar()
    contact_no=StringVar()

    supplier_id = Label(supplier_frame2, text="Supplier ID:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_id.pack(side=TOP,padx=10,anchor=W)
    id_entry = Entry(supplier_frame2, text=supplier_id, bg="#ffffff")
    id_entry.pack(side=TOP,padx=10,pady=1,fill=X)

    supplier_name = Label(supplier_frame2, text="Supplier Name:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_name.pack(side=TOP,padx=10,anchor=W)
    name_ety = Entry(supplier_frame2, text=supplier_name, bg="#ffffff")
    name_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    supplier_pan_no = Label(supplier_frame2, text="Pan No:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_pan_no.pack(side=TOP,padx=10,anchor=W)
    pan_ety = Entry(supplier_frame2, text=pan_no, bg="#ffffff")
    pan_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    supplier_contact = Label(supplier_frame2, text="Contact No:",font=("Calibre",9),bg="#000000",fg="#ffffff")
    supplier_contact.pack(side=TOP,padx=10,anchor=W)
    contact_ety = Entry(supplier_frame2, text=contact_no, bg="#ffffff")
    contact_ety.pack(side=TOP,padx=10,pady=1,fill=X)

    view_btn = Button(supplier_frame2, text="View",bg="#fb8c00",fg="#ffffff",command=View)
    view_btn.pack(side=TOP,padx=20,pady=5,fill=X)
    add_btn = Button(supplier_frame2, text="Add",bg="#fb8c00",fg="#ffffff",command=Insert)
    add_btn.pack(side=TOP,padx=20,pady=3,fill=X)
    update_btn = Button(supplier_frame2, text="Update",bg="#fb8c00",fg="#ffffff",command=Update)
    update_btn.pack(side=TOP, padx=20, pady=3, fill=X)
    clear_btn = Button(supplier_frame2, text="Clear",bg="#fb8c00",fg="#ffffff",command=Delete)
    clear_btn.pack(side=TOP, padx=20, pady=3, fill=X)

# Display the various data.
def View():
    database2()
    tree.delete(*tree.get_children())
    supp_db=sqlite3.connect("suppliers.db")
    c=supp_db.cursor()
    c.execute("SELECT * FROM SupplierDetails")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", END, values=row)
    supp_db.close()

# Modify the selected data in the table.
def Update():
    database2()
    supp_db=sqlite3.connect("suppliers.db")
    c=supp_db.cursor()
    c.execute("UPDATE SupplierDetails set id=?,name=?,pan=?,contact=? WHERE id=?",(supplier_id.get(),supplier_name.get(),pan_no.get(),contact_no.get(),supplier_id.get()))
    supp_db.commit()
    c.close()
    supp_db.close()

# Delete the selected data from the table.
def Delete():
    database2()
    supp_db = sqlite3.connect("suppliers.db")
    c = supp_db.cursor()
    c.execute('DELETE FROM SupplierDetails WHERE id = ?',(supplier_id.get(),))
    supp_db.commit()
    c.close()
    supp_db.close()

