import cv2
import sys
from flask import Flask, render_template, Response
from camera import VideoCamera
import time

video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically

# App Globals (do not edit)
app = Flask(__name__)
last_epoch = 0


@app.route('/')
def index():
	return render_template('index.html')

def gen(camera):
	local_state = True
	while True:
		frame, framebytes, mask, maskbytes = camera.get_frame()

		#cv2.imshow('FRAME', mask)

		# check to see if a key was pressed
		key = cv2.waitKey(1) & 0xFF
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

		if key == ord("s"):
			local_state = True
		if key == ord('t'):
			local_state = False

		#print(framebytes)
		if local_state == True:
			yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' +  framebytes + b'\r\n\r\n')
		else:
			yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' +  maskbytes  + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False, threaded=False)
