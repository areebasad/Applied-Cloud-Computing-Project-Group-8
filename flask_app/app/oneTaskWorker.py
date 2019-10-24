import subprocess
from celery import Celery

CELERY_BROKER_URL = 'pyamqp://airfoil:group8@10.10.10.8/g8host'
CELERY_RESULT_BACKEND = 'rpc://'

celery = Celery('testCelery', broker= CELERY_BROKER_URL, backend= CELERY_RESULT_BACKEND)
celery.conf['CELERY_TASK_SERIALIZER'] = 'json'
celery.conf['CELERY_RESULT_SERIALIZER'] = 'json'
celery.conf['CELERY_ACCEPT_CONTENT'] = ['json', 'pickle']

@celery.task
def airfoil_r2a15n200():
    subprocess.run(["./airfoil", "10", "0.0001", "10.", "0.01", "../cloudnaca/msh/r2a15n200.xml"])
    f = open('results/drag_ligt.m', 'r')
    return f.read()