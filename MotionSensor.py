#A small module to make a motionsensor using an old mobile phone for camera input and a raspberry pi to process the image


# importing OpenCV(cv2) module for opening images
import cv2 
# importing pygame module for playing music
import pygame
#To log files when motion occurs
import logging

class MotionSensor:
	def startSensor():
		#reads frames in grayscale
		try:
			previousFrame = cv2.imread('http://192.168.137.201:8080/shot.jpg',0) #got to change to search for camera
		except:
			print("Camera not found")
			exit()
		#calculate size of image and normalize it for future calculation
		height, width, channels = previousFrame.shape
		size = height * width
		previousFrameNor = normalize(previousFrame) #can be moved into the while loop, but since a raspberry pi is slow, the normalizion takes longer then copying it
	
		while True:
			try:
				curFrame = cv2.imread('http://192.168.137.201:8080/shot.jpg',0)
			except:
				print("Camera went offline")
				exit()
			curFrameNor = normalize(curFrame)
			diff = curFrameNor - previousFrameNor
			diff_per = ( 1.0 * diff ) / size
			if diff_per >= 0.01 : #more then 1% difference, the quality of images i can process at a time is really small at the moment (640 x 480 pixels)
				addToLog(curFrame)
			
			#Setting new previous Frame info
			previousFrame = curFrame
			previousFrameNor = curFrameNor
	
	def addToLog(curFrame):
		#setting up a log every time an chnage is found
		logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
		logging.info("There has been some movement")
		cv2.imwrite(%(asctime)s+".jpg",img)
		
		#play a spooky sound when someone enters
		pygame.mixer.init()
		pygame.mixer.music.load("spooky.mp3")
		pygame.mixer.music.set_volume(1.0)
		pygame.mixer.music.play(loops=0, start=0.0) #play music only once

		while pygame.mixer.music.get_busy() == True:
			pass
	

MotionSensorObj = MotionSensor()
MotionSensorObj.startSensor()
		
		
			
			
  
