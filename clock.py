from tkinter import *
import time
import os

t=0
flag = 0

root=Tk()
app_width = 250
app_height = 150

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

def back():
	os.system('python3 services.py')

def emo():
	global flag
	file1 = open("finalemotion.txt","r+") 
	str1 = file1.read()

	l1.config(text=str1)
	Button(root, text='<- Back',width=5,bg='green',fg='black',command=back).place(x=150,y=95)

	
def set_timer():
	global t
	t =t +15
	

def countdown():
	global t
	if t>0:
		l1.config(text = t)
		t = t-1
		l1.after(1000,countdown)
	elif t==0:
		l1.config(text = "Processing....")
		l1.after(5000,emo)



l1 = Label(root,font="times 20")
l1.place(x=75,y=40)

set_timer()
countdown()


root.mainloop()
