import os
import random
import time
from celery import Celery
from celery.result import AsyncResult


#START CELERY CONFIG


#Celery configuration
#Initialize Celery
celery = Celery(__name__, broker='pyamqp://rabbit_test_user:1234@localhost/rabbit_test_vhost', backend='rpc://')


#START CELERY METHODS

@celery.task
def example_celery_method(): #This is just an example
	time.sleep(4)
	return 'I have sleept for 4 seconds'


#END CELERY METHODS
#START FLASK METHODS


if __name__ == '__main__':
    celery.run(debug=True)

#if __name__ == '__main__':
#	app.run(host='0.0.0.0', debug=True)