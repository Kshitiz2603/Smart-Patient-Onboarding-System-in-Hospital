#importing necessary libraries/modules
from tkinter import *
import sqlite3
import os
import csv 
from csv import writer
import tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk
import numpy

#importing necessary libraries/modules
root = Tk()
app_width = 500 #width of screen
app_height = 500 #heigth of the screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') #aligning the window at the center of the screen
root.title("Details")


#Variables Declaration
Fullname=StringVar()
Age=StringVar()
Phonenumber=StringVar()
City=StringVar()
Email=StringVar()

#finish button function
def finish():
    root.destroy()

#submit_and_next button function
def submit_and_next():
    name1=Fullname.get()  #extracting entered name by user
    age=Age.get()  #extracting entered age by user
    phone=Phonenumber.get()  #extracting entered phone number by user
    city=City.get()  #extracting entered city by user
    email = Email.get()  #extracting entered email by user
    fill = [name1,age,phone,city,email]  #list of all the entered details
        # list of column names

    #filling all the details into PersonDetails.csv file
    with open('PersonDetails.csv','a+',newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow([name1,age,phone,city,email])

    write_obj.close()

    #filling all the details into persons.csv file
    data = [name1, age, phone, city,email]
    header = ['name', 'age', 'phone no', 'city','email']
    with open('person.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
    f.close()
    os.system('python3 capture1.py')  #captuing image of the new user
    os.system('python3 move.py') #moving that image to database
    os.system('python3 otp_generate.py') #otp generating script


def value():
    name = Fullname.get()
    print(name)
   
#Title of the screen            
label_0 = Label(root, text="Please Fill Your Details",width=20,font=("bold", 25))
label_0.place(x=70,y=53)

#Full name entry row
label_1 = Label(root, text="Full Name",width=20,font=("bold", 20))
label_1.place(x=25,y=130)
entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

#Age entry row
label_2 = Label(root, text="Age",width=20,font=("bold", 20))
label_2.place(x=25,y=180)
entry_2 = Entry(root,textvar=Age)
entry_2.place(x=240,y=180)

#Phone Number entry row
label_3 = Label(root, text="Phone Number",width=20,font=("bold", 20))
label_3.place(x=25,y=230)
entry_3 = Entry(root,textvar=Phonenumber)
entry_3.place(x=240,y=230)

#Address entry row
label_4 = Label(root, text="Address",width=20,font=("bold", 20))
label_4.place(x=25,y=280)
entry_4 = Entry(root,textvar=City)
entry_4.place(x=240,y=280)

#E-mail entry row
label_5 = Label(root, text="E-Mail",width=20,font=("bold", 20))
label_5.place(x=25,y=330)
entry_5 = Entry(root,textvar=Email)
entry_5.place(x=240,y=330)

#Continue button
Button(root, text='Continue',width=15,bg='green',fg='black',command=submit_and_next).place(x=280,y=440)

#Cancel button
Button(root, text='Cancel',width=15,bg='red',fg='black',command=finish).place(x=60,y=440)

root.mainloop()