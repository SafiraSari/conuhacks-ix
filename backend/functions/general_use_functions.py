import os

from flask import Flask, render_template, request
from backend import app
from set_up_data import *

@app.route('/<path>', method = ['POST'])
def handle_navbar_click():
    return_file = ""
    
    if ("player_profile" in request.form):
        return_file = user_page_file
    elif ("custom_lists" in request.form):
        return_file = custom_lists_file
    elif ("game_statistics" in request.form):
        return_file = game_statistics_file
    elif ("homepage" in request.form):
        return_file = homepage_file
    elif ("trending_games" in request.form):
        return_file = trending_games_file
    
    if (return_file != ""):
        return render_template(return_file)