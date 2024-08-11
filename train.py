from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self , root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        img = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\library-1147815_1920.jpg")
        img = img.resize((1600,350),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        flb = Label(self.root,image=self.photoimg)
        flb.place(x=0,y=30,width=1600,height=350)
        
        #bg
        
        title_bg = Label(self.root,text="TRAIN DATA",font=("Times New Roman", 35, "bold italic"), bg = "dark gray")
        title_bg.place(x=0,y=0, width=1600, height=50)
        
        bg = Image.open(r"C:\Users\Sahil\OneDrive\Pictures\Ram\facerecognition\FlashIntegro\New folder\leafless-tree-snowy-hill-with-cloudy-sky-background-black-white.jpg")
        bg = bg.resize((1600,850),Image.Resampling.LANCZOS)
        self.photobg=ImageTk.PhotoImage(bg)
        
        flbg = Label(self.root,image=self.photobg)
        flbg.place(x=0,y=350,width=1600,height=670)
        
        #btn
        bt_1=Button(self.root,text="TRAIN your DATA here",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),fg="green")
        bt_1.place(x=0, y=350,height=60,width=1530)
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
        
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed")
                

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()