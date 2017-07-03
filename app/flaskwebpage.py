# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import sys, os, traceback
app = Flask(__name__)

@app.route("/") 
@app.route("/index")
def index():
    try:
        return render_template('index.html')
    except:
        return get_exception()


def get_exception():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return '''
Python Version: {version}
File: {file_name}
Error Type: {error_type}
Error Message: {error_message}
Traceback: 
{traceback}
         '''.format(
                    version =sys.version.split("(")[0],
                    file_name = fname,
                    error_type = exc_type.__name__,
                    error_message = exc_obj,
                    traceback = traceback.format_exc().replace(", in ",", in \n"),
                    )


def get_client_ip():
    'Gets client IP from xforward for or remote address if not proxied'
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    else:
        return request.remote_addr

