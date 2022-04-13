#!/usr/bin/env python
import os
import json
import traceback
import base64
import logging
import psycopg2
from datetime import date, datetime
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='10.5.0.5',
                            database='postgres',
                            user='postgres',
                            password='fiap123')
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM links;')
    links = cur.fetchall()
    alunos = []
    for link in links:
        alunos.append(link)
    return jsonify(alunos)

@app.route("/Teste")
def Teste():
    return "API Ok\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)