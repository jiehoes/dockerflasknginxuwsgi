# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import sys, traceback
app = Flask(__name__)

@app.route("/") 
@app.route("/index")
def index():
    try:
        return render_template('index.html')
    except:
        return get_exception()


def get_exception():
    error_type, error_message, exc_traceback = sys.exc_info()
    return '''
Error Message: {error_message}
Error Type: {error_type}
Traceback: {traceback}
    '''.format(
                error_type=error_type,
                error_message=error_message,
                traceback=exc_traceback.format_exc().strip(),
              ).strip()


def get_client_ip():
    'Gets client IP from xforward for or remote address if not proxied'
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    else:
        return request.remote_addr

