from tkinter import*
from tkinter import ttk
import pymysql
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management system")
        self.root.geometry("1600x900+0+0")
        title=Label(self.root,text="student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg="green")
        title.pack(side=TOP,fill=X)

        #=========variables========

        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=20,y=100,width=450,height=670)

        m_title=Label(Manage_Frame,text="manage students",bg="black",fg="green",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll number",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="name",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="email",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_gender=Label(Manage_Frame,text="gender",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        

        lbl_contact=Label(Manage_Frame,text="contact",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_Frame,text="DOB",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="address",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=20,height=3)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=10,y=500,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)


        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=500,y=100,width=950,height=670)

        lbl_search=Label(Detail_Frame,text="search by",bg="black",fg="green",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=("roll","name","contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(Detail_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="search",width=10).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="showall",width=10).grid(row=0,column=4,padx=10,pady=10)



        table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="black")
        table_Frame.place(x=10,y=70,width=830,height=550)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)
        student_table=ttk.Treeview(table_Frame,columns=("roll","name","gender","contact","dob","email","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("roll",text="roll number")
        student_table.heading("name",text="Name")
        student_table.heading("gender",text="Gender")
        student_table.heading("contact",text="contact number")
        student_table.heading("dob",text="DOB")
        student_table.heading("email",text="email ID")
        student_table.heading("address",text="address")
        student_table['show']='headings'
        student_table.pack(fill=BOTH,expand=1)
    def add_students(self):    
        
           
            con=pymysql.connect(host="localhost",user="root",password="",database="stms")
            cur=con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END)
                                                                             ))
            con.commit()
            con.close()
 

root=Tk()
ob=student(root)
root.mainloop()
