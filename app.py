#! /usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
import geocoder as geo

# by: 2023BCD0002

# create flask app
app = Flask(__name__)

# enable CORS for all routes
CORS(app)

# Enable Prometheus metrics on the /metrics endpoint
metrics = PrometheusMetrics(app)

@app.route('/')
def get_location():
    # get the geolocation data for the IP address
    location = geo.ip('me')
    lat, long = location.latlng
    # render index.html with the data
    return render_template('index.html', 
            latitude=lat, 
            longitude=long, 
            city=location.city, 
            country=location.country)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)