#!/usr/bin/env python
import json
import traceback
import base64
import logging
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá Mundo!\n"

@app.route("/Teste")
def Teste():
    return "Hello World!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)