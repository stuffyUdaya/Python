from flask import Flask,render_template,request,redirect,session,flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?!.*[^a-zA-Z0-9])(.{8,15})$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="ThisisSecret"
mysql = MySQLConnector(app,'reglogindb')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register',methods=['GET'])
def register():
    return render_template('reg.html')
@app.route('/create',methods=['POST'])
def create():
    flashMessage = False
    if len(request.form['first_name'])<1:
        flash("required First Name")
        flashMessage = True
    elif len(request.form['last_name'])<1:
        flash("required Last Name")
        flashMessage = True
    elif len(request.form['reg_password'])<8:
        flash("password must be atleast 8 characters",'error')
        flashMessage = True
    elif not EMAIL_REGEX.match(request.form['reg_email']):
        flash("not a valid email address")
        flashMessage = True
    elif request.form['reg_password']!=request.form['reg_passwordconf']:
        flash("Password and Confirmation password are not matched")
        flashMessage = True
    elif not PWD_REGEX.match(request.form['reg_password']):
        flash("Password must contain atleast one Uppercase and a number!!","error")
        flashMessage = True
    if flashMessage == True :
        return redirect('/register')


    else:

        flash("successfully registered ")
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        reg_email = request.form['reg_email']
        reg_password = request.form['reg_password']
        reg_passwordconf = request.form['reg_passwordconf']
        pw_hash = bcrypt.generate_password_hash(reg_password)
        print pw_hash
        query = 'insert into registrations (first_name,last_name,reg_email,reg_password,created_at) values(:first_name,:last_name,:reg_email,:pw_hash,now())'
        data = {
                'first_name': first_name ,
                'last_name' : last_name,
                'reg_email':reg_email,
                'pw_hash':pw_hash


        }

        mysql.query_db(query,data)

        return redirect('/login')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/process',methods=['POST'])
def process():
    reg_email = request.form['log_email']
    reg_password = request.form['log_password']
    user_query = "SELECT * FROM registrations WHERE registrations.reg_email = :reg_email"
    query_data = { 'reg_email': reg_email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    
    if bcrypt.check_password_hash(user[0]['reg_password'], reg_password):

        return render_template("loggedin.html")
    else:
        flash("incorrect credentials")
        return redirect('/login')
app.run(debug=True)
