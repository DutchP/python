#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  models.py

# ######################################################################
# Imports
# ######################################################################
from flask import Flask,request,url_for,flash,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms.fields.simple import TextField, SubmitField
from flask_wtf.form import FlaskForm

# ######################################################################
app = Flask(__name__)

# ######################################################################
app.config["SECRET_KEY"]= "secret"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config.from_object(__name__)
app.debug=True
# ######################################################################
db = SQLAlchemy()
db.echo=False

# ######################################################################
# we got some list containing names
babynames = []

class NamesForm(FlaskForm):
	name = TextField("Baby name")
	submit = SubmitField("Send")

@app.route('/')
def index():
	"""docstring for inde method"""
	form = NamesForm()
	return render_template('index.html',form = form,babynames= babynames)

@app.route("/add",methods=['GET','POST'])
def add():
	"""docstring for add method"""
	if request.method == 'POST' and request.form['name'] != '':
		name = request.form['name']
		babynames.append(name)
		return redirect(url_for('index'))
	else:
		form = NamesForm()
		return render_template('index.html',form = form,babynames= babynames)
	
if __name__=='__main__':
	app.run(port=80)
