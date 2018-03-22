from flask import Flask, request ,render_template, Response
import numpy as np
import cv2


class FeedVideo():
    def __init__(self):
        # Create placeholder for imagen
        self.imagen     = None
        # Create configs for show and turnoff the feeds
        self.configs    = np.array([False,False])
        self.saveConfigsToDisk()
    # Some properties
    @property
    def imagen(self):
        return self.__imagen
    @property
    def configs(self):
        return self.__configs

    # Setters
    @configs.setter
    def configs(self, newConfigs):
        self.__configs = newConfigs
    @imagen.setter
    def imagen(self, newFrame):
        self.__imagen = newFrame


    def saveConfigsToDisk(self, path='./'):
        np.save('{}'.format(path) + 'configs.npy', self.configs)

    # Getters
    def __call__(self):
        while True:
            ret, jpeg   =   cv2.imencode('.jpeg', self.imagen)
            framebytes  =   jpeg.tobytes()
            yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' +  framebytes + b'\r\n\r\n')

feedVideo = FeedVideo()

# Frame to show

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/installation/')
def installation():
    global feedVideo
    return render_template('controlboard.html', show = feedVideo.configs[0])

@app.route('/monitoring/')
def monitoring():
    global feedVideo
    return render_template('monitoring.html', show = feedVideo.configs[0])

@app.route('/video_feed')
def video_feed():
    return Response(feedVideo(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_images', methods=['GET', 'POST'])
def get_images():
    global feedVideo
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    feedVideo.imagen  = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return Response('Happy to recive your images...', 201)


@app.route('/my-link/')
def my_link():
    global feedVideo
    if feedVideo.configs[0] == True:
        feedVideo.configs[0] = False
        feedVideo.saveConfigsToDisk()
    elif feedVideo.configs[0] == False:
        feedVideo.configs[0] = True
        feedVideo.saveConfigsToDisk()
    else:
        pass
    return (''), 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
