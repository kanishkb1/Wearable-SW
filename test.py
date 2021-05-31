from flask import Flask, request, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test_db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class User(db.Document):
   name = db.StringField()
   email = db.StringField()
   
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/wearable-testing/data', methods = ['POST'])
def data():
    content = request.get_json()
    print(content)
    return 'JSON received'

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')