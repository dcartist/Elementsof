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
@app.route('/all')
def programlisting():
    return render_template('listing.html', data = data)

@app.route('/program/id/<id>', methods=['GET'])
def programById(id=None):
    try:
        programInfo = list(filter(lambda x: x["id"] == int(id), data)) 
        print(programInfo[0]["name"])
    except:
        programInfo = [{'id': 99999, 'name': 'No Program Language Found', 'summary': 'Sorry the Language you are looking for is not listed. Please, look up another one and try again. Thank you'}]

    return render_template('program.html', id =id, program=programInfo[0], data = data)
    

@app.route('/api/', methods=['GET'])
def apiIndex():
    if request.method == 'GET':
        return(jsonify(data))


app.run(port=3000, debug=True)