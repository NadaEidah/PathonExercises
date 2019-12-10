#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:33:28 2019

@author: nada
"""


#Exercises DAY 15
print('--------Exercise 1--------------')
'''
from flask import Flask,request,render_template
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST','GET'])
def result():
   if request.method=='POST':
       result=request.form
       return render_template('result.html', result=result)
   
   
if __name__=='__main__':
    app.run()
'''      
print('--------Exercise 2--------------')     

from flask import Flask,render_template
import sqlite3 as sql

DATABASE="stocks.db"

app=Flask(__name__)
@app.route("/")
def index():
    with sql.connect(DATABASE) as con:
        cur=con.cursor()
    res=cur.execute("select * from  stocks")
    return render_template("index1_3.html",users=res)

if __name__=='__main__':
    app.run()