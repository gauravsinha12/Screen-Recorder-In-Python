import cv2
import pyautogui
import numpy as np
codec = cv2.VideoWriter_fourcc(*"MP4V")
out = cv2.VideoWriter("Recedf.mp4", codec , 25, (1366, 768))
cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)
while True:
    img = pyautogui.screenshot() #capturing screenshot
    frame = np.array(img) #converting the image into numpy array representation
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image
    out.write(frame) #writing the RBG image to file
    #display screen/frame being recorded
    if cv2.waitKey(1) == ord('q'): 
        break

out.release() 
cv2.destroyAllWindows()