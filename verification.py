#importing necessary libraries/modules
import cv2
import face_recognition
import numpy as np
import os
from tkinter import *
import csv
import site


#tkinter window screen
root = Tk()
root.geometry('450x400') #height x width of the tkinter screen
root.title("Details") #Title of the screen
root.eval('tk::PlaceWindow . center') 

#Image Database
path = 'Image'  #defining path to Image folder
images = [] 
classNames = []
myList = os.listdir(path)  #List of image name in the myList
print(myList)

#For loop to extract person's name saved for respective people
for cl in myList:
	curImg = cv2.imread(f'{path}/{cl}',1)
	images.append(curImg)
	classNames.append(os.path.splitext(cl)[0])
print(classNames)

#if user is matched to database
def matched(name):
	cap.release()
	cv2.destroyAllWindows()
	csv_file = csv.reader(open('/Users/kshitiz2000/desktop/pythonpro/PersonDetails.csv','r')) #Extracting information of person from the csv file

	for row in csv_file:
		if name in row[0]:  #searching for the matched person's name in the csv file
			print(row)
			name1=row[0] 	#name saved in name1 variable
			age=row[1] 	    #age saved in age variable
			phone=row[2] 	#phone number saved in phone variable
			city=row[3] 	#address saved in city variable
			email=row[4] 	#email saved in email variable

			#writing all the user's information on another csv file
			header = ['name', 'age', 'phone no', 'address','email']
			data = [name1, age, phone, city,email]
			with open('person.csv', 'w', encoding='UTF8') as f:
			    writer = csv.writer(f)
			    writer.writerow(header)
			    writer.writerow(data)

			#after writing the data, script is followed by confirmation.py file
			os.system('python3 confirmation.py')
			quit()


#if the user is not matched to the database, register the user as new user
def notmatched():
	cap.release()
	cv2.destroyAllWindows()

	#Details script will run
	os.system('python3 tk_details.py')
	quit()

#function of encoding of every image 
def findEncodings(images):
	encodeList = []  #creating empty list of encodings

	#every image encodings is appended to the encoding list
	for img in images:
		os.system('cd Image')
		os.system('rm -f .DS_Store')
		os.system('cd ../')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		encode = face_recognition.face_encodings(img)[0]
		encodeList.append(encode)
	return encodeList

os.system('cd Image')
os.system('rm -f .DS_Store')
os.system('cd ../')

#function to encode all the image in the database
encodeListKnown = findEncodings(images)
print("Encoding Complete")

#camera starts capturing
cap = cv2.VideoCapture(0)

#comparing the captured image's face encoding to all the images in the database
while True:
	success, img = cap.read()
	imgS = cv2.resize(img,(0,0), None, 0.25,0.25)
	imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
	facesCurFrame =face_recognition.face_locations(imgS)
	encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

	for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
		matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
		faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
		
		macthIndex = np.argmin(faceDis)

		if matches[macthIndex]:
			name = classNames[macthIndex]
			print(name)
			y1, x2, y2, x1 = faceLoc
			y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
			cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,255,0),2)
			cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
			cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
			matched(name)
			cap.release()
			break
			
		else:
			notmatched()
			cap.release()
			break


				

	cv2.imshow('Webcam',img)
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	
root.mainloop()





