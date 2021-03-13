#!/usr/bin/python

from flask import Flask, jsonify
import wsgiserver
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 23

app = Flask(__name__)

def data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return (humidity, temperature)

@app.route('/', methods=['GET'])
def index():
    humidity, temperature = data()
    return jsonify(
        humidity=humidity,
        temperature=temperature
    )

if __name__ == '__main__':
   app.run(debug=False, host="0.0.0.0", port="5000")
#     app.run(host="0.0.0.0", port="5000")

