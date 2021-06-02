# code for parsing json file
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, request, render_template
from flask_pymongo import PyMongo
import datetime
import json

# creating a Flask app
app = Flask(__name__)
# path to the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/med_sensor_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db


# provides homepage for the visitor
@app.route('/')
def index():
    print('Welcome')
    return render_template('index.html')


# pushed the data send by the device to cloud
@app.route('/wearable-testing/data', methods=['POST'])
def data():
    content = request.get_json()
    #print(content)
    #print(type(content))
    server_ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Server Timestamp is: ' + server_ts)
    content["s_ts"] = "%s" % server_ts
    print("final string", content)
    db.sensor_data.insert_one(content)
    return 'record added to db'


# pushed the data send by the device to cloud
@app.route('/wearable/data', methods=['POST'])
def wearable_data():
    content = request.get_json()
    server_ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Server Timestamp is: ' + server_ts)
    content["s_ts"] = "%s" % server_ts
    print("final string", content)
    db.wearable_sensor_data.insert_one(content)
    return 'record added to db'


# driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
