#importing necessary libraries/modules
from tkinter import *
import cv2
import csv
import os

#importing necessary libraries/modules
root = Tk()
app_width = 500 	#width of screen
app_height = 500 	#heigth of screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')  #aligning the window at the center of the screen
root.title("Confirmation")

#Notme button functions
def Notme():
	root.destroy()
	os.system('python3 otp.py')

#confirm button functions
def confirm():
	root.destroy()
	os.system('python3 services.py')

data = []

#From the csv file user's data will be read and displayed on the tkinter window
#Reading csv file
file = open("person.csv")
csvreader = csv.reader(file)
header = next(csvreader)

for row in csvreader:
    data.append(row)

#Title of the screen
label_0 = Label(root, text="Please Confirm Your Details",width=20,font=("bold", 30))
label_0.place(x=60,y=63)

#Displaying Full Name 
label_1 = Label(root, text="Full Name",width=20,font=("bold", 20))
label_1.place(x=25,y=130)
entry_1 = Label(root,text = data[0][0])
entry_1.place(x=240,y=130)

#Displaying Age
label_2 = Label(root, text="Age",width=20,font=("bold", 20))
label_2.place(x=25,y=180)
entry_2 = Label(root,text=data[0][1])
entry_2.place(x=240,y=180)

#Displaying Phone Number
label_3 = Label(root, text="Phone Number",width=20,font=("bold", 20))
label_3.place(x=25,y=230)
entry_3 = Label(root,text = data[0][2])
entry_3.place(x=240,y=230)

#Displaying Address
label_4 = Label(root, text="Address",width=20,font=("bold", 20))
label_4.place(x=25,y=280)
entry_4 = Label(root,text = data[0][3])
entry_4.place(x=240,y=280)

#Displaying Email
label_5 = Label(root, text="E-Mail",width=20,font=("bold", 20))
label_5.place(x=25,y=330)
entry_5 = Label(root,text=data[0][4])
entry_5.place(x=240,y=330)

Button(root, text="Confirm",width=7,bg='green',fg='black',command=confirm).place(x=95,y=420)  #Confirm Button
Button(root, text="Not Me",width=7,bg='red',fg='black',command=Notme).place(x=270,y=420)     #Not Me Button

file.close()
# Python program to create
# yes/no message bo

root.mainloop()