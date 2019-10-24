#import os
#import random
#import time
#import json
import subprocess
from celery import Celery
from celery.result import AsyncResult
from flask import Flask, request, render_template#, session, flash, redirect, url_for, jsonify, send_from_directory


#START CELERY CONFIG

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

#Celery configuration
app.config['CELERY_BROKER_URL'] = 'pyamqp://airfoil:group8@10.10.10.8/g8host'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'


#Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.update(app.config)
celery.conf['CELERY_TASK_SERIALIZER'] = 'json'
celery.conf['CELERY_RESULT_SERIALIZER'] = 'json'
celery.conf['CELERY_ACCEPT_CONTENT'] = ['json', 'pickle']

#START CELERY METHODS

@celery.task
def airfoil_r2a15n200(): #This is just an example
    subprocess.run(["./airfoil", "10", "0.0001", "10.", "0.01", "../cloudnaca/msh/r2a15n200.xml"])
    f = open('results/drag_ligt.m', 'r')
    return f.read()

#END CELERY METHODS
#START FLASK METHODS

#This is just to render the simple webpage
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

#This is a curl test method without celery worker input
@app.route('/test', methods=['GET'])
def test_curl():
	if request.method == 'GET':
		return 'hello, World'

#This is a curl test method with celery worker input
@app.route('/celery_test/r2a15n200', methods=['GET'])
def test_celery_curl():
	if request.method == 'GET':
		task = airfoil_r2a15n200.delay()
		async_result = AsyncResult(id=task.task_id, app=celery)
		processing_result = async_result.get()
		return str(processing_result)


if __name__ == '__main__':
    app.run(debug=True)
