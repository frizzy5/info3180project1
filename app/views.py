"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, json, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import ProfileForm
from app.models import UserProfile
from werkzeug.utils import secure_filename
import time
import os
import random


###
# Routing for your application.
###

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile/', methods=['GET', 'POST'])
def newprofile():
    form = ProfileForm()
    
    if request.method == "POST":
        if form.validate_on_submit():
            first_name = request.form['firstname']
            last_name = request.form['lastname']
            username = request.form['username']
            age = request.form['age']
            biography = request.form['biography']
            gender = request.form['gender']
           
            pics = app.config["UPLOAD_FOLDER"]
            imagen = request.files['image']
            imageName = secure_filename(imagen.filename)
            imagen.save(os.path.join(pics, imageName))
            
            while True:
                userid = random.randint(10000, 55555)
                result = db.session.query.filter_by(userid=userid).first() 
                if result is None:
                    break
            
            created_on = time.strftime("%d %b %Y")
            
            newuser = UserProfile(userid,username,first_name,last_name,gender,age,biography,created_on,imageName)
            db.session.add(newuser)
            db.session.commit()
            
            flash('New profile created', 'success')
            return redirect(url_for('profiles'))
        
    flash_errors(form)
    return render_template('add_profile.html', form=form)

@app.route('/profiles', methods=['GET','POST'])
def profiles():
    profiles = db.session.query(UserProfile).all()
    
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        allprofiles = []
        for profile in profiles:
            profilelist = {'username': profile.username, 'userid': profile.userid}
            allprofiles.append(profilelist)
        return jsonify(users=allprofiles)
    else:
        if not profiles:
            flash('No users to show.', 'danger')
            return redirect(url_for('add_profile'))
        return render_template('profiles_list.html', profiles=profiles)
    
@app.route('/profile/<userid>', methods=['GET','POST'])
def view_profile(userid):
    user = UserProfile.query.filter_by(userid=userid).first()

    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        return jsonify(userid=user.userid, username=user.username, image=user.image, gender=user.gender, age=user.age, created_on=user.created_on)
    elif request.method == 'GET':
        return render_template('view_user_profile.html', user=user)
    else:
        flash('User not found.','danger')
        return redirect(url_for('profiles'))
           
    

###
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in %s field - %s" % (getattr(form,field).label.text, error ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")