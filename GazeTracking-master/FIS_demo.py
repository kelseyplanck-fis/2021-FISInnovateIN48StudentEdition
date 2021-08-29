"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import time
import webbrowser
import pyttsx3

engine = pyttsx3.init()

from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

start=time.time()

opened = False

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    # if gaze.is_blinking():
    #     text = "Blinking"
    #     engine.say(text)
    #     engine.runAndWait()
    if gaze.is_right():
        text = "You are looking right"
        if ((time.time() >= start+8) and not opened):
            opened = True
            engine.say(text)
            engine.runAndWait()
            webbrowser.open('https://www.fisglobal.com/en/')
    elif gaze.is_left():
        text = "You are looking left"
        if ((time.time() >= start+8) and not opened):
            opened = True
            engine.say(text)
            engine.runAndWait()
            webbrowser.open('https://www.usbank.com/home-loans/mortgage.html')
    elif gaze.is_center():
        text = "You are looking at the center"
        if ((time.time() >= start+8) and not opened):
            engine.say(text)
            engine.runAndWait()

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()

    start = round(start)
    
    cv2.putText(frame, str(start), (90, 180), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.9, (147, 58, 31), 2)
    
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (147, 58, 31), 1)

    if opened:
        start = time.time()
        opened = False

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
