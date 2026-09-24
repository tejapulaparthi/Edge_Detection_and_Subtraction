import edge_detection as ed
import flask
from flask_cors import CORS
import cv2
import numpy as np
app = flask.Flask(__name__)
CORS(app)
@app.route("/detect", methods=["POST"])
def detect():
    file = flask.request.files["image"]
    file_bytes = file.read()
    image_array = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    edges = ed.detect_edges(image)
    success, encoded_image = cv2.imencode('.png', edges)
    return flask.Response(
        encoded_image.tobytes(),
        mimetype='image/png'
    )
@app.route("/subtract", methods=["POST"])
def subtraction():
    file1 = flask.request.files["image1"]
    file2 = flask.request.files["image2"]
    file_bytes1 = file1.read()
    file_bytes2 = file2.read()
    image_array1 = np.frombuffer(file_bytes1, np.uint8)
    image_array2 = np.frombuffer(file_bytes2, np.uint8)
    image1 = cv2.imdecode(image_array1, cv2.IMREAD_COLOR)
    image2 = cv2.imdecode(image_array2, cv2.IMREAD_COLOR)
    result = ed.subtraction(image1, image2)
    success, encoded_image = cv2.imencode('.png', result)
    return flask.Response(
        encoded_image.tobytes(),
        mimetype='image/png'
    )
if __name__ == "__main__":
    app.run()