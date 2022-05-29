from flask import Flask, render_template, request, url_for
from foodborne import app
from foodborne.models import randomForestRegressor
import numpy as np


@app.route('/')
@app.route('/home')
def home():
  return render_template("default.html")

@app.route('/results', methods=['POST'])
def getStuffFromWebsite():
  if request.method == "POST":
    field = request.form['symbol1']
    
    field2=request.form['symbol2']
    
    field3=request.form['symbol3']
    field4=request.form['symbol4']
    field5=request.form['symbol5']
    field6=request.form['symbol6']
    arr=np.array([ field3, field4, field5, field6])


    
    #arr=float(arr)
    
    arr=np.reshape(arr, (1,4))
    
    predictions = randomForestRegressor(arr)
    return render_template("results.html", predictions=predictions)
  return render_template("default.html")



