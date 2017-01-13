from flask import Flask, session, render_template, redirect, request, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?!.*[^a-zA-Z0-9])(.{8,15})$')
DATE_REGEX = re.compile(r'^(((0?[1-9]|1[012])/(0?[1-9]|1\d|2[0-8])|(0?[13456789]|1[012])/(29|30)|(0?[13578]|1[02])/31)/(19|[2-9]\d)\d{2}|0?2/29/((19|[2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00)))$')
app = Flask(__name__)
app.secret_key="Thisissecret"
@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process',methods=['POST'])
def process():

    if len(request.form['f_name'])<1:
        flash("required First Name")
    elif len(request.form['l_name'])<1:
        flash("required Last Name")
    elif len(request.form['password'])<8:
        flash("password must be atleast 8 characters",'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("not a valid email address")
    elif request.form['password']!=request.form['confpassword']:
        flash("Password and Confirmation password are not mtched")
    elif not DATE_REGEX.match(request.form['birthdate']):
        flash("Enter a valid Birth Date")
    elif not PWD_REGEX.match(request.form['password']):
        flash("Password must contain atleast one Uppercase and a number!!","error")

    else:
        flash('Thanks for Submitting your Info','success')
    return redirect('/')

app.run(debug=True)
