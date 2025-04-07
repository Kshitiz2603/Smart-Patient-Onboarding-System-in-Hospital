#importing necessary libraries/modules
from tkinter import *
import cv2
import csv

#tkinter window screen
root = Tk()
root.geometry('450x400') #Width x Height of the screen
root.title("Details")

#Heading on the screen
label_0 = Label(root, text="Lab Test",width=20,font=("bold", 30))
label_0.place(x=40,y=100)

root.mainloop()