from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

# from programData import programmingData  
with open('results.json') as programData:
    data = json.load(programData)

errorMessage = [{'id': 99999, 'name': 'No Program Language Found', 'summary': 'Sorry the Language you are looking for is not listed. Please, look up another one and try again. Thank you'}]

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
## Search API by Id
@app.route('/api/id/<id>', methods=['GET'])
def apiFindById(id=None):
    try:
        if(list(filter(lambda x: x["id"] == int(id), data))):
            idInformation = list(filter(lambda x: x["id"] == int(id), data))
            return(jsonify(idInformation))
        else:
            return(jsonify(errorMessage))
    except:
        return(jsonify(errorMessage))
## Search API by snippet of a name       
@app.route('/api/name/<name>', methods=['GET'])
def programByName(name=None):
    if request.method =='GET':
        if name:
            try:
                nameResults = list(filter(lambda x: name.lower() in x["name"].replace("(programming language)", "").lower() , data)) 
                if len(nameResults) == 0:
                    return(jsonify(errorMessage))
                else:
                    return (jsonify(nameResults))           
            except:
                return(jsonify(errorMessage))

app.run(port=3000, debug=True)