from flask import Blueprint, render_template  #Blueprint is used to have views divided into different files 
from flask_login import login_required, current_user 

views = Blueprint('views', __name__) 

@views.route('/') #explains what to do when someone visits your website 

@login_required

def home(): 
    return render_template("home.html", user=current_user)



























