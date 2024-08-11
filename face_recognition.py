from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import *
import cv2
from datetime import datetime
from time import strftime
import mysql.connector
import os

class Face_recognition:
    def __init__(self , root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        #title_bg.place(x=0,y=0, width=1600, height=50)
        
        #img
        
        img = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img = img.resize((810,750),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        
        lbg=Label(self.root,image=self.photoimage)
        lbg.place(x=0,y=50,height=750,width=750)
        
        
        #ljsfv
        
        img2 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img2 = img2.resize((1650,50),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        
        lbg2=Label(self.root,image=self.photoimage2)
        lbg2.place(x=0,y=0,height=50,width=1650)
        
        title_bg = Label(lbg2,text="NIRT ATTENDANCE SYSTEM",font=("Times New Roman", 40, "bold italic"), bg = "dark gray")
        title_bg.place(x=0,y=0, width=1600, height=50)
        
        
        #image2
        
        img1=Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\face-detection-4760361_1280.jpg")
        img1=img1.resize((800,800),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        lb2=Label(self.root,image=self.photoimage1)
        lb2.place(x=750,y=50,height=750,width=800)
        
        bt1=Button(lb2,text="detect face",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="light green")
        bt1.place(x=241,y=580,width=314)
        
        
        img3 = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img3 = img3.resize((1650,50),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        
        lbg3=Label(self.root,image=self.photoimage3)
        lbg3.place(x=0,y=800,height=50,width=1650)
        
        lbg3=Label(lbg3,text="Face Detecting Program",font=("times new roman",24,"bold"),bg="gray")
        lbg3.place(x=0,y=0, height=50,width=1650)
        
        
        self.root.bind('<Return>', self.save_info_to_csv)
        
    def save_info_to_csv(self, event=None):
        # Save information to CSV file
        # Replace this with your implementation to save the information to CSV
        messagebox.showinfo("Information Saved", "Information has been saved to CSV file.")
        
        #attendence
    def mark_attendence(self,i,e,n,d):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
    
        #with open("sahil.csv", "a", newline="\n") as f:
        #    f.write(f"\n{i},{e},{n},{d},{dtString},{d1},Present")
            

        with open("sahil.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (e not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{e},{n},{d},{dtString},{d1},Present")
                
            
        
        #face recog  dc
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
            
            coord=[]
            #dc
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Sahil@123",database="sys")
                my_cursur=conn.cursor()
                
                my_cursur.execute("select Name from student where student_id="+str(id))
                n=my_cursur.fetchone()
                n="+".join(n)
                
                my_cursur.execute("select Enrollment_no from student where student_id="+str(id))
                e=my_cursur.fetchone()
                e="+".join(e)
                
                my_cursur.execute("select department from student where student_id="+str(id))
                d=my_cursur.fetchone()
                d="+".join(d)
                
                my_cursur.execute("select student_id from student where student_id="+str(id))
                i=my_cursur.fetchone()
                i="+".join(i)
              
              #dc  
                if confidence>77:
                    cv2.putText(img,f"student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Enrollment_no:{e}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,e,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
                
            return coord
        #dc
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
                 
   
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()