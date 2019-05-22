import numpy as np
import cv2
import time

def  play(nama):
	for i in nama:
		cap = cv2.VideoCapture('video/%s.mp4'%i)
		while(cap.isOpened()):
		    ret, frame = cap.read()
		    if ret == True:
		        cv2.imshow('frame',frame)
		        # & 0xFF is required for a 64-bit system
		        if cv2.waitKey(1) & 0xFF == ord('q'):
		            break
		        time.sleep(.04)
		    else:
		        break
		cap.release()
	cv2.destroyAllWindows()
