#importing necessary libraries/modules
import os
import math
import random
import smtplib
from tkinter import *
import cv2
import csv

#tkinter window screen
root = Tk()
app_width = 450  #width of screen
app_height = 400 #heigth of screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')  #aligning the window at the center of the screen
root.title("Details")

#Variable declaration for Label and entry widgets
email1=StringVar()

#submit button functions
def submit():
    csv_file = csv.reader(open('/Users/kshitiz2000/desktop/pythonpro/PersonDetails.csv','r'))
    for row in csv_file:
        if email1.get() in row[4]:  #entered email id if matches to database
            os.system('python3 otp_generate.py')  #otp will be generated
        else :
            os.system('python3 tk_details.py')  #else user will be registered as a new user

#cancel button functions
def cancel():
    root.destroy()
    quit()

#Title of the screen
label_0 = Label(root, text="Verification",width=20,font=("bold", 30))
label_0.place(x=40,y=100)

#Email entry row
label_1 = Label(root, text="Enter your email:",width=20,font=("bold", 17))
label_1.place(x=10,y=200)

entry_1 = Entry(root,textvar=email1)
entry_1.place(x=200,y=200)

#Submit Button
submit_button = Button(root, text='Continue',width=10,bg='green',fg='black',command=submit)
submit_button.place(x=80,y=300)

#Cancel Button
exit_button = Button(root, text='Cancel',width=10,bg='green',fg='black',command=cancel)
exit_button.place(x=260,y=300)

root.mainloop()
