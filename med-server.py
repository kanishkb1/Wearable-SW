#code for parsing json file
# Using flask to make an api
# import necessary libraries and functions

from flask import Flask, jsonify, request, render_template
  
# creating a Flask app
app = Flask(__name__)
# path to the database
db_path = "<enter your db path here>"

# returns simple strings when we use GET.
# returns the data that we send when we use POST.
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/wearable-testing/data', methods = ['POST'])
def data():
    content = request.get_json()
    print(content)
    return 'JSON received'



# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({})
  
  
# driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)