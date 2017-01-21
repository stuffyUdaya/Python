from flask import Flask,render_template,request,redirect,session, flash
from mysqlconnection  import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'THISISSECRET'
@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def process():
    if len(request.form['email'])<1:
        flash("Email cant be blank",'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invaid Email','error')
    else:
        flash('success','success')
        query = 'insert into email(email,updated_at) values(:email,now())'
        data = {
                'email':request.form['email']

        }

        
    return redirect('/')
app.run(debug=True)
