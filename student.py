from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self , root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        
        
        #=======================variables
        
        self.var_stid=StringVar()
        self.var_course=StringVar()
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_sec=StringVar()
        self.var_enroll=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_add=StringVar()
        self.var_rad1=StringVar()
        #self.var_rad2=StringVar()
        
        
        img = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img = img.resize((1600,180),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        flb = Label(self.root,image=self.photoimg)
        flb.place(x=0,y=0,width=1600,height=180)
        
        #bg
        bg = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\collection-young-people-background-collage-large-group-smiling-faces-social-media-80759124.jpg")
        bg = bg.resize((1600,850),Image.Resampling.LANCZOS)
        self.photobg=ImageTk.PhotoImage(bg)
        
        flbg = Label(self.root,image=self.photobg)
        flbg.place(x=0,y=180,width=1600,height=670)
        
        title_bg = Label(flbg, text="Student Managment System",font=("Times New Roman", 35, "bold italic"), bg = "dark gray")
        title_bg.place(x=0,y=0, width=1600, height=45)
        
        main_frame=Frame(flbg,bd=2)
        main_frame.place(x=0, y=47,width=1600,height=650)
        
        #left label frmae
        
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=("times new  roman",12,"bold"))
        left_frame.place(x=10, y=10,width=750, height=580)
        
        img1 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img1 = img1.resize((740,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        flb1 = Label(left_frame,image=self.photoimg1)
        flb1.place(x=4,y=0,width=740,height=150)
        
        #curent course
        curent_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course", font=("times new  roman",12,"bold"))
        curent_frame.place(x=5, y=150,width=740, height=105)
        
        #course
        course_label=Label(curent_frame,text="Course", font=("times new roman",13, "bold"),bg="white")
        course_label.grid(row=0, column=0,padx=10, sticky=W)
        
        course_combo=ttk.Combobox(curent_frame,textvariable=self.var_course,font=("times new roman", 13, "bold") , state="readonly",width=20)
        course_combo["values"]=("Select Course" ,"Btech","Mtech", "B Pharma" , "M Pharma")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=10, sticky=W)
        #course_combo=ttk.Combobox(curent_frame,textvariable=self.var_course,font=("times new roman", 13, "bold") , state="readonly",width=20)
        #course_combo["values"]=("Select Course" , "Btech","Mtech", "B Pharma" , "M Pharma")
        #course_combo.current(0)
        #course_combo.grid(row=0,column=1,padx=10, sticky=W)
        
        #department
        dep_label=Label(curent_frame,text="Department", font=("times new roman",13, "bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10, sticky=W)
        
        dep_combo=ttk.Combobox(curent_frame,textvariable=self.var_dep,font=("times new roman", 13, "bold") , state="readonly",width=20)
        dep_combo["values"]=("Select Department" , "Computer Science","it", "Civil Engineering" , "Machanical engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=10,pady=5, sticky=W)
        
        #semester
        sem_label=Label(curent_frame,text="Semester", font=("times new roman",13, "bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=12,pady=10, sticky=W)
        
        sem_combo=ttk.Combobox(curent_frame,textvariable=self.var_sem,font=("times new roman", 13, "bold") , state="readonly",width=20)
        sem_combo["values"]=("Select Semester" , "1st", "2nd" ,"3rd" ,"4rth" , "5th" ,"6th" ,"7th" ,"8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=10,pady=10 ,sticky=W)
        
        
        #section
        sec_label=Label(curent_frame,text="Section", font=("times new roman",13, "bold"),bg="white")
        sec_label.grid(row=1,column=2,padx=12,pady=10, sticky=W)
        
        sec_combo=ttk.Combobox(curent_frame,textvariable=self.var_sec,font=("times new roman", 13, "bold") , state="readonly",width=20)
        sec_combo["values"]=("None" , "A", "B" , "C")
        sec_combo.current(0)
        sec_combo.grid(row=1,column=3,padx=10,pady=10 ,sticky=W)
        
        
        
        #leftnthird  label
        
        thleft_label=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Information" ,font=("times new roman" , 13, "bold"))
        thleft_label.place(x=15,y=290,height=295,width=740)    
        
        #enrollment
        enroll_label=Label(thleft_label,text="Enrollment no.",font=("times new roman", 13 , "bold"),bg="white")
        enroll_label.grid(row=1,column=0,padx=10, pady=5,sticky=W)
        
        enroll_entry=ttk.Entry(thleft_label,textvariable=self.var_enroll,width=25,font=("times new roman", 13, "bold"))
        enroll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #name
        name_label=Label(thleft_label,text="Name",font=("times new roman", 13 , "bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5, sticky=W)
        
        name_entry=ttk.Entry(thleft_label,textvariable=self.var_name,width=25,font=("times new roman", 13, "bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #student id
        stid_label=Label(thleft_label,text="Student_Id",font=("times new roman", 13 , "bold"),bg="white")
        stid_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)
        
        stid_entry=ttk.Entry(thleft_label,textvariable=self.var_stid,width=25,font=("times new roman", 13, "bold"))
        stid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #gender
        gender_label=Label(thleft_label,text="Gender",font=("times new roman", 13 , "bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10, pady=5,sticky=W)
        
        #gender_entry=ttk.Entry(thleft_label,textvariable=self.var_gender,width=25,font=("times new roman", 13, "bold"))
        #gender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(thleft_label,width=23,textvariable=self.var_gender,font=("times new roman",13,"bold"), state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Trans")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #dob
        dob_label=Label(thleft_label,text="Dob",font=("times new roman", 13 , "bold"),bg="white")
        dob_label.grid(row=3,column=0,padx=10, pady=5,sticky=W)
        
        dob_entry=ttk.Entry(thleft_label,textvariable=self.var_dob,width=25,font=("times new roman", 13, "bold"))
        dob_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone
        phone_label=Label(thleft_label,text="Phone",font=("times new roman", 13 , "bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10, pady=5,sticky=W)
        
        phone_entry=ttk.Entry(thleft_label,textvariable=self.var_phone,width=25,font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label=Label(thleft_label,text="Email",font=("times new roman", 13 , "bold"),bg="white")
        email_label.grid(row=4,column=0,padx=10, pady=5,sticky=W)
        
        email_entry=ttk.Entry(thleft_label,textvariable=self.var_email,width=25,font=("times new roman", 13, "bold"))
        email_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Adress
        adress_label=Label(thleft_label,text="Address",font=("times new roman", 13 , "bold"),bg="white")
        adress_label.grid(row=4,column=2,padx=10, pady=5,sticky=W)
        
        adress_entry=ttk.Entry(thleft_label,textvariable=self.var_add,width=25,font=("times new roman", 13, "bold"))
        adress_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #radio buttons
        self.var_rad1=StringVar()
        Radiobutton1=ttk.Radiobutton(thleft_label,variable=self.var_rad1,text="Take Photo sample", value="yes")
        Radiobutton1.grid(row=5,column=0,pady=20,)
        
        Radiobutton2=ttk.Radiobutton(thleft_label,variable=self.var_rad1,text="No Photos sample", value="no")
        Radiobutton2.grid(row=5,column=1,pady=20,)
        
        
        #buttons frame
        btn_frame=Frame(thleft_label,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=186,width=735,height=35)
        
        #buttons frame
        btn1_frame=Frame(thleft_label,bd=2,relief=RIDGE)
        btn1_frame.place(x=0,y=220,width=735,height=35)
        
        #save buttton
        sv_butt=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        sv_butt.grid(row=0, column=0)
        
        #update buttton
        upd_butt=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        upd_butt.grid(row=0, column=1)
        
        #delete buttton
        del_butt=Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        del_butt.grid(row=0, column=2)
        
        #reset buttton
        res_butt=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        res_butt.grid(row=0, column=3)
        
        #take photo
        tp_butt=Button(btn1_frame,command=self.generate_dataset,text="Take photo",width=40,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        tp_butt.grid(row=0, column=0)
        
        #update photo
        up_butt=Button(btn1_frame,text="Update  photo",width=40,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        up_butt.grid(row=0, column=1)
        
        
        

        
        
        
        
        
        
        #right label frmae
        
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="students details", font=("times new  roman",12,"bold"))
        right_frame.place(x=764, y=10,width=747, height=580)
        
        img2 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\photos\library-1147815_1920.jpg")
        img2 = img2.resize((735,150),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        flb2 = Label(right_frame,image=self.photoimg2)
        flb2.place(x=4,y=0,width=735,height=150)
        
        #search system
        curent_framee=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search Details", font=("times new  roman",12,"bold"))
        curent_framee.place(x=2, y=150,width=735, height=70)
        
        searchba_label=Label(curent_framee,text="Search By",font=("times new roman", 13 , "bold"),bg="light blue")
        searchba_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)
        
        sear_combo=ttk.Combobox(curent_framee,font=("times new roman", 13, "bold") , state="readonly",width=15)
        sear_combo["values"]=("Select" , "Enrollment no.", "Phone")
        sear_combo.current(0)
        sear_combo.grid(row=0,column=1,padx=10,pady=10 ,sticky=W)
        
        sear_entry=ttk.Entry(curent_framee,width=15,font=("times new roman", 15, "bold"))
        sear_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        sea_butt=Button(curent_framee,text="Search",width=15,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        sea_butt.grid(row=0, column=3)
        
        sho_butt=Button(curent_framee,text="Showall",width=15,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        sho_butt.grid(row=0, column=4)
        
        curentt_framee=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        curentt_framee.place(x=2, y=220,width=735, height=330)
        
        Scrollbar_x=ttk.Scrollbar(curentt_framee,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(curentt_framee,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(curentt_framee,column=("Student_Id","Course","Dep","Sem","Sec","Enroll no.","Name","Gender","DOB","phone no","Email","Address"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.student_table.xview)
        Scrollbar_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Student_Id", text="Student_Id")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Sec", text="Section")
        self.student_table.heading("Enroll no.", text="Enrollment no.")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("phone no", text="Phone no.")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #==================================function declration=====================================
        
    def add_data(self):
            if self.var_course.get()=="Select course" or self.var_name.get()=="" or self.var_enroll.get()=="":
                messagebox.showerror("Error"," All fields are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sahil@123",database="sys")
                    my_cursur=conn.cursor()
                    my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_stid.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_sec.get(),
                                                                                                                self.var_enroll.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_add.get(), 
                                                                                                                self.var_rad1.get()                             
                    
                                                                                                            ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","student details has been added successfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
        
        
        #fetch data
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sahil@123",database="sys")
        my_cursur=conn.cursor()
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student")
        data=my_cursur.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        #======================get cursor=============================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_stid.set(data[0])
        self.var_course.set(data[1])
        self.var_dep.set(data[2])
        self.var_sem.set(data[3])
        self.var_sec.set(data[4])
        self.var_enroll.set(data[5])
        self.var_name.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_phone.set(data[9])
        self.var_email.set(data[10])
        self.var_add.set(data[11])
        self.var_course.set(data[12])
        #self.var_rad1.set(data[13])
        
        
        #UPDATE FUNCTIONS
        
    def update_data(self):
        if self.var_course.get()=="Select course" or self.var_name.get()=="" or self.var_enroll.get()=="":
            messagebox.showerror("Error"," All fields are required")
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sahil@123",database="sys")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update student set course=%s,department=%s,semester=%s,section=%s,Enrollment_no=%s,Name=%s,gender=%s,dob=%s,phone_number=%s,email=%s,address=%s,photosample=%s where student_id=%s",(
                        
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                            self.var_enroll.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_add.get(),
                                                                                                                                                                                            self.var_rad1.get(),
                                                                                                                                                                                            self.var_stid.get(),
                                                                                                                                                                                    ))
                    
                else:
                    if not Update:
                        return
                    
                messagebox.showinfo("Succes","Student details updated succefully ",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
               messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
               
               
    #deletfunction
    def delete_data(self):
        if self.var_stid.get()=="":
            messagebox.showerror("Error","Student_Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","do you want to delete this students data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sahil@123",database="sys")
                    my_cursur=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_stid.get(),)
                    my_cursur.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Successfuly deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)          
                
                
#reset button

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")  
        self.var_sem.set("Select Semester")  
        self.var_sec.set("None")  
        self.var_stid.set("")  
        self.var_stid.set("")   
        self.var_name.set("")  
        self.var_enroll.set("")  
        self.var_gender.set("Select Gender") 
        self.var_dob.set("") 
        self.var_phone.set("") 
        self.var_email.set("") 
        self.var_add.set("") 


# =========take photo

    def generate_dataset(self):
        if self.var_course.get()=="Select course" or self.var_name.get()=="" or self.var_enroll.get()=="":
            messagebox.showerror("Error"," All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sahil@123",database="sys")
                my_cursur=conn.cursor()
                my_cursur.execute("Select * from student")
                myresult=my_cursur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursur.execute("update student set course=%s,department=%s,semester=%s,section=%s,Enrollment_no=%s,Name=%s,gender=%s,dob=%s,phone_number=%s,email=%s,address=%s,photosample=%s where student_id=%s",(
                        
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                            self.var_enroll.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_add.get(),
                                                                                                                                                                                            self.var_rad1.get(),
                                                                                                                                                                                            self.var_stid.get()==id+1
                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
     #           ==================face frontals fromopencv
     
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret , my_frame=cap.read()
                    #cropped_face = face_cropped(my_frame)
                
                    if face_cropped(my_frame) is not None:
                       img_id += 1
                       face=cv2.resize(face_cropped(my_frame),(450,450))
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)     
                       file_name_path=f"data/user.{id}.{img_id}.jpg"  
                       cv2.imwrite(file_name_path, face)
                       cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                       #cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Crooped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                   
        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()