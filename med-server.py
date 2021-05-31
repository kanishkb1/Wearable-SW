# code for parsing json file
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo.errors import BulkWriteError

# creating a Flask app
app = Flask(__name__)
# path to the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/med_sensor_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db


# returns simple strings when we use GET.
# returns the data that we send when we use POST.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wearable-testing/data', methods=['POST'])
def data():
    content = request.get_json()
    print(content)
    db.sensor_data.insert_one(content)
    return 'record added to db'


# driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
