#importing necessary libraries/modules
import os
import math
import random
import smtplib
from tkinter import *
import cv2
import csv

#importing necessary libraries/modules
root = Tk()
root.title("OTP_Verification")
app_width = 450  #width of screen
app_height = 400  #heigth of screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')  #aligning the window at the center of the screen

#otp variable 
otp1=StringVar()

#submit button functions
def submit():
    otpgot = otp1.get()  #user entered otp extracted
    file1 = open("Otp_file.txt") 
    value = file1.read()  #otp saved in file extracted
    if value == otpgot :  #comparison between entered otp and original otp
        print("verified")  #if successful print verified and move to service.py 
        os.system('python3 services.py')
    root.destroy()
    file1.close() 

#resend button functions
def resend():
    os.system('python3 otp_generate.py')  #if otp not received again new otp_generate.py script will run

#cancel button functions
def cancel():
    root.destroy()
    

#Title of the screen
label_0 = Label(root, text="OTP Verification",width=20,font=("bold", 30))
label_0.place(x=40,y=100)

#Otp entry row
label_1 = Label(root, text="Enter your otp:",width=20,font=("bold", 17))
label_1.place(x=10,y=200)

entry_1 = Entry(root,textvar=otp1)
entry_1.place(x=200,y=200)

#submit button
submit_button = Button(root, text='Confirm',width=10,bg='green',fg='black',command=submit)
submit_button.place(x=80,y=300)

#resend button
resend_button = Button(root, text='Resend',width=10,bg='green',fg='black',command=resend)
resend_button.place(x=280,y=300)


root.mainloop()
