#!flask/bin/python
from flask import Flask, jsonify
from tinydb import TinyDB, Query
import subprocess
import os
import sys
from tasks import airfoil_calc

app = Flask(__name__)
db = TinyDB('db.json')
xml_files = ['r2a0n200.xml', 'r3a3n200.xml', 'r1a9n200.xml', 'r0a6n200.xml', 'r3a9n200.xml', 'r3a15n200.xml', 'r3a24n200.xml', 'r1a24n200.xml', 'r2a9n200.xml', 'r2a12n200.xml', 'r3a12n200.xml', 'r2a30n200.xml', 'r2a15n200.xml', 'r1a27n200.xml', 'r0a12n200.xml', 'r0a0n200.xml', 'r3a18n200.xml', 'r1a15n200.xml', 'r0a21n200.xml', 'r1a12n200.xml', 'r2a18n200.xml', 'r2a3n200.xml', 'r3a6n200.xml', 'r1a30n200.xml', 'r0a27n200.xml', 'r2a24n200.xml', 'r1a18n200.xml', 'r3a30n200.xml', 'r2a6n200.xml', 'r3a0n200.xml', 'r2a27n200.xml', 'r0a15n200.xml', 'r0a18n200.xml', 'r0a9n200.xml', 'r0a30n200.xml', 'r1a6n200.xml', 'r0a24n200.xml', 'r3a27n200.xml', 'r1a0n200.xml', 'r3a21n200.xml', 'r2a21n200.xml', 'r1a3n200.xml', 'r1a21n200.xml', 'r0a3n200.xml']
xml_files.sort()

@app.route('/test', methods=['GET'])
def airfoil():
    airfoilDB = Query()
    final_result = {}
    for xml_file in xml_files[0:5]:
        dbResponse = db.search(airfoilDB.filename == xml_file)
        if (not dbResponse):
            data = airfoil_calc.delay(xml_file)
            result = data.get()
            record = {'filename': xml_file, 'result': result}
            db.insert(record)
            final_result[xml_file] = result
        else:
            final_result[xml_file] = dbResponse[0]['result']
    return final_result

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
