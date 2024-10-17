from flask import Flask, send_file
import os
import random

app = Flask(__name__)

def random_image():

    img_dir = "./static/dishes"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    return img_path
def lol():
    img_dir = "./static/dishes"
    img_list = os.listdir(img_dir)
    return img_list
    


@app.route('/')
def myapp():

    image = random_image()
    return send_file(image, mimetype='image/jpg')
@app.route('/list')
def mpp():
    a=lol()

    return a




app.run(debug=True)