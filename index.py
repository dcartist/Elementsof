from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

# from programData import programmingData  
with open('results.json') as programData:
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
        summary = programInfo[0]["summary"].split("\n\n")
        return render_template('program.html', id =id, program=programInfo[0], data = data, summary = summary)
    
    except:
        return render_template('error.html')
    

@app.route('/api/', methods=['GET'])
def apiIndex():
    if request.method == 'GET':
        return(jsonify(data))

@app.route('/api/id/<id>', methods=['GET'])
def apiFindById(id=None):
    try:
        if(list(filter(lambda x: x["id"] == int(id), data))):
            idInformation = list(filter(lambda x: x["id"] == int(id), data))
            return(jsonify(idInformation))
        else:
            errorMessage = [{'id': 99999, 'name': 'No Program Language Found', 'summary': 'Sorry the Language you are looking for is not listed. Please, look up another one and try again. Thank you'}]
            print(errorMessage)
            return(jsonify(errorMessage))
    except:
        errorMessage = {'id': 99999, 'name': 'No Program Language Found', 'summary': 'Sorry the Language you are looking for is not listed. Please, look up another one and try again. Thank you'}
        return(jsonify(errorMessage))
        



app.run(port=3000, debug=True)