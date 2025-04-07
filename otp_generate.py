#importing necessary libraries/modules
import os
import math
import random
import smtplib
from tkinter import *
import cv2
import csv

#reading the csv file where the user information is saved
data = []
file = open("person.csv")
csvreader = csv.reader(file)
header = next(csvreader)

for row in csvreader:
    data.append(row)

#email id is extracted from csv file
emailid = data[0][4]

#otp generation and sending to receiver's address
digits="0123456789"
OTP=""
for i in range(6): #random otp generation
    OTP+=digits[math.floor(random.random()*10)]
    
otp = OTP + " is your OTP"
msg= otp

#connecting to smtp server for sending mail
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("kshitiz2603@gmail.com", "hzplwmaypwckpbhx")
s.sendmail('&&&&&&&&&&&',emailid,msg)
file = open('Otp_file.txt', 'w')  #random otp number saved in otp_file.txt
file.write(OTP)
file.close()

os.system('python3 otp_verified.py')