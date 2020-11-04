from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

# from programData import programmingData  
with open('programData.json') as programData:
    data = json.load(programData)

app = Flask(__name__)
cors = CORS(app)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    print(data)
    return render_template('index.html')
@app.route('/api/', methods=['GET'])
def apiIndex():
    if request.method == 'GET':
        return(jsonify(data))


app.run(port=3000, debug=True)