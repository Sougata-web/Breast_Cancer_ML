import numpy as np
import pandas as pd
import pickle

from flask import Flask

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('app.html')
    