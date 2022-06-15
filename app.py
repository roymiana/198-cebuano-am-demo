from flask import Flask, render_template, jsonify
import sys
from utils.inference import start_live

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/start_asr")
def start():
    start_live()
    return jsonify("speechrecognition start success!")


@app.route("/get_audio")
def get_audio():
    with open('transcript.txt', 'r') as f:
        transcript = f.read()
    return jsonify(transcript)

if __name__ == '__main__':
   app.run()