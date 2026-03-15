#! /usr/bin/env python3

from flask import Flask, request, render_template
from flask_cors import CORS
import geocoder as geo

# create flask app
app = Flask(__name__)

# enable CORS for all routes
CORS(app)

@app.route('/')
def get_location():
    # get the client's IP address
    ip_address = request.remote_addr

    # get the geolocation data for the IP address
    location = geo.ip(ip_address)

    # render index.html with the data
    return render_template('index.html', 
            latitude=location.latlng[0], 
            longitude=location.latlng[1], 
            city=location.city, 
            country=location.country)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)