import os

from flask import Flask, render_template, request
from backend import app
from set_up_data import *

@app.route('/login.html', methods = ['POST'])
def verify_user_credentials():
    credentials_received = []
    credentials_list.append(request.form['login_username'])
    credentials_list.append(request.form['login_password'])
    
    if (credentials_received in credentials_list):
        return render_template(homepage_file)
    
    # TODO: else, set error message
