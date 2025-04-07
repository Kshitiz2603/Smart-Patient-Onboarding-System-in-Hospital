#importing necessary libraries/modules
from tkinter import *
import cv2
import csv
import os

#tkinter window screen
root = Tk()
app_width = 450		#width of screen
app_height = 400 	#heigth of screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')	#aligning the window at the center of the screen
root.title("Services")

#BookAppointment button functions
def Book_Appointment():
	root.destroy()
	os.system('python3 BookAppointment.py')

#LabTest button functions
def LabTest():
	root.destroy()
	os.system('python3 labtest.py')

#EmotionalAnalysis button functions
def Emotional_Analysis():
	root.destroy()
	os.system('python3 Emotional_Analysis.py')

#Title of the screen
label_0 = Label(root, text="Please Choose One",width=20,font=("bold", 30))
label_0.place(x=40,y=100) #Title's x and y placement

Button(root, text="Book Appointment",width=10,bg='white',fg='black',command=Book_Appointment).place(x=30,y=250) #Book Appointment Button
Button(root, text="Lab Test Reports",width=10,bg='white',fg='black',command=LabTest).place(x=165,y=250) #Lab Test Report Button
Button(root, text="Emotional Analysis",width=10,bg='white',fg='black',command=Emotional_Analysis).place(x=300,y=250) #Emotional Analysis Button

root.mainloop()