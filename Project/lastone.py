from gpiozero import LED
from time import sleep
import cv2
import numpy as np
import random
import os




# Cam Function
def camera(lane):
    global count
    count=0
    global img_counter
    
    if lane==0:                                 
        cam = cv2.VideoCapture(lane)           #choose camera
    elif lane==2:
        cam = cv2.VideoCapture(lane)
    elif lane==1:
        cam = cv2.VideoCapture("/home/pi/Desktop/Project/video1.mp4")
    else:
        cam = cv2.VideoCapture("/home/pi/Desktop/Project/video4.mp4")
        
    
    

    while True:
        ret, image = cam.read()
        if (ret == False):
            print("failed to grab frame")
            break

        folder="fold"+str(lane)
        imgpth=os.path.join(folder, str(img_counter) + '.jpg')
        cv2.imwrite(imgpth, image)             
        
        img_name = "frame.png".format(img_counter)
        img_counter+=1
        
        break
        
    image = cv2.imread(imgpth)
    
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    car_cascade = cv2.CascadeClassifier('cars.xml')
    cars = car_cascade.detectMultiScale(grey, 1.1, 1)
    
    for (x, y, w, h) in cars:
        
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        
   
 
   

    cam.release()
    cv2.destroyAllWindows()
    return count



def timecalc(count):
    i=count
    low=10
    medium=20
    high=30
    print("no of vehicles ="+ str(count))
 
    delay=0
 
    if i < low:
        if i<1:
            delay=2
            print('green light delay = 2 sec')
        elif i<4:
            delay=i*2
            print('green light delay = '+str(delay)+' sec')
        elif i<7:
            delay=7.5
            print('green light delay = '+str(delay)+' sec')
        else:
            delay=10.5
            print('green light delay = '+str(delay)+' sec')
    elif i < medium:
        if i<medium/2:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
        else:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
    elif i < high:
        if i<high/2:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
        else:
            delay=60
            print('green light delay = '+str(delay)+' sec')
    return(delay)











# Lane Functions
def Lane0(count):
    
    duration= timecalc(count)
    
  
    red0.off()
    red1.off()
    red2.off()
    sleep(0.5)
    
    
    red0.off()
    amber3.off()
    red3.on()
    red1.on()
    red2.on()
    green0.on()
    sleep(duration)

    green0.off()
    amber0.on()
    sleep(3)
    
    count=camera(1)
    
    amber0.off()
    red0.on()
    
    
    

    

def Lane1(count):


    duration= timecalc(count)
    
    
    red1.off()
    red2.off()
    red3.off()
    sleep(0.5)
    

    
    red1.off()
    
    amber0.off()
    red0.on()
    green1.on()
    red2.on()
    red3.on()
    sleep(duration)

    green1.off()
    amber1.on()
    sleep(3)
    count=camera(2)
    
    

    
   
    

def Lane2(count):
    
    duration= timecalc(count)
    
    red2.off()
    red0.off()
    red3.off()
    sleep(0.5)
    

    
    red2.off()
    amber1.off()
    red1.on()
    green2.on()
    red0.on()
    red3.on()
    sleep(duration)

    green2.off()
    amber2.on()
    sleep(3)
    count=camera(3)
    
    
    
    

  

def Lane3(count):
    duration= timecalc(count)
    
    
    red3.off()
    red0.off()
    red1.off()
    sleep(0.5)
    

    amber2.off()
    red3.off()
    red2.on()
    green3.on()
    red0.on()
    red1.on()
    sleep(duration)

    green3.off()
    amber3.on()
    sleep(3)
    
    count=camera(0)
    

    





    
red0 = LED(16)
red1 = LED(26)                          
red2 = LED(10)               
red3 = LED(6)               

amber0 = LED(19)
amber1 = LED(20)            
amber2 = LED(12)             
amber3 = LED(5)              

green0 = LED(13)
green1 = LED(21)            
green2 = LED(9)             
green3 = LED(17)             


img_counter=0
camera(0)
while True:
    
    Lane0(count)
    Lane1(count)
    Lane2(count)
    Lane3(count)
