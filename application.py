# application.py - Measure Up application
#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import scrolledtext
import os
import csv
import sqlite3
from datetime import date
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk


class loginWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        # Save parent reference to use it
        self.parent = parent

        self.v_username = tk.StringVar()
        self.v_password = tk.StringVar()


        tk.Label(self, text='Enter Username: ').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(self, text='Enter Password: ').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        e_username = tk.Entry(self, textvariable=self.v_username)
        e_username.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        e_password = tk.Entry(self, textvariable=self.v_password, show="*")
        e_password.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        tk.Button(self, text="Login", command=self.login).grid(column=1, row=2, padx=5, pady=5)

    # Login function for click button
    def login(self):

        if self.v_username.get() == "Akosua" and self.v_password.get() == "mypassword":
            access = True
            #print(access)
        else:
            access = False
            mbox.showwarning('Incorrect Password','Wrong password. Program will exit')
            #print(str(access) + " " + str(self.v_username.get()) + " " + str(self.v_password.get()))

        #access =  True # Used to test if a user can login.

        if access:
            # Close Toplevel window and show root window
            #print("I am here")
            self.destroy()
            self.parent.deiconify()

            #self.parent.deiconify()
        else:
            #self.parent.quit()
            self.quit()


class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master.title("Bema Besia")
        self.master.geometry("+100+100")
        self.master.resizable(0,0)
        self.pack(fill='both', expand=True, padx=5, pady=5)
        self.iconlocation = os.getcwd() + "/measureup.ico"
        try:
            self.master.iconbitmap(self.iconlocation)
        except:
            pass

        # Initialize the database
        #database = sqlite3.connect('dbmeasureup.db')
        #cur = database.cursor()
        # Create the menu bar for the main window
        self.menubar = tk.Menu(self)
        self.master.config(menu=self.menubar)

        # Create the File menu, Options menu, Help menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.optionmenu = tk.Menu(self.menubar, tearoff=0)

        # Add the menu items to the Menu bar
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.menubar.add_cascade(label='Options', menu=self.optionmenu)
        self.menubar.add_cascade(label='Help', menu=self.helpmenu)

        self.filemenu.add_command(label='Quit', command=self.allmenucommands)
        self.helpmenu.add_command(label='About', command=self.allmenucommands)
        self.optionmenu.add_command(label='My Options', command=self.allmenucommands)

        # Create the three buttons, Create New Customer,  Enter Customer Measurements & Search Customer Measurements
        self.btn_newCustomer = ttk.Button(self, text='New Customer', command=self.newCustomerCmd)
        self.btn_newCustomer.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        self.btn_customerMeas = ttk.Button(self, text='Customer Measurements', command=self.customeMeasurementCmd)
        self.btn_customerMeas.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)
        self.btn_searchMeas = ttk.Button(self, text='Search Measurements', command=self.customSearchCmd)
        self.btn_searchMeas.grid(column=2, row=0, padx=10, pady=10, sticky=tk.E)

        # Insert HoJ banner in Frame
        #hojFrame1 = ttk.LabelFrame(self)
        #hojFrame1.grid(column=0, row=1, pady=0, padx=0, columnspan=3)
        #render = ImageTk.PhotoImage(file=r"C:\Users\ekwaoffei\PycharmProjects\Home\HoJ\application\hojbanner.jpg")
        #img = tk.Label(hojFrame1, image=render)
        #img.image = render
        #img.grid(column=0, row=0)

        # Hide root window
        self.master.withdraw()
        #self.withdraw()

        # Lunch login window
        loginWindow(self.master)

    def allmenucommands(self):
        print('test')

    def newCustomerCmd(self):
        NewCustomerWindow(self)

    def customeMeasurementCmd(self):
        CustomerMeasurement(self)

    def customSearchCmd(self):
        CustomerSearch(self)

    def quit(self):
        self.destroy()


class NewCustomerWindow(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Bema Besia")
        self.grab_set()
        self.resizable(0,0)

        self.newCustFrame = ttk.LabelFrame(self, text='Enter new customer details')
        self.newCustFrame.grid(column=0, row=0, pady=5, padx=5)
        #ttk.Label(self, text='This is a testssssssssssssssss').grid(column=0, row=0)
        # Date picker to be done
        self.today = date.strftime(date.today(), '%Y-%m-%d')


        # String variables
        self.v_custName = tk.StringVar()
        self.v_mobNumber1 = tk.StringVar()
        self.v_mobNumber2 = tk.StringVar()
        self.v_custEMail = tk.StringVar()
        self.v_custAddress = tk.StringVar()
        self.v_sexSelect = tk.StringVar()



        # Date
        ttk.Label(self, text='Date').grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self, text=self.today).grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
        # Enter customer name
        ttk.Label(self, text='Name:  ').grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        self.e_custNameEntry = ttk.Entry(self, textvariable=self.v_custName)
        self.e_custNameEntry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)
        # Enter customer mobile number
        # To do : Create number Regex
        ttk.Label(self, text='Mobile Number 1:  ').grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
        self.e_custMobNumber1 = ttk.Entry(self, textvariable=self.v_mobNumber1)
        self.e_custMobNumber1.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)

        ttk.Label(self, text='Mobile Number 2:  ').grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
        self.e_custMobNumber2 = ttk.Entry(self, textvariable=self.v_mobNumber2)
        self.e_custMobNumber2.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)

        # Enter customer email
        # To do : Create email Regex
        ttk.Label(self, text='E-Mail: ').grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)
        self.e_custEMail = ttk.Entry(self, textvariable=self.v_custEMail)
        self.e_custEMail.grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)
        # Customer Address
        ttk.Label(self, text='Address: ').grid(column=0, row=5, padx=5, pady=5, sticky=tk.W)
        self.e_custAddress = ttk.Entry(self, textvariable=self.v_custAddress)
        self.e_custAddress.grid(column=1, row=5, padx=5, pady=5, sticky=tk.E)
        # Customer sex
        ttk.Label(self, text='Gender: ').grid(column=0, row=6, padx=5, pady=5, sticky=tk.W)
        self.cmb_sexCombo = ttk.Combobox(self, textvariable=self.v_sexSelect, state='readonly', width=17)
        self.cmb_sexCombo['values'] = ("Female", "Male")
        self.cmb_sexCombo.grid(column=1, row=6, pady=5, padx=5, sticky=tk.E)
        self.cmb_sexCombo.current(0)

        # Save Button
        self.btn_custSave = ttk.Button(self, text='               Save               ', command=self.saveNewCustCmd)
        self.btn_custSave.grid(column=1, row=7, padx=5, pady=5, sticky=tk.E)



    def saveNewCustCmd(self):
        # Initialize the database connection
        database = sqlite3.connect('dbmeasureup.db')
        cur = database.cursor()

        # Get Rowcount
        cur.execute("SELECT MAX(c_customerID) from t_customer")
        myrowCount = cur.fetchall()[0][0]

        #print (str(myrowCount))


        if myrowCount is None :
            rowCount = 0

        else:
            rowCount = int(myrowCount)
            rowCount = int(rowCount + 1)

        cur.execute("INSERT INTO t_customer values (?,?,?,?,?,?,?,?)",
                        (rowCount, self.v_custName.get(), self.today, self.v_mobNumber1.get(), self.v_mobNumber2.get(), self.v_custEMail.get(), self.v_custAddress.get(), self.cmb_sexCombo.get())
                        )
        try:
            database.commit()
        except sqlite3.Error:
            database.rollback()

        if database:
            cur.close()
            database.close()
            showRecord = "New customer created successfully!"
            mbox.showinfo('Successful', showRecord, parent=self)
        else:
            mbox.showerror('Save Error', 'Could not save the new customer record', parent=self)


class CustomerMeasurement(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Bema Besia")
        self.grab_set()
        self.resizable(0,0)

        self.custListFrame = ttk.LabelFrame(self, text='Customer List')
        #self.custListFrame.grid(column=0, row=0, pady=5, padx=5)
        self.custListFrame.pack(side='left', anchor='n')
        #ttk.Label(self.custListFrame, text='This is customer list frame').grid(column=0, row=0)
        # Date picker to be done
        self.today = date.strftime(date.today(), '%Y-%m-%d')

        # String vars
        self.v_custName = tk.StringVar()
        self.v_custBust = tk.StringVar()
        self.v_custWaist = tk.StringVar()
        self.v_custHip = tk.StringVar()
        self.v_custShoulder = tk.StringVar()
        self.v_custShoulderToNipple = tk.StringVar()
        self.v_custNippleToNipple = tk.StringVar()
        self.v_custShoulderToUnderBust = tk.StringVar()
        self.v_custShoulderToWaist = tk.StringVar()
        self.v_custShoulderToHip = tk.StringVar()
        self.v_custAcrossBack = tk.StringVar()
        self.v_custAcrossChest = tk.StringVar()
        self.v_custAroundArm = tk.StringVar()
        self.v_custNapeToWaist = tk.StringVar()
        self.v_custKabaLength = tk.StringVar()
        self.v_custBlouseLength = tk.StringVar()
        self.v_custSkirtLength = tk.StringVar()
        self.v_custSlitLength = tk.StringVar()
        self.v_custSleeveLength = tk.StringVar()
        self.v_custDressLength = tk.StringVar()

        self.custMeasureFrame = ttk.LabelFrame(self, text='Measurement details in inches')
        #self.custMeasureFrame.grid(column=1, row=0, pady=5, padx=5)
        self.custMeasureFrame.pack(side='right', anchor='n')
        #ttk.Label(self.custMeasureFrame, text='This is customer list frame').grid(column=0, row=0)

        # Date picker
        ttk.Label(self.custMeasureFrame, text='Date').grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self.custMeasureFrame, text=self.today).grid(column=1, row=0, padx=5, pady=5, sticky=tk.E)
        # Entries
        ttk.Label(self.custMeasureFrame, text='Customer Name: ').grid(column=0, row=1, padx=5, pady=1, sticky=tk.W)
        # Customer name after double clicking in List view : query to be done
        self.e_custName = ttk.Label(self.custMeasureFrame)
        self.e_custName.grid(column=1, row=1, padx=5, pady=1, sticky=tk.E)
        # More Entries
        ttk.Label(self.custMeasureFrame, text='Bust ').grid(column=0, row=2, padx=5, pady=1, sticky=tk.W)
        self.e_custBust = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custBust)
        self.e_custBust.grid(column=1, row=2, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Waist').grid(column=0, row=3, padx=5, pady=1, sticky=tk.W)
        self.e_custWaist = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custWaist)
        self.e_custWaist.grid(column=1, row=3, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Hip').grid(column=0, row=4, padx=5, pady=1, sticky=tk.W)
        self.e_custHip = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custHip)
        self.e_custHip.grid(column=1, row=4, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Shoulder').grid(column=0, row=5, padx=5, pady=1, sticky=tk.W)
        self.e_custShoulder = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custShoulder)
        self.e_custShoulder.grid(column=1, row=5, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Shoulder To Nipple').grid(column=0, row=6, padx=5, pady=1, sticky=tk.W)
        self.e_custShoulderToNipple = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custShoulderToNipple)
        self.e_custShoulderToNipple.grid(column=1, row=6, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Nipple to Nipple').grid(column=0, row=7, padx=5, pady=1, sticky=tk.W)
        self.e_custNippleToNipple = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custNippleToNipple)
        self.e_custNippleToNipple.grid(column=1, row=7, padx=5, pady=1, sticky=tk.W)
        ttk.Label(self.custMeasureFrame, text='Shoulder to Under Bust').grid(column=0, row=8, padx=5, pady=1, sticky=tk.W)
        self.e_custShoulderToUnderBust = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custShoulderToUnderBust)
        self.e_custShoulderToUnderBust.grid(column=1, row=8, padx=5, pady=1, sticky=tk.W)
        ttk.Label(self.custMeasureFrame, text='Shoulder To Waist').grid(column=0, row=9, padx=5, pady=1, sticky=tk.W)
        self.e_custShoulderToWaist = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custShoulderToWaist)
        self.e_custShoulderToWaist.grid(column=1, row=9, padx=5, pady=1, sticky=tk.W)
        ttk.Label(self.custMeasureFrame, text='Shoulder To Hip').grid(column=0, row=10, padx=5, pady=1, sticky=tk.W)
        self.e_custShoulderToHip = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custShoulderToHip)
        self.e_custShoulderToHip.grid(column=1, row=10, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Across Back').grid(column=0, row=11, padx=5, pady=1, sticky=tk.W)
        self.e_custAcrossBack = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custAcrossBack)
        self.e_custAcrossBack.grid(column=1, row=11, padx=5, pady=1, sticky=tk.W)
        ttk.Label(self.custMeasureFrame, text='Across Chest').grid(column=0, row=12, padx=5, pady=1, sticky=tk.W)
        self.e_custAcrossChest = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custAcrossChest)
        self.e_custAcrossChest.grid(column=1, row=12, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Around Arm').grid(column=0, row=13, padx=5, pady=1, sticky=tk.W)
        self.e_custAroundArm = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custAroundArm)
        self.e_custAroundArm.grid(column=1, row=13, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Nape To Waist').grid(column=0, row=14, padx=5, pady=1, sticky=tk.W)
        self.e_custNapeToWaist = tk.Entry(self.custMeasureFrame, textvariable=self.v_custNapeToWaist)
        self.e_custNapeToWaist.grid(column=1, row=14, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Kaba Length').grid(column=0, row=15, padx=5, pady=1, sticky=tk.W)
        self.e_custKabaLength = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custKabaLength)
        self.e_custKabaLength.grid(column=1, row=15, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Blouse Length').grid(column=0, row=16, padx=5, pady=1, sticky=tk.W)
        self.e_custBlouseLength = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custBlouseLength)
        self.e_custBlouseLength.grid(column=1, row=16, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Skirt Length').grid(column=0, row=17, padx=5, pady=1, sticky=tk.W)
        self.e_custSkirtLength = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custSkirtLength)
        self.e_custSkirtLength.grid(column=1, row=17, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Slit Length').grid(column=0, row=18, padx=5, pady=1, sticky=tk.W)
        self.e_custSlitLength = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custSlitLength)
        self.e_custSlitLength.grid(column=1, row=18, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Sleeve Length').grid(column=0, row=19, padx=5, pady=1, sticky=tk.W)
        self.e_custSleeveLength = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custSleeveLength)
        self.e_custSleeveLength.grid(column=1, row=19, padx=5, pady=1, sticky=tk.E)
        ttk.Label(self.custMeasureFrame, text='Dress Length').grid(column=0, row=20, padx=5, pady=1, sticky=tk.W)
        self.e_custDressLength = ttk.Entry(self.custMeasureFrame, textvariable=self.v_custDressLength)
        self.e_custDressLength.grid(column=1, row=20, padx=5, pady=1, sticky=tk.E)
        self.btn_custMeasSave = ttk.Button(self.custMeasureFrame, text='Save', command=self.saveCmd)
        self.btn_custMeasSave.grid(column=1, row=21, padx=5, pady=5, sticky=tk.E)

        # List box
        self.l_customerList = tk.Listbox(self.custListFrame, height=32)
        #self.l_customerList.grid(column=0, row=0, sticky=tk.W,  rowspan=20)
        self.l_customerList.pack(side='left', fill='both')
        self.s_scrollCustomers = tk.Scrollbar(self.custListFrame, command=self.l_customerList.yview)
        #s_scrollCustomers.grid(column=1, row=0, sticky=tk.NS)
        self.s_scrollCustomers.pack(side='right', anchor='n', fill='y')
        self.l_customerList.bind('<Double-Button-1>', self.selectitem)

        # Insert customers in listbox
        self.searchCustNames()

    # Function : Get Name of Customers into List
    def searchCustNames(self):
        # Initialize the database connection
        database = sqlite3.connect('dbmeasureup.db')
        cur = database.cursor()
        query = cur.execute("select c_custName from t_customer")
        rows = query.fetchall()
        #print(rows)
        for row in rows:
            self.l_customerList.insert('end', row[0])


    # Function - double click select list box item
    def selectitem(self, event):
        print()

        cust_from_list = self.l_customerList.get('active')
        #print()
        #print(event)
        #self.e_custName.delete(0, 'end')
        self.e_custBust.delete(0, 'end')
        self.e_custWaist.delete(0, 'end')
        self.e_custHip.delete(0, 'end')
        self.e_custShoulder.delete(0, 'end')
        self.e_custShoulderToNipple.delete(0, 'end')
        self.e_custNippleToNipple.delete(0, 'end')
        self.e_custShoulderToUnderBust.delete(0, 'end')
        self.e_custShoulderToWaist.delete(0, 'end')
        self.e_custShoulderToHip.delete(0, 'end')
        self.e_custAcrossBack.delete(0, 'end')
        self.e_custAcrossChest.delete(0, 'end')
        self.e_custAroundArm.delete(0, 'end')
        self.e_custNapeToWaist.delete(0, 'end')
        self.e_custKabaLength.delete(0, 'end')
        self.e_custBlouseLength.delete(0, 'end')
        self.e_custSkirtLength.delete(0, 'end')
        self.e_custSlitLength.delete(0, 'end')
        self.e_custSleeveLength.delete(0, 'end')
        self.e_custDressLength.delete(0, 'end')

        # Variables to hold fetched measurement data



        active_cust_select = self.l_customerList.get('active')
        #print(str(active_cust_select))
        # Show selected user from List
        def clearName(self):
            self.e_custName = ttk.Label(self.custMeasureFrame, text="                                      ")
            self.e_custName.grid(column=1, row=1, padx=5, pady=1, sticky=tk.E)

        clearName(self)


        self.e_custName = ttk.Label(self.custMeasureFrame, text=active_cust_select)
        self.e_custName.grid(column=1, row=1, padx=5, pady=1, sticky=tk.E)

        # Connect to db and query
        database = sqlite3.connect('dbmeasureup.db')
        cur = database.cursor()
        v_mycustomerid = cur.execute("select c_customerID from t_customer where c_custName= '" + str(active_cust_select) + "'")
        rows = v_mycustomerid.fetchall()[0][0]
        # for x in rows:
        #print(str(rows))
        #q_getcustmeas = "select * from t_custMeasurements where c_customerID= '" + str(rows) + "'"
        #print(q_getcustmeas)
        query = cur.execute("select * from t_custMeasurements where c_customerID= '" + str(rows) + "'")
        q_rows = query.fetchall()
        #print(q_rows)
        if len(q_rows) == '0':
            pass
        else:
            cBust = q_rows[0][2]
            cWaist = q_rows[0][3]
            cHip = q_rows[0][4]
            cShoulder = q_rows[0][5]
            cShoulderNipple = q_rows[0][6]
            cNip2Nip = q_rows[0][7]
            cShoulder2UBust = q_rows[0][8]
            cShoulder2Waist = q_rows[0][9]
            cShoulder2Hip = q_rows[0][10]
            cAcrossBack = q_rows[0][11]
            cAcrossChest = q_rows[0][12]
            cAroundArm = q_rows[0][13]
            cNape2Waist = q_rows[0][14]
            cKabaLength = q_rows[0][15]
            cBlouseLength = q_rows[0][16]
            cSkirtLength = q_rows[0][17]
            cSlitLength = q_rows[0][18]
            cSleeveLength = q_rows[0][19]
            cDressLength = q_rows[0][20]

            self.e_custBust.insert('end', str(cBust))
            self.e_custWaist.insert('end', str(cWaist))
            self.e_custHip.insert('end', str(cHip))
            self.e_custShoulder.insert('end', str(cShoulder))
            self.e_custShoulderToNipple.insert('end', str(cShoulderNipple))
            self.e_custNippleToNipple.insert('end', str(cNip2Nip))
            self.e_custShoulderToUnderBust.insert('end', str(cShoulder2UBust))
            self.e_custShoulderToWaist.insert('end', str(cShoulder2Waist))
            self.e_custShoulderToHip.insert('end', str(cShoulder2Hip))
            self.e_custAcrossBack.insert('end', str(cAcrossBack))
            self.e_custAcrossChest.insert('end', str(cAcrossChest))
            self.e_custAroundArm.insert('end', str(cAroundArm))
            self.e_custNapeToWaist.insert('end', str(cNape2Waist))
            self.e_custKabaLength.insert('end', str(cKabaLength))
            self.e_custBlouseLength.insert('end', str(cBlouseLength))
            self.e_custSkirtLength.insert('end', str(cSkirtLength))
            self.e_custSlitLength.insert('end', str(cSlitLength))
            self.e_custSleeveLength.insert('end', str(cSleeveLength))
            self.e_custDressLength.insert('end', str(cDressLength))

        if database:
            cur.close()
            database.close()

    def saveCmd(self):
        #print()
        # self.e_custName.delete(0, 'end')
        cust_from_list = self.l_customerList.get('active')
        self.today1 = date.strftime(date.today(), '%Y-%m-%d')
        vBust = self.e_custBust.get()
        vWaist = self.e_custWaist.get()
        vHip = self.e_custHip.get()
        vShoulder = self.e_custShoulder.get()
        vShoulder2Nipple = self.e_custShoulderToNipple.get()
        vNip2Nip = self.e_custNippleToNipple.get()
        vShoulder2UBust = self.e_custShoulderToUnderBust.get()
        vShoulder2Waist = self.e_custShoulderToWaist.get()
        vShoulder2Hip = self.e_custShoulderToHip.get()
        vAcrossBack = self.e_custAcrossBack.get()
        vAcrossChest = self.e_custAcrossChest.get()
        vAroundArm = self.e_custAroundArm.get()
        vNape2Waist = self.e_custNapeToWaist.get()
        vKabaLength = self.e_custKabaLength.get()
        vBlouseLength = self.e_custBlouseLength.get()
        vSkirtLength = self.e_custSkirtLength.get()
        vSlitLength = self.e_custSlitLength.get()
        vSleeveLength = self.e_custSleeveLength.get()
        vDressLength = self.e_custDressLength.get()

        def getValues(self):
            self.today1 = date.strftime(date.today(), '%Y-%m-%d')
            i_vBust = self.e_custBust.get()
            vBust = i_vBust
            i_vWaist = self.e_custWaist.get()
            vWaist = i_vWaist
            i_vHip = self.e_custHip.get()
            vHip = i_vHip
            i_vShoulder = self.e_custShoulder.get()
            vShoulder = i_vShoulder
            i_vShoulder2Nipple = self.e_custShoulderToNipple.get()
            vShoulder2Nipple = i_vShoulder2Nipple
            i_vNip2Nip = self.e_custNippleToNipple.get()
            vNip2Nip = i_vNip2Nip
            i_vShoulder2UBust = self.e_custShoulderToUnderBust.get()
            vShoulder2UBust = i_vShoulder2UBust
            i_vShoulder2Waist = self.e_custShoulderToWaist.get()
            vShoulder2Waist = i_vShoulder2Waist
            i_vShoulder2Hip = self.e_custShoulderToHip.get()
            vShoulder2Hip = i_vShoulder2Hip
            i_vAcrossBack = self.e_custAcrossBack.get()
            vAcrossBack = i_vAcrossBack
            i_vAcrossChest = self.e_custAcrossChest.get()
            vAcrossChest = i_vAcrossChest
            i_vAroundArm = self.e_custAroundArm.get()
            vAroundArm = i_vAroundArm
            i_vNape2Waist = self.e_custNapeToWaist.get()
            vNape2Waist = i_vNape2Waist
            i_vKabaLength = self.e_custKabaLength.get()
            vKabaLength = i_vKabaLength
            i_vBlouseLength = self.e_custBlouseLength.get()
            vBlouseLength = i_vBlouseLength
            i_vSkirtLength = self.e_custSkirtLength.get()
            vSkirtLength = i_vSkirtLength
            i_vSlitLength = self.e_custSlitLength.get()
            vSlitLength = i_vSlitLength
            i_vSleeveLength = self.e_custSleeveLength.get()
            vSleeveLength = i_vSleeveLength
            i_vDressLength = self.e_custDressLength.get()
            vDressLength = i_vDressLength
            #print(vBust)
        getValues(self)

        # Initialise database connection
        database = sqlite3.connect('dbmeasureup.db')
        cur1 = database.cursor()
        # Get customer id
        cur1.execute("select c_customerID from t_customer where c_custName like " + "'" + str(cust_from_list) + "'")
        foundID = cur1.fetchall()[0][0]

        # Query string
        '''
        longquery = "INSERT OR REPLACE INTO t_custMeasurements ( \
                                              c_customerID, \
                                              c_Date,\
                                              c_custBust, \
                                              c_custWaist, \
                                              c_custHip, \
                                              c_custShoulder, \
                                              c_custShoulderToNipple, \
                                              c_custNippleToNipple, \
                                              c_custShoulderToUnderBust, \
                                              c_custShoulderToWaist, \
                                              c_custShoulderToHip, \
                                              c_custAcrossBack, \
                                              c_custAcrossChest, \
                                              c_custAroundArm, \
                                              c_custNapeToWaist, \
                                              c_custKabaLength, \
                                              c_custBlouseLength, \
                                              c_custSkirtLength, \
                                              c_custSlitLength, \
                                              c_custSleeveLength, \
                                              c_custDressLength \
                                          ) \
                                          VALUES ((SELECT c_customerID FROM t_customer WHERE c_customerID = " + "'" + str(foundID) + "'" + ")" + "," \
                                              + "'" + str(self.today1) + "'" + "," \
                                              "'" + str(vBust) + "'" + "," \
                                              + "'" + str(vWaist) + "'" + "," \
                                              + "'" + str(vHip) + "'" + "," \
                                              + "'" + str(vShoulder) + "'" + "," \
                                              + "'" + str(vShoulder2Nipple) + "'" + "," \
                                              + "'" + str(vNip2Nip) + "'" + "," \
                                              + "'" + str(vShoulder2UBust) + "'" + "," \
                                              + "'" + str(vShoulder2Waist) + "'" + "," \
                                              + "'" + str(vShoulder2Hip) + "'" + "," \
                                              + "'" + str(vAcrossBack) + "'" + "," \
                                              + "'" + str(vAcrossChest) + "'" + "," \
                                              + "'" + str(vAroundArm) + "'" + "," \
                                              + "'" + str(vNape2Waist) + "'"  + "," \
                                              + "'" + str(vKabaLength) + "'" + "," \
                                              + "'" + str(vBlouseLength) + "'" + "," \
                                              + "'" + str(vSkirtLength) + "'" + "," \
                                              + "'" + str(vSlitLength) + "'" + "," \
                                              + "'" + str(vSleeveLength) + "'" "," \
                                              + "'" + str(vDressLength) + "'" + ")"
        '''
        longquery1 = "UPDATE t_custMeasurements SET \
        			c_customerID = '" + str((foundID)) + "', " + \
                     "c_Date = '" + str(self.today1) + "', " + \
                     "c_custBust = '" + str(vBust) + "', " + \
                     "c_custWaist = '" + str(vWaist) + "', " + \
                     "c_custHip = '" + str(vHip) + "', " + \
                     "c_custShoulder = '" + str(vShoulder) + "', " + \
                     "c_custShoulderToNipple = '" + str(vShoulder2Nipple) + "', " + \
                     "c_custNippleToNipple = '" + str(vNip2Nip) + "', " + \
                     "c_custShoulderToUnderBust = '" + str(vShoulder2UBust) + "', " + \
                     "c_custShoulderToWaist = '" + str(vShoulder2Waist) + "', " + \
                     "c_custShoulderToHip = '" + str(vShoulder2Hip) + "', " + \
                     "c_custAcrossBack = '" + str(vAcrossBack) + "', " + \
                     "c_custAcrossChest = '" + str(vAcrossChest) + "', " + \
                     "c_custAroundArm = '" + str(vAroundArm) + "', " + \
                     "c_custNapeToWaist = '" + str(vNape2Waist) + "', " + \
                     "c_custKabaLength = '" + str(vKabaLength) + "', " + \
                     "c_custBlouseLength = '" + str(vBlouseLength) + "', " + \
                     "c_custSkirtLength = '" + str(vSkirtLength) + "', " + \
                     "c_custSlitLength = '" + str(vSlitLength) + "', " + \
                     "c_custSleeveLength = '" + str(vSleeveLength) + "', " + \
                     "c_custDressLength = '" + str(vDressLength) + "' " + \
                     " WHERE c_customerID = '" + str(foundID) + "'; "

        longquery2 = "INSERT INTO t_custMeasurements (" + \
                     "c_customerID," + \
                     "c_Date," + \
                     "c_custBust," + \
                     "c_custWaist," + \
                     "c_custHip," + \
                     "c_custShoulder," + \
                     "c_custShoulderToNipple," + \
                     "c_custNippleToNipple," + \
                     "c_custShoulderToUnderBust," + \
                     "c_custShoulderToWaist," + \
                     "c_custShoulderToHip," + \
                     "c_custAcrossBack," + \
                     "c_custAcrossChest," + \
                     "c_custAroundArm," + \
                     "c_custNapeToWaist," + \
                     "c_custKabaLength," + \
                     "c_custBlouseLength," + \
                     "c_custSkirtLength," + \
                     "c_custSlitLength," + \
                     "c_custSleeveLength," + \
                     "c_custDressLength )" + \
                     " SELECT " + \
                     "'" + str((foundID)) + "'," + \
                     "'" + str(self.today1) + "'," + \
                     "'" + str(vBust) + "'," + \
                     "'" + str(vWaist) + "'," + \
                     "'" + str(vHip) + "'," + \
                     "'" + str(vShoulder) + "'," + \
                     "'" + str(vShoulder2Nipple) + "'," + \
                     "'" + str(vNip2Nip) + "'," + \
                     "'" + str(vShoulder2UBust) + "'," + \
                     "'" + str(vShoulder2Waist) + "'," + \
                     "'" + str(vShoulder2Hip) + "'," + \
                     "'" + str(vAcrossBack) + "'," + \
                     "'" + str(vAcrossChest) + "'," + \
                     "'" + str(vAroundArm) + "'," + \
                     "'" + str(vNape2Waist) + "'," + \
                     "'" + str(vKabaLength) + "'," + \
                     "'" + str(vBlouseLength) + "'," + \
                     "'" + str(vSkirtLength) + "'," + \
                     "'" + str(vSlitLength) + "'," + \
                     "'" + str(vSleeveLength) + "'," + \
                     "'" + str(vDressLength) + "' " + \
                     " WHERE (Select Changes() = 0)"

        #print(longquery1)
        #print(longquery2)
        # Save or Update measurement records
        cur1.execute(longquery1)
        cur1.execute(longquery2)
        try:
           database.commit()
        except sqlite3.Error:
            database.rollback()

        if database:
            cur1.close()
            database.close()
            showRecord = "Saved!"
            mbox.showinfo('Successful', showRecord)
        else:
            mbox.showinfo('Save Error', 'Could not save!')

class CustomerSearch(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Bema Besia")
        self.grab_set()
        self.resizable(0, 0)

        # Customer List Frame
        self.custSearchListFrame = ttk.LabelFrame(self, text=' Customer List ')
        self.custSearchListFrame.pack(side='left', anchor='n', padx=5, pady=5)

        # Customer Detail Frame
        self.DetailFrame = ttk.LabelFrame(self, text=' Customer details ')
        self.DetailFrame.pack(side='top', anchor='n', fill='both', padx=5, pady=25)
        ttk.Label(self.DetailFrame, text='Name:         ').grid(column=0, row=0, sticky=tk.W, padx=1, pady=1)
        #ttk.Label(self.DetailFrame, text='Gender:         ').grid(column=0, row=1, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text='Date Created:         ').grid(column=0, row=2, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text='Mobile Number 1:         ').grid(column=0, row=3, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text='Mobile Number 2:         ').grid(column=0, row=4, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text='E-Mail:         ').grid(column=0, row=5, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text='Address:         ').grid(column=0, row=6, sticky=tk.W, padx=1, pady=1)

        # Customer detail variables
        cName = tk.StringVar()
        cMobNum1 = tk.StringVar()
        cMobNum2 = tk.StringVar()
        cEMail = tk.StringVar()
        cAddress = tk.StringVar()

        self.e_cName = ttk.Entry(self.DetailFrame, textvariable=cName)
        self.e_cName.grid(column=2, row=0, sticky=tk.E)
        #ttk.Label(self.DetailFrame).grid(column=4, row=0, sticky=tk.E)
        self.e_cMobNum1 = ttk.Entry(self.DetailFrame, textvariable=cMobNum1)
        self.e_cMobNum1.grid(column=2, row=3, sticky=tk.E)
        self.e_cMobNum2 = ttk.Entry(self.DetailFrame, textvariable=cMobNum2)
        self.e_cMobNum2.grid(column=2, row=4, sticky=tk.E)
        self.e_cEMail = ttk.Entry(self.DetailFrame, textvariable=cEMail)
        self.e_cEMail.grid(column=2, row=5, sticky=tk.E)
        self.e_cAddress = ttk.Entry(self.DetailFrame, textvariable=cAddress)
        self.e_cAddress.grid(column=2, row=6, sticky=tk.E)
        #ttk.Label(self.DetailFrame).grid(column=4, row=1, sticky=tk.E)

        # Buttons Update, Delete
        self.btn_Update = ttk.Button(self.DetailFrame, text='Update User Details')
        self.btn_Update.grid(column=0, row=7, sticky=tk.W, padx=3, pady=8)


        # Customer Detail Measurement Frame
        self.custMeasureDetailFrame = ttk.LabelFrame(self, text=' Measurement details in inches ')
        self.custMeasureDetailFrame.pack(side='top', anchor='s', fill='both')
        ttk.Label(self.custMeasureDetailFrame, text='Bust: ').grid(column=0, row=0, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Waist: ').grid(column=0, row=1, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Hip: ').grid(column=0, row=2, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Shoulder: ').grid(column=0, row=3, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Shoulder To Nipple: ').grid(column=0, row=4, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Nipple To Nipple: ').grid(column=0, row=5, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Shoulder To Under Bust:').grid(column=0, row=6, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Shoulder To Waist: ').grid(column=0, row=7, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Shoulder To Hip: ').grid(column=0, row=8, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Across Back: ').grid(column=0, row=9, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Across Chest: ').grid(column=3, row=0, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Around Arm: ').grid(column=3, row=1, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Nape To Waist: ').grid(column=3, row=2, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Kaba Length: ').grid(column=3, row=3, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Blouse Length: ').grid(column=3, row=4, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Skirt Length: ').grid(column=3, row=5, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Slit Length: ').grid(column=3, row=6, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Sleeve Length: ').grid(column=3, row=7, sticky=tk.E, padx=1, pady=1)
        ttk.Label(self.custMeasureDetailFrame, text='Dress Length: ').grid(column=3, row=8, sticky=tk.E, padx=1, pady=1)
        ttk.Button(self.custMeasureDetailFrame, text='Export').grid(column=0, row=10, sticky=tk.W, padx=5, pady=5)
        #ttk.Button(self.custMeasureDetailFrame, text='Delete').grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)

        self.btn_DeleteUser = ttk.Button(self.custMeasureDetailFrame, text='Delete User', command=self.deleteUserCmd)
        self.btn_DeleteUser.grid(column=1, row=10, sticky=tk.W, padx=3, pady=8)

        #  String vars for measurements
        self.v_custName = tk.StringVar()
        self.v_custBust = tk.StringVar()
        self.v_custWaist = tk.StringVar()
        self.v_custHip = tk.StringVar()
        self.v_custShoulder = tk.StringVar()
        self.v_custShoulderToNipple = tk.StringVar()
        self.v_custNippleToNipple = tk.StringVar()
        self.v_custShoulderToUnderBust = tk.StringVar()
        self.v_custShoulderToWaist = tk.StringVar()
        self.v_custShoulderToHip = tk.StringVar()
        self.v_custAcrossBack = tk.StringVar()
        self.v_custAcrossChest = tk.StringVar()
        self.v_custAroundArm = tk.StringVar()
        self.v_custNapeToWaist = tk.StringVar()
        self.v_custKabaLength = tk.StringVar()
        self.v_custBlouseLength = tk.StringVar()
        self.v_custSkirtLength = tk.StringVar()
        self.v_custSlitLength = tk.StringVar()
        self.v_custSleeveLength = tk.StringVar()
        self.v_custDressLength = tk.StringVar()

        # Fetched measurements
        self.e_cBust = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cBust.grid(column=1, row=0, sticky=tk.W, padx=1, pady=1)
        self.e_cWaist = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cWaist.grid(column=1, row=1, sticky=tk.W, padx=1, pady=1)
        self.e_cHip = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cHip.grid(column=1, row=2, sticky=tk.W, padx=1, pady=1)
        self.e_cShoulder = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cShoulder.grid(column=1, row=3, sticky=tk.W, padx=1, pady=1)
        self.e_cShoulderToNip = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cShoulderToNip.grid(column=1, row=4, sticky=tk.W, padx=1, pady=1)
        self.e_cNipToNip = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cNipToNip.grid(column=1, row=5, sticky=tk.W, padx=1, pady=1)
        self.e_cShoulderToUBust = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cShoulderToUBust.grid(column=1, row=6, sticky=tk.W, padx=1, pady=1)
        self.e_cShoulderToWaist = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cShoulderToWaist.grid(column=1, row=7, sticky=tk.W, padx=1, pady=1)
        self.e_cShoulderToHip = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cShoulderToHip.grid(column=1, row=8, sticky=tk.W, padx=1, pady=1)
        self.e_cAcrossBack = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cAcrossBack.grid(column=1, row=9, sticky=tk.W, padx=1, pady=1)
        self.e_cAcrossChest = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cAcrossChest.grid(column=4, row=0, sticky=tk.E, padx=1, pady=1)
        self.e_cAroundArm = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cAroundArm.grid(column=4, row=1, sticky=tk.E, padx=1, pady=1)
        self.e_cNapeToWaist = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cNapeToWaist.grid(column=4, row=2, sticky=tk.E, padx=1, pady=1)
        self.e_cKabaLength = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cKabaLength.grid(column=4, row=3, sticky=tk.E, padx=1, pady=1)
        self.e_cBlouseLength = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cBlouseLength.grid(column=4, row=4, sticky=tk.E, padx=1, pady=1)
        self.e_cSkirtLength = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cSkirtLength.grid(column=4, row=5, sticky=tk.E, padx=1, pady=1)
        self.e_cSlitLength = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cSlitLength.grid(column=4, row=6, sticky=tk.E, padx=1, pady=1)
        self.e_cSleeveLength = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cSleeveLength.grid(column=4, row=7, sticky=tk.E, padx=1, pady=1)
        self.e_cDressLength = ttk.Entry(self.custMeasureDetailFrame, width=8)
        self.e_cDressLength.grid(column=4, row=8, sticky=tk.E, padx=1, pady=1)

        # List box
        self.l_customerList = tk.Listbox(self.custSearchListFrame, height=32)
        # self.l_customerList.grid(column=0, row=0, sticky=tk.W,  rowspan=20)
        self.l_customerList.pack(side='left', fill='both', padx=5, pady=5)
        self.s_scrollCustomers = tk.Scrollbar(self.custSearchListFrame, command=self.l_customerList.yview)
        # s_scrollCustomers.grid(column=1, row=0, sticky=tk.NS)
        self.s_scrollCustomers.pack(side='right', anchor='n', fill='y')
        self.l_customerList.bind('<Double-Button-1>', self.selectitem)

        # Insert customers in listbox
        self.searchCustNames()

        # Function : Get Name of Customers into List
    def searchCustNames(self):
        # Initialize the database connection
        database = sqlite3.connect('dbmeasureup.db')
        cur = database.cursor()
        query = cur.execute("select c_custName from t_customer")
        rows = query.fetchall()
        # print(rows)
        for row in rows:
            self.l_customerList.insert('end', row[0])

        if database:
            cur.close()
            database.close()

    # Function - double click select list box item
    def selectitem(self, event):

        # Active selected customer on click
        active_cust_select = self.l_customerList.get('active')
        # Connect to db and query
        database = sqlite3.connect('dbmeasureup.db')
        cur = database.cursor()
        v_mycustomerid = cur.execute("select * from t_customer where c_custName= '" + str(active_cust_select) + "'")
        rows = v_mycustomerid.fetchall()
        #print(rows)
        cName = rows[0][1]
        cDate = rows[0][2]
        cMob1 = rows[0][3]
        cMob2 = rows[0][4]
        cEMail = rows[0][5]
        cAddress = rows[0][6]
        cGender = rows[0][7]

        #ttk.Label(self.DetailFrame, text=' ').grid(column=4, row=0, sticky=tk.W, padx=1, pady=1)
        #ttk.Label(self.DetailFrame, text='           ').grid(column=2, row=1, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text=' ').grid(column=2, row=2, sticky=tk.W, padx=1, pady=1)
        self.e_cName.delete('0', 'end')
        self.e_cMobNum1.delete('0', 'end')
        self.e_cMobNum2.delete('0', 'end')
        self.e_cEMail.delete('0', 'end')
        self.e_cAddress.delete('0', 'end')

        #ttk.Label(self.DetailFrame, text=str(cName)).grid(column=2, row=0, sticky=tk.W, padx=1, pady=1)
        #ttk.Label(self.DetailFrame, text=str(cGender)).grid(column=2, row=1, sticky=tk.W, padx=1, pady=1)
        ttk.Label(self.DetailFrame, text=str(cDate)).grid(column=2, row=2, sticky=tk.W, padx=1, pady=1)
        self.e_cName.insert('0', str(cName))
        self.e_cMobNum1.insert('0',str(cMob1))
        self.e_cMobNum2.insert('0', str(cMob2))
        self.e_cEMail.insert('0', str(cEMail))
        self.e_cAddress.insert('0', str(cAddress))

        # Get customer id
        query = cur.execute("select c_customerID from t_customer where c_custName = '" + str(active_cust_select) + "'")
        id_rows = query.fetchall()[0][0]
        #print(q_rows)
        q_query = cur.execute("select * from t_custMeasurements where c_customerID = '" + str(id_rows) + "'")
        q_rows =  q_query.fetchall()
        #print(q_rows)

        self.e_cBust.delete('0', 'end')
        self.e_cWaist.delete('0', 'end')
        self.e_cHip.delete('0', 'end')
        self.e_cShoulder.delete('0', 'end')
        self.e_cShoulderToNip.delete('0', 'end')
        self.e_cNipToNip.delete('0', 'end')
        self.e_cShoulderToUBust.delete('0', 'end')
        self.e_cShoulderToWaist.delete('0', 'end')
        self.e_cShoulderToHip.delete('0', 'end')
        self.e_cAcrossBack.delete('0', 'end')
        self.e_cAcrossChest.delete('0', 'end')
        self.e_cAroundArm.delete('0', 'end')
        self.e_cNapeToWaist.delete('0', 'end')
        self.e_cKabaLength.delete('0', 'end')
        self.e_cBlouseLength.delete('0', 'end')
        self.e_cSkirtLength.delete('0', 'end')
        self.e_cSlitLength.delete('0', 'end')
        self.e_cSleeveLength.delete('0', 'end')
        self.e_cDressLength.delete('0', 'end')

        self.e_cBust.insert('end', str(q_rows[0][2]))
        self.e_cWaist.insert('end', str(q_rows[0][3]))
        self.e_cHip.insert('end', str(q_rows[0][4]))
        self.e_cShoulder.insert('end', str(q_rows[0][5]))
        self.e_cShoulderToNip.insert('end', str(q_rows[0][6]))
        self.e_cNipToNip.insert('end', str(q_rows[0][7]))
        self.e_cShoulderToUBust.insert('end', str(q_rows[0][8]))
        self.e_cShoulderToWaist.insert('end', str(q_rows[0][9]))
        self.e_cShoulderToHip.insert('end', str(q_rows[0][10]))
        self.e_cAcrossBack.insert('end', str(q_rows[0][11]))
        self.e_cAcrossChest.insert('end', str(q_rows[0][12]))
        self.e_cAroundArm.insert('end', str(q_rows[0][13]))
        self.e_cNapeToWaist.insert('end', str(q_rows[0][14]))
        self.e_cKabaLength.insert('end', str(q_rows[0][15]))
        self.e_cBlouseLength.insert('end', str(q_rows[0][16]))
        self.e_cSkirtLength.insert('end', str(q_rows[0][17]))
        self.e_cSlitLength.insert('end', str(q_rows[0][18]))
        self.e_cSleeveLength.insert('end', str(q_rows[0][19]))
        self.e_cDressLength.insert('end', str(q_rows[0][20]))

        if database:
            cur.close()
            database.close()

    def deleteUserCmd(self):
        #print()
        # Active selected customer on click
        active_cust_select = self.l_customerList.get('active')

        showmessage = "Really delete " + str(active_cust_select) + "'s record? "
        res = mbox.askyesno('Warning', showmessage)
        #print(res)
        if res == True:
            #print("True")
            # Connect to db and query
            database = sqlite3.connect('dbmeasureup.db')
            cur = database.cursor()
            # Get customer id
            query = cur.execute("select c_customerID from t_customer where c_custName = '" + str(active_cust_select) + "'")
            q_rows = query.fetchall()[0][0]
            #print(q_rows)
            q_query1 = cur.execute("delete from t_custMeasurements where c_customerID = '" + str(q_rows) + "'")
            database.commit()
            q_query2 = cur.execute("delete from t_customer where c_customerID = '" + str(q_rows) + "'")
            database.commit()
            #q_rows = q_query.fetchall()
            # print(q_rows)


            # Set all entries  to blank after delete
            def emptyEntries(self):
                ttk.Label(self.DetailFrame, text='                                      ').grid(column=2, row=2, sticky=tk.W, padx=1, pady=1)
                self.e_cName.delete('0', 'end')
                self.e_cMobNum1.delete('0', 'end')
                self.e_cMobNum2.delete('0', 'end')
                self.e_cEMail.delete('0', 'end')
                self.e_cAddress.delete('0', 'end')
                self.e_cBust.delete('0', 'end')
                self.e_cWaist.delete('0', 'end')
                self.e_cHip.delete('0', 'end')
                self.e_cShoulder.delete('0', 'end')
                self.e_cShoulderToNip.delete('0', 'end')
                self.e_cNipToNip.delete('0', 'end')
                self.e_cShoulderToUBust.delete('0', 'end')
                self.e_cShoulderToWaist.delete('0', 'end')
                self.e_cShoulderToHip.delete('0', 'end')
                self.e_cAcrossBack.delete('0', 'end')
                self.e_cAcrossChest.delete('0', 'end')
                self.e_cAroundArm.delete('0', 'end')
                self.e_cNapeToWaist.delete('0', 'end')
                self.e_cKabaLength.delete('0', 'end')
                self.e_cBlouseLength.delete('0', 'end')
                self.e_cSkirtLength.delete('0', 'end')
                self.e_cSlitLength.delete('0', 'end')
                self.e_cSleeveLength.delete('0', 'end')
                self.e_cDressLength.delete('0', 'end')
                myindex = self.l_customerList.size()
                #print(str(myindex))
                self.l_customerList.delete(0, myindex)

                query1 = cur.execute("select c_custName from t_customer")
                rows = query1.fetchall()
                print(rows)
                for row in rows:
                    self.l_customerList.insert('end', row[0])
                    self.l_customerList.focus_set()

            emptyEntries(self)


            if database:
                cur.close()
                database.close()

        else:
            print()



def main():
    app = tk.Tk()
    MainWindow(app)
    app.mainloop()

if __name__ == '__main__':
    main()