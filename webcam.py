# import the necessary packages
from threading import Thread
import cv2# import the necessary packages
import time
import datetime
import imutils
class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240),framerate=32):
        self.stream = WebcamVideoStream(src=src)

    def start(self):
        # start the threaded video stream
        return self.stream.start()

    def update(self):
        # grab the next frame from the stream
        self.stream.update()

    def read(self):
        # return the current frame
        return self.stream.read()

    def stop(self):
        # stop the thread and release any resources
        self.stream.stop()



class WebcamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return
            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True



if __name__ == '__main__':
    # initialize the video streams and allow them to warmup
    print("[INFO] starting cameras...")
    webcam = VideoStream(src=0).start()
    time.sleep(2.0)
    total = 0

    # loop over frames from the video streams
    while True:
        # initialize the list of frames that have been processed
     
        # loop over the frames and their respective motion detectors
        # read the next frame from the video stream and resize
        # it to have a maximum width of 400 pixels
        frame = webcam.read()
        frame = imutils.resize(frame, width=400)
 
        # convert the frame to grayscale, blur it slightly, update
        # the motion detector
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        # we should allow the motion detector to "run" for a bit
        # and accumulate a set of frames to form a nice average
  
        # increment the total number of frames read and grab the 
        # current timestamp
        timestamp = datetime.datetime.now()
        ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        # loop over the frames a second time
        # draw the timestamp on the frame and display it
        cv2.putText(frame, ts, (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        cv2.imshow('DEMO', frame)
     
        # check to see if a key was pressed
        key = cv2.waitKey(1) & 0xFF
     
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
         
    # do a bit of cleanup
    print("[INFO] cleaning up...")
    cv2.destroyAllWindows()
    webcam.stop()
