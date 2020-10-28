# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:28:24 2020

@author: vinay
"""

from tkinter import *                           
from tkinter import filedialog     
import os
import webbrowser
from tkinter import messagebox
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk,Image


model = load_model("my_fruits360_model_131classes.h5")
print("[INFO] Model Loaded...")

base_path = os.getcwd()
base_dir = os.path.join(base_path,"fruits-360")
train_dir = os.path.join(base_dir,"Training")
test_dir = os.path.join(base_dir,"Test")
#print("base dir: ",base_dir)
#print("train dir: ",train_dir)
#print("test dir: ",test_dir)


class_names = os.listdir(train_dir)
print("[INFO] Class Names Loaded...")
print("Number of classes: ",len(class_names))

def predictFruitClass(imagepath):
    image=tf.keras.preprocessing.image.load_img(imagepath,target_size=(32,32))
    image=tf.keras.preprocessing.image.img_to_array(image)
    image = image*1./255
    #plt.imshow(image)
    #plt.show()
    #print("image shape:",image.shape)
    batch_image = image[tf.newaxis,...]
    #print("batched image shape: ",batch_image.shape)     
    pred = model.predict(batch_image)
    winner = np.argmax(pred)
    #print("Fruit Name: ",class_names[winner])
    label2.config(text = class_names[winner])
    #print("Accuracy: ",pred[0][winner]*100)
    label4.config(text = str(pred[0][winner]*100)[:6]+"%")


def openFile():
    imagepath = filedialog.askopenfilename(initialdir=os.path.join(os.getcwd(),"fruits-360"),title="Select an Image ",filetypes=(("Image Files","*.jpg"),("Image Files","*.jpeg"),("Image Files","*.png"),("All Files","*.*")))    
    if(imagepath == ""):
        print("select a image file")
    print("path of image: ",imagepath)
    print("")
    global img
    img = ImageTk.PhotoImage(Image.open(imagepath).resize((250, 250), Image.ANTIALIAS))
    canvas.create_image((53,60),image=img,anchor=NW)
    predictFruitClass(imagepath)
    

root=Tk()
root.title("FRUIT  RECOGNITION")
root.geometry("800x400")
root.config(bg="black")

label0=Label(root,text="FRUIT RECOGNITION",bg="black",fg="red",height=1,width=25)
label0.config(font=('arial',18,'bold'))
label0.place(x=410,y=0)
label1=Label(root,text="Fruit Name :",bg="cyan",fg="black",width=17)
label1.config(font=('arial',12,'bold'))
label1.place(x=400,y=100)
label2=Label(root,text="--",bg="cyan",fg="black",width=17)
label2.config(font=('arial',13,'bold'))
label2.place(x=590,y=100)
label3=Label(root,text="Accuracy :",bg="cyan",fg="black",width=17)
label3.config(font=('arial',12,'bold'))
label3.place(x=400,y=160)
label4=Label(root,text="--",bg="cyan",fg="black",width=17)
label4.config(font=('arial',13,'bold'))
label4.place(x=590,y=160)

canvas=Canvas(root,width=350,height=350,bg="white")
canvas.place(x=8,y=22)
img = ImageTk.PhotoImage(Image.open("fruits.jpg").resize((250, 250), Image.ANTIALIAS))
canvas.create_image((53,60),image=img,anchor=NW)

labe = Label(canvas,text="Fruit Image",bg="white",fg="black")
labe.config(font=('arial',13,'bold'))
labe.place(x=140,y=10)
divider=Label(root,bg="red",height=100,width=0)
divider.place(x=365,y=0)

def architectureModel():
    messagebox.showinfo('[INFO]',"INTERNET REQUIRED!!\nLoad my_fruits360_model_131classes.h5 file")
    # opening netron for model visualization using python need net
    webbrowser.open('https://lutzroeder.github.io/netron/')

label5 = Label(root,text="Click to browse an image:",bg="black",fg="white")
label5.config(font=('arial',13,'bold'))
label5.place(x=390,y=240)    
selectButton=Button(root,text="Browse an Image",bg="red",fg="white",activebackground="green",width=20,command=openFile)
selectButton.config(font=('arial',10,'bold'))
selectButton.place(x=600,y=240)
architecture_button=Button(root,text="View Model Architecture ",bg="red",fg="white",activebackground="green",width=45,command=architectureModel)
architecture_button.config(font=('arial',10,'bold'))
architecture_button.place(x=400,y=300)


    
def aboutUs():
    messagebox.showinfo("[INFO]","CHILUKURI VINAY KUMAR - 11716840")

def destroy():
    root.destroy()
    print("command: exit")
    
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="INFO", menu=filemenu)
filemenu.add_command(label="About us", command=aboutUs)

destroy_button=Button(root,text="Exit",bg="red",fg="white",activebackground="green",width=17,command=destroy)
destroy_button.config(font=('times',10,'bold'))
destroy_button.place(x=640,y=350)
root.mainloop()
