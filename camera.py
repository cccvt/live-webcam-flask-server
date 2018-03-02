import cv2
#from imutils.video.pivideostream import PiVideoStream
#from webcam import VideoStream
import imutils
import time
import numpy as np

class VideoCamera(object):
	def __init__(self, flip = False, src = 0):

		self.stream = cv2.VideoCapture(src)
		mask = np.zeros((320,320))
		self.mask = mask.astype(np.uint8)
		time.sleep(2.0)

	def get_frame(self):
		#frame = self.flip_if_needed(self.vs.read())
		(grabbed, frame) = self.stream.read()
		ret, jpeg = cv2.imencode('.jpg', frame)

		# BLANK
		_, jpegDemo = cv2.imencode('.jpeg', self.mask)

		return frame, jpeg.tobytes(), self.mask, jpegDemo.tobytes()


