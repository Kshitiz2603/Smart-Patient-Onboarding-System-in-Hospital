import os
import math
import random
import smtplib
from tkinter import *
import cv2
import csv

root = Tk()
root.geometry('450x400')
root.title("Details")

email1=StringVar()

def submit():
    csv_file = csv.reader(open('/Users/kshitiz2000/desktop/pythonpro/PersonDetails.csv','r'))
    for row in csv_file:
        if email1 in row[4]:
            os.system('python3 otp_generate.py')
        else :
            os.system('python3 tk_details.py')


def cancel():
    root.destroy()
    os.system('python3 confirmation.py')



label_0 = Label(root, text="Verification",width=20,font=("bold", 30))
label_0.place(x=40,y=100)

label_1 = Label(root, text="Enter your email:",width=20,font=("bold", 17))
label_1.place(x=10,y=200)

entry_1 = Entry(root,textvar=email1)
entry_1.place(x=200,y=200)

submit_button = Button(root, text='Continue',width=10,bg='green',fg='black',command=submit)
submit_button.place(x=80,y=300)
exit_button = Button(root, text='cancel',width=10,bg='green',fg='black',command=cancel)
exit_button.place(x=260,y=300)

root.mainloop()
