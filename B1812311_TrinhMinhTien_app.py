# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 10:05:24 2022

@author: Admin
"""
from B1812311_TrinhMinhTien_train import predict_iris
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/result", methods=['post'])
def form_handle():
    sl = request.form.get('sl')
    sw = request.form.get('sw')
    pl = request.form.get('pl')
    pw = request.form.get('pw')
    result = predict_iris(sl, sw, pl, pw)
    return render_template("index.html", message = result)

if __name__ == "__main__":
    app.run(debug=True)
