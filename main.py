from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
import os
from time import strftime
import datetime as datetime
import tkinter
from train import Train
from face_recognition import Face_recognition
from attendance import attendance_system
from tkinter import filedialog


class Face_Recognition_System:
    def __init__(self , root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        img = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\Am I good enough (1.png")
        img = img.resize((1540,180),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        flb = Label(self.root,image=self.photoimg)
        flb.place(x=0,y=0,width=1540,height=180)
        
        #bg
        bg = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\th (2).jpeg")
        bg = bg.resize((1600,850),Image.Resampling.LANCZOS)
        self.photobg=ImageTk.PhotoImage(bg)
        
        flbg = Label(self.root,image=self.photobg)
        flbg.place(x=0,y=180,width=1600,height=670)
        
        title_bg = Label(flbg, text="NIRT ATTENDANCE SYSTEM",font=("Times New Roman", 35, "bold italic"), bg = "dark gray")
        title_bg.place(x=0,y=0, width=1600, height=45)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
            
        lbl = Label(title_bg, font=('times new roman',14,'bold'),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        #button
        bt1 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\stim.jpg")
        bt1 = bt1.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt=ImageTk.PhotoImage(bt1)
        
        bt1_1=Button(flbg,image=self.photobt,command=self.student_details,cursor="hand2")
        bt1_1.place(x=200,y=80,width=220,height=220)
        
        bt1_1=Button(flbg,text="Student login",command=self.student_details,cursor="hand2",font=("Times New Roman", 20, "bold italic"),bg = "Turquoise" )
        bt1_1.place(x=200,y=300,width=220,height=40)
         
        
        #secon
        bt2 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\collection-young-people-background-collage-large-group-smiling-faces-social-media-80759124.jpg")
        bt2 = bt2.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt2=ImageTk.PhotoImage(bt2) 
        
        bt2_1=Button(flbg,image=self.photobt2,command=self.open_img,cursor="hand2")
        bt2_1.place(x=200,y=370,width=220,height=220)
        
        bt2_1=Button(flbg,text="Data",command=self.open_img,cursor="hand2",font=("Times New Roman", 20, "bold italic"), bg = "Turquoise")
        bt2_1.place(x=200,y=580,width=220,height=40)
        
        #thir
        bt3 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\2473087.jpg")
        bt3 = bt3.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt3=ImageTk.PhotoImage(bt3)
        
        bt3_1=Button(flbg,image=self.photobt3,command=self.face_det,cursor="hand2")
        bt3_1.place(x=800,y=80,width=220,height=220)
        #bt3_1.place(x=500,y=80,width=220,height=220)
        
        bt3_1=Button(flbg,text="Face detector",command=self.face_det,cursor="hand2",font=("Times New Roman", 20, "bold italic"), bg = "Turquoise")
        bt3_1.place(x=800,y=300,width=220,height=40)
        #bt3_1.place(x=500,y=300,width=220,height=40)
        
        #fourth
        bt4 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\R.jpeg")
        bt4 = bt4.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt4=ImageTk.PhotoImage(bt4)
        
        bt4=Button(flbg,image=self.photobt4,cursor="hand2")
        bt4.place(x=500,y=370,width=220,height=220)
        
        bt4_1=Button(flbg,text="Help desk",cursor="hand2",font=("Times New Roman", 20, "bold italic"), bg = "Turquoise")
        bt4_1.place(x=500,y=580,width=220,height=40)
        
        #fifth
        bt5 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\7606066.jpg")
        bt5 = bt5.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt5=ImageTk.PhotoImage(bt5)
        
        bt5=Button(flbg,image=self.photobt5,command=self.attendance_system,cursor="hand2")
        bt5.place(x=1100,y=80,width=220,height=220)
        
        bt5_1=Button(flbg,text="Attendence",command=self.attendance_system,cursor="hand2",font=("Times New Roman", 20, "bold italic"), bg = "Turquoise")
        bt5_1.place(x=1100,y=300,width=220,height=40)
        
        #sixth
        bt6 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\head-663997_1920.jpg")
        bt6 = bt6.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt6=ImageTk.PhotoImage(bt6)
        
        bt6=Button(flbg,image=self.photobt6,command=self.train_data,cursor="hand2")
        bt6.place(x=500,y=80,width=220,height=220)
        #bt6.place(x=1100,y=80,width=220,height=220)
        
        bt6_1=Button(flbg,text="Train face",command=self.train_data,cursor="hand2",font=("Times New Roman", 20, "bold italic"),bg = "Turquoise")
        bt6_1.place(x=500,y=300,width=220,height=40)
        #bt6_1.place(x=1100,y=300,width=220,height=40)
        
        #exit
        bt7 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\Untitled design.png")
        bt7 = bt7.resize((220,220),Image.Resampling.LANCZOS)
        self.photobt7=ImageTk.PhotoImage(bt7)
        
        bt7_1=Button(flbg,image=self.photobt7,command=self.iexit,cursor="hand2")
        bt7_1.place(x=800,y=370,width=220,height=220)
        
        bt7_1=Button(flbg,text="Exit",command=self.iexit,cursor="hand2",font=("Times New Roman", 20, "bold italic"),fg="red", bg = "Turquoise")
        bt7_1.place(x=800,y=580,width=220,height=40)
        
        
        
    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("face Recognition","Are you sure",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
        
    def open_img(self):
        os.startfile("data")
#  =================================Functions buttons====================================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  
    
    def face_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)   
        
    def attendance_system(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_system(self.new_window) 
        
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()