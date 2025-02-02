import os

from flask import Flask, render_template, request
from backend import app
from backend import *

@app.route('/login', methods = ['POST', 'GET'])
def verify_user_credentials():
    # credentials_received = []
    # credentials_list.append(request.form['login_username'])
    # credentials_list.append(request.form['login_password'])
    
    # if (credentials_received in credentials_list):
    #     return render_template(homepage_file)
    
    # TODO: else, set error message

    # print(request.args.get('login_username'))

    # if ("login_submit" in request.form):
    #     render_template(set_up_data.homepage_file)
    # else:
    #     render_template(set_up_data.user_page_file)

    return render_template(set_up_data.homepage_file)
