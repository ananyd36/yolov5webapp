from flask import Flask, render_template, Response,  request, session, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from detect import *
import os
import torch

__author__ = 'Anany'
__source__ = ''

app = Flask(__name__)
# UPLOAD_FOLDER = "C:\Users\Arpit Sharma\Desktop\Friendship goals\content\yolov5\static\uploads"
DETECTION_FOLDER = r'./static/detections'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
#app.config['DETECTION_FOLDER'] = DETECTION_FOLDER


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    print("I about")
    return render_template("about.html")

@app.route("/uploaded",methods = ["GET","POST"])
def uploaded():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        print(filename)
        file_path = os.path.join(r"./static/uploads", filename)
        print(file_path)
        f.save(file_path)
        with torch.no_grad():
            detect_image(file_path, DETECTION_FOLDER)
        return render_template("uploaded.html",display_detection = filename, fname = filename)

if __name__ == "__main__":
    app.run(debug = True)
