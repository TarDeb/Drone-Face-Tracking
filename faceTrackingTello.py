from utils import *
import cv2

w, h = 360, 240
pid = [0.4, 0.4, 0]
pError = 0
startCounter = 0  

myDrone = initializeTello()

while True:
    ## Flight
    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    ## Step 1
    img = telloGetFrame(myDrone, w, h)
    ## Step 2
    img, info = findFace(img)
    ## Step 3
    pError = trackFace(myDrone, info, w, pid, pError)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break
