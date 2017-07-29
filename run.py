# Use conda u idiots
"""
export FLASK_APP=run.py
python -m flask run
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return "IMAGE HERE"
