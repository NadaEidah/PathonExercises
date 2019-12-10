#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:01:32 2019

@author: nada
"""

#Exercises DAY 16
print('--------Exercise 1--------------')

from flask import *
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home1_2.html")

@app.route("/enternew")
def new_student():
    return render_template("students1_2.html")

@app.route("/addrec", methods=["POST","GET"])
def addrec():
    if request.method == 'POST':
        try:
            name=request.form['name']
            addr=request.form['addr']
            city=request.form['city']
            pin=request.form['pin']
            
            with sql.connect('ex16.db') as con:
                cur=con.cursor()
    
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?,?,?,?)",(name,addr,city,pin))

                con.commit()
                msg="Record successfully added"
        except:
            con.rollback()
            msg="erro in insert operation"
        
        finally:
            return render_template("result1_2.html", msg=msg)
            con.close()
            
@app.route('/list')
def list():
    con=sql.connect('ex16.db')
    con.row_factory=sql.Row
    
    cur=con.cursor()
    cur.execute('select * from students')
    
    rows=cur.fetchall();
    return render_template("list1_2.html",users=rows)

if __name__=='__main__':
    app.run(debug=True)