import sys
import os
import insertBlob
import subprocess
from celery import Celery

CELERY_BROKER_URL = 'pyamqp://airfoil:group8@10.10.10.8/g8host'
CELERY_RESULT_BACKEND = 'rpc://'

task_name = sys.argv[0][:-3]
celery = Celery(task_name, broker= CELERY_BROKER_URL, backend= CELERY_RESULT_BACKEND)
celery.conf['CELERY_TASK_SERIALIZER'] = 'json'
celery.conf['CELERY_RESULT_SERIALIZER'] = 'json'
celery.conf['CELERY_ACCEPT_CONTENT'] = ['json', 'pickle']

@celery.task
def airfoil_calc(file_name):
    subprocess.run(["./airfoil", "10", "0.0001", "10.", "0.01", "../cloudnaca/msh/"+file_name])
    currentPath = os.getcwd()
    pathToResults = currentPath +"/results/"
    insertBlob.insertingAllResults(file_name, pathToResults)
    return
