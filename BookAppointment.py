#importing necessary libraries/modules
from tkinter import *
import cv2
import smtplib, ssl
import tkcalendar
from tkcalendar import Calendar, DateEntry
import csv

#tkinter window screen
root = Tk()
app_width = 450		#width of screen
app_height = 400    #heigth of screen

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') #aligning the window at the center of the screen
root.title("Appointment Booking")

c=StringVar()
date = StringVar()
t=StringVar()

data = []

file = open("person.csv")
csvreader = csv.reader(file)
header = next(csvreader)

for row in csvreader:
    data.append(row)
emailid = data[0][4]
name = data[0][0]

def submit_and_next():
	doc = c.get()
	time = t.get()
	dat = cal.get()

	message_c = "Mr/Mrs " + name + ", your appointment has been booked with Dr. " + doc + " for date " + dat + " at " + time + " ."
	message = message_c
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "kshitiz2603@gmail.com"  # Enter sender's address
	receiver_email = "kshitizchoudhary2000@gmail.com"  # Enter receiver address
	password = "hzplwmaypwckpbhx" #third party generated password 
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)


#Title of the screen
label_0 = Label(root, text="Book Appointment",width=20,font=("bold", 30))
label_0.place(x=50,y=35)

#Date entry row
label_1 = Label(root, text="Date",width=20,font=("bold", 18))
label_1.place(x=7,y=120)

cal = DateEntry(root, width= 12, background= "white", foreground= "black",bd=2)
cal.place(x=250,y=120)

#Time entry row
label_2 = Label(root, text="Time",width=20,font=("bold", 18))
label_2.place(x=7,y=190)

list0 = ['12:00 PM','1:00 PM','2:00 PM','3:00 PM','4:00 PM'];

droplist=OptionMenu(root,t, *list0)
droplist.config(width=12)
t.set('select your time') 
droplist.place(x=250,y=190)

#Doctor selection entry row
label_3 = Label(root, text="Preferred Doctor",width=20,font=("bold", 18))
label_3.place(x=7,y=260)

list1 = ['Cardiologists','Allergist', 'Dermatologists','Endocrinologists'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=12)
c.set('select your doctor') 
droplist.place(x=250,y=260)

#Submit Button
Button(root, text='Submit',width=15,bg='green',fg='black',command=submit_and_next).place(x=250,y=340)

root.mainloop()