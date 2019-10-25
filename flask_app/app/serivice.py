#!flask/bin/python
from flask import Flask, jsonify
from tinydb import TinyDB, Query
import subprocess
import sys
from testCelery import airfoil_r2a15n200

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/test', methods=['GET'])
def airfoil(filename):
   #I need to check if this filename is in the database or not and store the result also
   #String
    airfoilDB = Query()
    dbResponse = db.search(airfoilDB.filename == filename)
    print(dbResponse)
    if (len(dbresponse == 0 )):
        data = airfoil_r2a15n200.delay()
        result = data.get()
        record = {'filename': filename, 'result': result}
        db.insert(record)
        print(db.all)
        return result
    else:
        print(dbResponse)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
