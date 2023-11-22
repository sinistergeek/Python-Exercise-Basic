from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def main():
    return '<a href="/time">time</a>'

@app.route("/route")
def echo():
    return str(time.time())
