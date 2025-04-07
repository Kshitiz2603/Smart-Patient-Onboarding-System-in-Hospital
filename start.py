#importing necessary libraries/modules
from tkinter import *
from tkinter import ttk
import  tkinter.messagebox
import os
import tkinter.font as font


#tkinter window screen
root = Tk()
app_width = 250  #width of screen
app_height = 250 #heigth of screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.title('Start')

#start button functions
def start():
    os.system('python3 verification.py') #clicking on start button sends user to verification.py file

#displaying of the text
label_0 = Label(root, text="Press the button below to start the process",wraplength=150, justify = CENTER,width=20,font=("bold", 13))
label_0.place(x=40,y=70)

#button widget on screen
Button(root, wraplength=80,text="Start",width=5,height= 2,justify = CENTER, bg='white',fg='black',command=lambda: [start(), quit()]).place(x=85,y=120)


root.mainloop()