from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import *
import cv2
from datetime import datetime
from time import strftime
#from matplotlib import widgets
import mysql.connector
import os
import csv
from tkinter import filedialog 

myData=[]
class attendance_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        #variables
        self.var_at_attid=StringVar()
        self.var_at_enroll=StringVar()
        self.var_at_dep=StringVar()
        self.var_at_name=StringVar()
        self.var_at_date=StringVar()
        self.var_at_time=StringVar()
        self.var_at_att=StringVar()
        
        
        #img
        img = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img = img.resize((1600,180),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        flb = Label(self.root,image=self.photoimg)
        flb.place(x=0,y=0,width=1600,height=180)
        
        #bg
        bg = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\leafless-tree-snowy-hill-with-cloudy-sky-background-black-white.jpg")
        bg = bg.resize((1600,850),Image.Resampling.LANCZOS)
        self.photobg=ImageTk.PhotoImage(bg)
        
        flbg = Label(self.root,image=self.photobg)
        flbg.place(x=0,y=180,width=1600,height=670)
        
        #title
        title_bg = Label(flbg, text="NIRT ATTENDANCE SYSTEM",font=("Times New Roman", 35, "bold italic"), bg = "dark gray")
        title_bg.place(x=0,y=0, width=1600, height=45)
        
        #main frame
        main_frame=Frame(flbg,bd=2)
        main_frame.place(x=10, y=50,width=1510,height=600)
        
        #left frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=("times new  roman",12,"bold"))
        left_frame.place(x=10, y=10,width=760, height=580)
        
        img1 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img1 = img1.resize((740,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        flb1 = Label(left_frame,image=self.photoimg1)
        flb1.place(x=4,y=0,width=750,height=150)
        
        leftin_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        leftin_frame.place(x=3, y=155,width=750,height=400)
        
        ##labels  and entry
        #attendence id
        Aid_label=Label(leftin_frame,text="Attendance id.",font=("times new roman", 15 , "bold"),bg="white")
        Aid_label.grid(row=0,column=0,padx=10, pady=10,sticky=W)
        
        Aid_entry=ttk.Entry(leftin_frame,textvariable=self.var_at_attid,width=20,font=("times new roman", 15, "bold"))
        Aid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #enroll
        enroll_label=Label(leftin_frame,text="Enrollment no.",font=("times new roman", 15 , "bold"),bg="white")
        enroll_label.grid(row=0,column=2,padx=10, pady=10,sticky=W)
        
        enroll_entry=ttk.Entry(leftin_frame,textvariable=self.var_at_enroll,width=20,font=("times new roman", 15, "bold"))
        enroll_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
        #Name 
        name_label=Label(leftin_frame,text="Name",font=("times new roman", 15 , "bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10, pady=10,sticky=W)
        
        name_entry=ttk.Entry(leftin_frame,textvariable=self.var_at_name,width=20,font=("times new roman", 15, "bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #Department 
        Dep_label=Label(leftin_frame,text="Department",font=("times new roman", 15 , "bold"),bg="white")
        Dep_label.grid(row=1,column=2,padx=10, pady=10,sticky=W)
        
        Dep_entry=ttk.Entry(leftin_frame,textvariable=self.var_at_dep,width=20,font=("times new roman", 15, "bold"))
        Dep_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #Date 
        date_label=Label(leftin_frame,text="Date.",font=("times new roman", 15 , "bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10, pady=10,sticky=W)
        
        date_entry=ttk.Entry(leftin_frame,textvariable=self.var_at_date,width=20,font=("times new roman", 15, "bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #Time
        time_label=Label(leftin_frame,text="Time",font=("times new roman", 15 , "bold"),bg="white")
        time_label.grid(row=2,column=2,padx=10, pady=10,sticky=W)
        
        time_entry=ttk.Entry(leftin_frame,textvariable=self.var_at_time,width=20,font=("times new roman", 15, "bold"))
        time_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        
        #attendance ststus
        sec_label=Label(leftin_frame,text="Attendance", font=("times new roman",15, "bold"),bg="white")
        sec_label.grid(row=3,column=0,padx=10,pady=10, sticky=W)
        
        sec_combo=ttk.Combobox(leftin_frame,textvariable=self.var_at_att,font=("times new roman", 15, "bold") , state="readonly",width=18)
        sec_combo["values"]=("Status" , "Present", "Absent")
        sec_combo.current(0)
        sec_combo.grid(row=3,column=1,padx=10,pady=10 ,sticky=W)
        
        #btnframe
        btn_frame=Frame(leftin_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=745,height=145)
        
        #save buttton
        sv_butt=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        sv_butt.grid(row=4, column=0)
        
        #update buttton
        upd_butt=Button(btn_frame,text="Export csc",command=self.exportCsv,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        upd_butt.grid(row=4, column=1)
        
        #delete buttton
        del_butt=Button(btn_frame,text="Update",width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        del_butt.grid(row=4, column=2)
        
        #reset buttton
        res_butt=Button(btn_frame,text="Reset",command=self.reset_cursor,width=20,font=("times new roman", 12, "bold"),bg="dark blue", fg="white",cursor="hand2")
        res_butt.grid(row=4, column=3)
        
        
        #right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=("times new  roman",12,"bold"))
        right_frame.place(x=770, y=10,width=730, height=580)
        
        curent_fram=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        curent_fram.place(x=2, y=0,width=720, height=550)
        
        #scrooll bar
        scroll_x=ttk.Scrollbar(curent_fram,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(curent_fram,orient=VERTICAL)
        
        self.attendanceReportTable=ttk.Treeview(curent_fram,column=("Attendance id","Enrollment no.","Department","Name","Date.","Time","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)
        
        self.attendanceReportTable.heading("Attendance id",text="Attendance Id")
        self.attendanceReportTable.heading("Enrollment no.",text="Enrollment no.")
        self.attendanceReportTable.heading("Department",text="Department")
        self.attendanceReportTable.heading("Name",text="Name")
        self.attendanceReportTable.heading("Date.",text="Date.")
        self.attendanceReportTable.heading("Time",text="Time")
        self.attendanceReportTable.heading("Attendance",text="Attendance")
        
        self.attendanceReportTable["show"]="headings"
        
        self.attendanceReportTable.column("Attendance id",width=120)
        self.attendanceReportTable.column("Enrollment no.",width=120)
        self.attendanceReportTable.column("Department",width=120)
        self.attendanceReportTable.column("Name",width=100)
        self.attendanceReportTable.column("Date.",width=100)
        self.attendanceReportTable.column("Time",width=100)
        self.attendanceReportTable.column("Attendance",width=120)

        
        self.attendanceReportTable.pack(fill=BOTH,expand=1)
        #widgets.bind("<Button-1>", self.get_cursur)

        self.attendanceReportTable.bind("<ButtonRelease-1>", lambda event: self.get_cursur())
        #self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursur)
        
        
        #facedata
    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)
    
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
        self.fetchData(myData)
            
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="\n") as myfile:
                expot=csv.writer(myfile,delimiter=",")
                for i in myData:
                    expot.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported Succesfully to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
    def get_cursur(self):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_at_attid.set(rows[0])
        self.var_at_enroll.set(rows[1])
        self.var_at_dep.set(rows[2])
        self.var_at_name.set(rows[3])
        self.var_at_date.set(rows[4])
        self.var_at_time.set(rows[5])
        self.var_at_att.set(rows[6])
        
    def reset_cursor(self):
        self.var_at_attid.set("")
        self.var_at_enroll.set("")
        self.var_at_dep.set("")
        self.var_at_name.set("")
        self.var_at_date.set("")
        self.var_at_time.set("")
        self.var_at_att.set("status")
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=attendance_system(root)
    root.mainloop()