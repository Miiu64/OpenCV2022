import cv2 as cv

capture = cv.VideoCapture(1)

#While loop to show frame by frame
while True:
    #reads frame by frame
    isTrue, frame = capture.read()
    #shows frame by frame
    cv.imshow('Video', frame)

    #If waitKey delay is 20 miliseconds and d key is pressed, video ends
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#realeases the path from capture
capture.release()
#destroys all the windows
cv.destroyAllWindows()
cv.waitKey(0)