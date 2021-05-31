import flask
from flask_pymongo import PyMongo
from pymongo.errors import BulkWriteError

app = flask.Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def home():
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])

@app.route("/get_todo/<int:todoId>")
def insert_one(todoId):
    todo = db.todos.find_one({"_id": todoId})
    return todo

@app.route("/replace_todo/<int:todoId>")
def replace_one(todoId):
    result = db.todos.replace_one({'_id': todoId}, {'title': "modified title"})
    return {'id': result.raw_result}

@app.route("/update_todo/<int:todoId>")
def update_one(todoId):
    result = db.todos.update_one({'_id': todoId}, {"$set": {'title': "updated title"}})
    return result.raw_result

@app.route("/delete_todo/<int:todoId>", methods=['DELETE'])
def delete_todo(todoId):
    todo = db.todos.delete_one({'_id': todoId})
    return todo.raw_result


@app.route("/save_file", methods=['POST', 'GET'])
def save_file():
    upload_form = """<h1>Save file</h1>
                     <form method="POST" enctype="multipart/form-data">
                     <input type="file" name="file" id="file">
                     <br><br>
                     <input type="submit">
                     </form>"""

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            mongodb_client.save_file(file.filename, file)
            return {"file name": file.filename}
    return upload_form

@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': 'todo title', 'body': 'todo body'})
    return flask.jsonify(message="success")

@app.route("/add_many")
def add_many():
    try:
        todo_many = db.todos.insert_many([
            {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
            {'_id': 8, 'title': "todo title two", 'body': "todo body two"},
            {'_id': 2, 'title': "todo title three", 'body': "todo body three"},
            {'_id': 9, 'title': "todo title four", 'body': "todo body four"},
            {'_id': 10, 'title': "todo title five", 'body': "todo body five"},
            {'_id': 5, 'title': "todo title six", 'body': "todo body six"},
        ], ordered=False)
    except BulkWriteError as e:
        return flask.jsonify(message="duplicates encountered and ignored",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return flask.jsonify(message="success", insertedIds=todo_many.inserted_ids)

@app.route('/wearable-testing/data', methods=['POST'])
def data():
    content = request.get_json()
    print(content)

    return 'JSON received'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
