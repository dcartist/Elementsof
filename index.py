from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

# from programData import programmingData  
with open('programData.json') as programData:
    data = json.load(programData)

app = Flask(__name__)
cors = CORS(app)