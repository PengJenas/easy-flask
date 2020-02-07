# -*- coding: utf-8 -*-
from flask import Flask,send_file,redirect,url_for,request
import argparse
import os
import time

parser = argparse.ArgumentParser(description="your http port") 
parser.add_argument('--port',type=int,default=80)
args = parser.parse_args() 

filePath = os.path.dirname(__file__)
logPath = os.path.join(filePath,'log')
with open(logPath,'w') as f:
    f.write('Welcome !')

app = Flask(__name__)
@app.route('/')
def index():
    return send_file("index.html")

@app.route('/readlog')
def log():
    with open(logPath,'r') as f:
        log_list = f.readlines()
    log_txt = '<br />'.join(reversed(log_list))
    return log_txt

@app.route('/dellog')
def dellog():
    ip = request.remote_addr
    nowtime = time.strftime(r"%d/%b/%Y %H:%M:%S")
    with open(logPath,'w') as f:
        # 111.222.333.444 - - [12/Oct/2019 07:37:10] "GET /readlog HTTP/1.1" 200 -
        f.write('{} - - [{}] "Clear log" - \n'.format(ip,nowtime))
    return redirect(url_for('log'))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=args.port)
