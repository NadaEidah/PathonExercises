#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:51:23 2019

@author: nada
"""

#Exercises DAY 14
print('--------Exercise 1--------------')

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return 'This is the Index page from Exercise 1'

'''
@app.route('/hello')
def hello():
    return 'Hello World! from Exercise 1'

@app.route('/members')
def members():
    return 'Members Page from Exercise 1'


if __name__=='__main__':
    app.run()
'''    

print('--------Exercise 2--------------')

@app.route('/score/<int:score>')
def score(score):
  return render_template('ex2.html', marks=score)

    
print('--------Exercise 3--------------')


@app.route('/css')
def css():
  return render_template('ex3.html')


if __name__=='__main__':
    app.run()