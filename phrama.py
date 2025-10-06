from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")  
        self.root.geometry("1550x800+0+0")             
 
#  ===================== addmed variable==============

        self.refmed_var = StringVar()
        self.addmed_var = StringVar()

# ====================== main conection variable===================

        self.reg_var = StringVar()
        self.companyname_var = StringVar()
        self.type_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedate_var = StringVar()
        self.ExpiryDate_var = StringVar()
        self.Sideeffect_var = StringVar()
        self.preswarning_var = StringVar()
        self.productQT_var = StringVar()
        self.Dosage_var = StringVar()


        # Label 
        lbltitle = Label(
            self.root,
            text="Pharmacy Management System",
            bd=15,
            relief=RIDGE,
            bg="white",
            fg="darkgreen",
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=4
        )

        lbltitle.pack(side=TOP, fill=X)  
        img1 = Image.open("C:\\Users\\Dell\\Desktop\\python projects\\P M S\\logo.png")

        img1 = img1.resize((80,80),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)
        
        # ===================== Dataframe=====================

        DataFrame = Frame(self.root,bd=15, relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

       

        DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,font=("times new roman", 13, "bold"),
                                      text= "Medicine Imformation",fg="darkgreen")
        DataFrameLeft.place(x=0,y=5,width=900,height=350)


       

        # =======================Button Frame========================

        ButtonFrame = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        # ========================main button========================

        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial", 12, "bold"),
                                                  fg="white", bg="#87CEFA")
        btnAddData.grid(row=0,column=0,padx=5, pady=3)

        btnAddData=Button(ButtonFrame,text="Update",font=("arial", 13, "bold"),
                                                  fg="white", bg="#87CEFA")
        btnAddData.grid(row=0,column=1,padx=5, pady=3)

        btnAddData=Button(ButtonFrame,text="Reset",font=("arial", 13, "bold"),
                                                  fg="white", bg="#87CEFA")
        btnAddData.grid(row=0,column=2,padx=5, pady=3)

        btnAddData=Button(ButtonFrame,text="Exist",font=("arial", 13, "bold"),
                                                  fg="white", bg="#FF9999")
        btnAddData.grid(row=0,column=3,padx=5, pady=3)
        
        btnAddData=Button(ButtonFrame,text="Delete",font=("arial", 13, "bold"),
                                                  fg="white", bg="#FF9999")
        btnAddData.grid(row=0,column=4,padx=5, pady=3)
        
        # =========================Search bar==============================

        btnAddData=Button(ButtonFrame,text="Search By",font=("arial", 14, "bold"),
                                                  fg="white", bg="turquoise")
        btnAddData.grid(row=0,column=5,sticky = W)

        search_combo=ttk.Combobox(ButtonFrame,width=17,font=("arial", 15, "bold"),state = "readonly")
        search_combo["values"]= ("Ref", "medname","Lot")
        search_combo.grid(row=0,column=6,padx=5, pady=3)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=20,font=("arial", 15, "bold"))
        txtSearch.grid(row = 0,column=7)

        searchBtn=Button(ButtonFrame,text="Search",font=("arial", 13, "bold"),width=20,
                                                  fg="white", bg="turquoise")
        searchBtn.grid(row=0,column=8,padx=15, pady=5)
        
        ShowBtn=Button(ButtonFrame,text="Show All",font=("arial", 13, "bold"),width=20,
                                                  fg="white", bg="mediumseagreen")
        ShowBtn.grid(row=0,column=9,padx=5, pady=5)


    #    ========================== label and entry========================


        lblrefno=Label(DataFrameLeft,text="Reference  No:",font=("arial", 12, "bold"))                                        
        lblrefno.grid(row=0,column=0,sticky = W)

        conn = psycopg2.connect(host="localhost",database="pharmacy",  user="postgres",password="asad@1122",)
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Reg FROM pharmacy")
        asad = my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.reg_var,width=27,font=("arial", 12,"bold"),state = "readonly")
        ref_combo["values"]= asad
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblCompanyname = Label(DataFrameLeft,text="Company Name:", font=("arial", 12, "bold"),padx=2,pady=6)
        lblCompanyname.grid(row=2, column=0, sticky=W)
        txtCompanyname = Entry(DataFrameLeft, textvariable=self.companyname_var, font=("arial", 12, "bold"), width=29)
        txtCompanyname.grid(row=2, column=1)
          
        # =============================medicien Add========================
        lblmedicineName = Label(DataFrameLeft,text="Medicine Name:",font=("arial", 12, "bold"),padx=2,pady=6) 
        lblmedicineName.grid(row=3,column=0, sticky=W)
        
        conn = psycopg2.connect(host="localhost",database="pharmacy",  user="postgres",password="asad@1122",)
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT medname FROM pharmacy")
        usman = my_cursor.fetchall()
        
        comMedicineName=ttk.Combobox(DataFrameLeft,width=27,font=("arial", 12,"bold"),state = "readonly")
        comMedicineName["values"]= usman
        comMedicineName.grid(row=3,column=1)
        comMedicineName.current(0)
         
        #  == midicine types==
        lblmedicineType = Label(DataFrameLeft,text="Medicine Types:",font=("arial", 12, "bold")) 
        lblmedicineType.grid(row=4,column=0, sticky=W)
        
        comMedicineType=ttk.Combobox(DataFrameLeft,textvariable=self.type_var,width=27,font=("arial", 12,"bold"),state = "readonly")
        comMedicineType["values"]= ("tablets","liquid","topical","drop","inhales","injection")
        comMedicineType.grid(row=4,column=1)
        comMedicineType.current(0)
     
       
        lblLotno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotno.grid(row=5, column=0, sticky=W)
        txtLotno = Entry(DataFrameLeft,textvariable=self.lotno_var,font=("arial", 13, "bold"), width=30)
        txtLotno.grid(row=5, column=1)

        
        
        lblissuedate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissuedate.grid(row=6, column=0, sticky=W)
        txtissuedate = Entry(DataFrameLeft,textvariable=self.issuedate_var, font=("arial", 13, "bold"), width=30)
        txtissuedate.grid(row=6, column=1)
        
        lblexprydate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblexprydate.grid(row=7, column=0, sticky=W)
        txtexprydate = Entry(DataFrameLeft, textvariable=self.ExpiryDate_var, font=("arial", 13, "bold"), width=30)
        txtexprydate.grid(row=7, column=1)
        
        lbluses = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=6)
        lbluses.grid(row=8, column=0, sticky=W)
        txtuses = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=30)
        txtuses.grid(row=8, column=1)
        
        lblsideeffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblsideeffect.grid(row=9, column=0, sticky=W)
        txtsideeffect = Entry(DataFrameLeft,textvariable= self.Sideeffect_var,font=("arial", 13, "bold"), width=30)
        txtsideeffect.grid(row=9, column=1)

    #    ========================================================================

        lblpres = Label(DataFrameLeft, font=("arial", 12, "bold"),text= "pres&warning:",padx=2)
        lblpres.grid(row=0, column=2, sticky=W)
        txtpres = Entry(DataFrameLeft, textvariable=self.preswarning_var,font=("arial", 13, "bold"), width=30)
        txtpres.grid(row=0, column=3)
        
        lbltotalprice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablets price:", padx=2, pady=4)
        lbltotalprice.grid(row=2, column=2, sticky=W)
        txttotalprice = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=30)
        txttotalprice.grid(row=2, column=3)

        
        lblProduct = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Product QT:", padx=2, pady=6)
        lblProduct.grid(row=3, column=2, sticky=W)
        txtProduct = Entry(DataFrameLeft, textvariable=self.productQT_var, font=("arial", 13, "bold"), width=30)
        txtProduct.grid(row=3, column=3)
         
        
        lblDosage = Label(DataFrameLeft, font=("arial", 12, "bold"),text= "Dosage:",padx=2)
        lblDosage.grid(row=4, column=2, sticky=W)
        txtDosage = Entry(DataFrameLeft, textvariable=self.Dosage_var, font=("arial", 13, "bold"), width=30)
        txtDosage.grid(row=4, column=3)

    #   ==================== Images ===============================

  
        img2 = Image.open("C:\\Users\\Dell\\Desktop\\python projects\\P M S\\img2.png")
        img2 = img2.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=490,y=330)
        
        img3 = Image.open("C:\\Users\\Dell\\Desktop\\python projects\\P M S\\img3.png")
        img3 = img3.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=640,y=330)

        img4 = Image.open("C:\\Users\\Dell\\Desktop\\python projects\\P M S\\img9.png")
        img4 = img4.resize((145,135),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=780,y=330)
        
        lblHome = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Stay Safe  Stay Home",
                             padx=2, pady=4,bg="white",fg="red")
        lblHome.place(x=550,y=135)

    #    ==================================Right frame =============================

        DataFrameRight = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,font=("times new roman", 13, "bold"),
                                      text= "Medicine Add department",fg="darkgreen")
        DataFrameRight.place(x=910,y=3,width=540,height=350)



        img5 = Image.open("C:\\Users\\Dell\\Desktop\\python projects\\P M S\\img11.png")
        img5 = img5.resize((180,75),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)


        img6 = Image.open("C:\\Users\\Dell\\Desktop\\python projects\\P M S\\img10.png")
        img6 = img6.resize((180,75),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1130,y=160)

        
        # ============================================================================


        lblrefno = Label(DataFrameRight, font=("arial", 12, "bold"), text="Reference No:")
        lblrefno.place(x=0, y=80)

        txtrefno = Entry(DataFrameRight, textvariable=self.refmed_var, font=("arial", 13, "bold"), width=30)
        txtrefno.place(x=135, y=85)
                                           
        lblMedname = Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name:")
        lblMedname.place(x=0, y=110)

        txtMedname = Entry(DataFrameRight, textvariable=self.addmed_var, font=("arial", 13, "bold"), width=30)
        txtMedname.place(x=135, y=110)


    #   =========================== side frame ==================================

        side_frame = Frame(DataFrameRight, bg="white", bd=4, relief=RIDGE)
        side_frame.place(x=0, y=150, width=290, height=160)

# Scrollbars
        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(
            side_frame,
            columns=("refno", "MedName"),
            xscrollcommand=sc_x.set,
            yscrollcommand=sc_y.set
            )

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("refno", text="Reference No")
        self.medicine_table.heading("MedName", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("refno", width=100)
        self.medicine_table.column("MedName", width=100)
        self.medicine_table.bind("<ButtonRelease-1>",self.medget_cursor)

#       ================  Medicine  Add Buuton =======================
     
        down_frame = Frame(DataFrameRight, bg="grey", bd=4, relief=RIDGE)
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddMed=Button(down_frame,text="Add",width=11,font=("arial", 12, "bold"),fg="white", bg="#87CEFA",command=self.AddMed )
        btnAddMed.grid(row=0,column=0,padx=2,pady=2)

        btnUpdateMed=Button(down_frame,command=self.updateMed,text="Update",width=11,font=("arial", 12, "bold"), fg="white", bg="#87CEFA")
        btnUpdateMed.grid(row=1,column=0,padx=2,pady=2)

        btnDeleteMed=Button(down_frame,command=self.DeleteMed,text="Delete",width=11,font=("arial", 12, "bold"),  fg="white", bg="#FF9999")
        btnDeleteMed.grid(row=2,column=0,padx=2,pady=2)

        btnClearMed=Button(down_frame,command=self.ClearMed,text="clear",width=11,font=("arial", 12, "bold"), fg="white", bg="#FF9999")
        btnClearMed.grid(row=3,column=0,padx=2,pady=2)

    #    =========================== Frame details ==============================

        Framedetails = Frame(self.root,relief=RIDGE ,bd=10)
        Framedetails.place(x=0,y=580,width=1528,height= 210)
  
    
# ============================= main table & scroll bar ==========================

        Table_frame = Frame(self.root,relief=RIDGE)
        Table_frame.place(x=0, y=600, width=1528, height=180)  

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
       
        self.pharmacy_table = ttk.Treeview(
         Table_frame,
               columns=("reg","companyname","type","tablename","lotno","issuedate",
              "ExpiryDate","uses","Sideeffect","pres&warning","tabletsprice","productQT","Dosage"),
               xscrollcommand=scroll_x.set,
                yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Medicine Type")
        self.pharmacy_table.heading("lotno", text="Lot No")
        # self.pharmacy_table.heading("medicnename", text="medicine name")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("ExpiryDate", text="Expiry Date")
        self.pharmacy_table.heading("Sideeffect", text="Side Effect")
        self.pharmacy_table.heading("preswarning", text="Prescription & Warning")
        self.pharmacy_table.heading("tabletsprice", text="Tablet Price")
        self.pharmacy_table.heading("productQT", text="Product Quantity")
        self.pharmacy_table.heading("Dosage", text="Dosage")

# # Columns width
        self.pharmacy_table.column("reg", width=100)
        self.pharmacy_table.column("companyname", width=120)
        self.pharmacy_table.column("type", width=100)
        
        self.pharmacy_table.column("lotno", width=80)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("ExpiryDate", width=100)
        
        self.pharmacy_table.column("Sideeffect", width=120)
        self.pharmacy_table.column("preswarning",  width=150)
        self.pharmacy_table.column("tabletsprice", width=100)
        self.pharmacy_table.column("productQT", width=100)
        self.pharmacy_table.column("Dosage", width=100)
        self.pharmacy_table.pack(fill=BOTH, expand=1)
        self.fetch_dataMed()


    #   ====================== Medicine Funactionlity Decleration========================

  

    def AddMed(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="pharmacy",  
                user="postgres",       
                password="asad@1122",
            )

            my_cursor = conn.cursor()
            my_cursor.execute(
                         "INSERT INTO pharmacy (reg, medname) VALUES (%s, %s)",
                                                   ( self.refmed_var.get(), self.addmed_var.get())   
                                                    )
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success", "Medicine Added")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
    


# =======================================================================

    def fetch_dataMed(self):
        conn = psycopg2.connect(
            host="localhost",
            database="pharmacy",  
            user="postgres",       
            password="asad@1122",
            )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        # =====================================medGetCuersor==============================


    def medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]

        if row:  
            self.refmed_var.set(row[0])   #  column (reg)
            self.addmed_var.set(row[1])   #  column (medname)



    def updateMed(self):

        if self.refmed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = psycopg2.connect(
                    host="localhost",
                    database="pharmacy",  
                    user="postgres",       
                    password="asad@1122",
            )
                my_cursor = conn.cursor()
            
                my_cursor.execute(
                    "UPDATE pharmacy SET medname = %s WHERE reg = %s",
                    (self.addmed_var.get(), self.refmed_var.get())
            )
            
                conn.commit()
                self.fetch_dataMed()   # refresh table
                conn.close()

                messagebox.showinfo("Success", "Medicine has been updated")
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {e}")


    def DeleteMed(self): 
        if self.refmed_var.get() == "":
            messagebox.showerror("Error", "Reference number is required to delete")
        else:
            try:
                conn = psycopg2.connect(
                    host="localhost",
                    database="pharmacy",  
                    user="postgres",       
                    password="asad@1122",
            )
                my_cursor = conn.cursor()

                query = "DELETE FROM pharmacy WHERE reg = %s"
                val = (self.refmed_var.get(),)
                my_cursor.execute(query, val)

                conn.commit()
                self.fetch_dataMed()  # refresh karein table ko
                conn.close()

                messagebox.showinfo("Success", "Medicine Deleted Successfully")

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {e}")
 

    def ClearMed(self):
        try:
            self.refmed_var.set("")
            self.addmed_var.set("")
            messagebox.showinfo("Cleared", "All fields have been cleared")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")



# ===================== main table connection=============================

    def add_data(self):

        if self.reg_var.get() == "" or self.lotno_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return   

        try:
            conn = psycopg2.connect(
                host="localhost",
                database="pharma",  
                user="postgres",       
                password="asad@1122",
            )
            my_cursor = conn.cursor()

            my_cursor.execute(
            """INSERT INTO pharma 
                   (reg, companyname, type, lotno, issuedate, ExpiryDate, Sideeffect, preswarning, tabletsprice, productQT, Dosage) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (
                    self.reg_var.get(),
                    self.companyname_var.get(),
                    self.type_var.get(),
                    self.lotno_var.get(),
                    self.issuedate_var.get(),
                    self.ExpiryDate_var.get(),
                    self.Sideeffect_var.get(),
                    self.preswarning_var.get(),
                    self.tabletsprice_var.get(),
                    self.productQT_var.get(),
                    self.Dosage_var.get()
               )
           )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data has been inserted")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
  







            
if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
