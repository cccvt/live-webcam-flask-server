# Flask server with optional ON CLICK  feed images from OpenCV

This code can also run on Raspberry Pi as a security camera running open-cv. Also with the use of ngrok you can feed the live stream of the localhost to the Internet.

## Setup

This project uses a USB WebCam to stream video. Before running the code.

## Installing Dependencies

This project uses openCV  to feed the video. You can install openCV on raspberry pi by using the following [tutorial](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/). I used the Python 3.5. Or you can use the ./install-opencv.sh to install opencv in auto mode in Ubuntu 16.04.


``` for install opencv
chmod +x install-opencv.sh
./install-opencv.sh
```

## Running the Program

Run the program



```Open the terminal and run
python3 camera.py
python3 flask_class.py 
```
to run server, go to /Monitoring and click on ShowVideo to start streaming from camera.py


To view the live stream on a different network than your Raspberry Pi or PC, you can use [ngrok](https://ngrok.com/) to expose a local tunnel. To run ngrok with `./ngrok http 5000` and visit one of the generated links in your browser.

Know bugs. Does not work in Firefox 
	   Must do click on TurnOFf video before close the webpage
