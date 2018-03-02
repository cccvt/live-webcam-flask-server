# Flask server to feed images from OpenCV

This code can run on Raspberry Pi as a security camera running open-cv. Also with the use of ngrok you can feed the live stream of the localhost to the Internet.

## Setup

This project uses a USB WebCam to stream video. Before running the code.

## Installing Dependencies

This project uses openCV to detect objects in the video feed. You can install openCV by using the following [tutorial](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/). I used the Python 3.5 vertion. Or you can use the ./install-opencv.sh to install opencv in auto mode in Ubuntu 16.04.


``` for install opencv
chmod +x install-opencv.sh
./install-opencv.sh
```

## Running the Program

Run the program

```Open the terminal and run
sudo python3 main.py
```

Note: To view the live stream on a different network than your Raspberry Pi, you can use [ngrok](https://ngrok.com/) to expose a local tunnel. Once downloaded, run ngrok with `./ngrok http 5000` and visit one of the generated links in your browser.

